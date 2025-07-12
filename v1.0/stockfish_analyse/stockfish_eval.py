from stockfish import Stockfish
import chess
from dotenv import load_dotenv
import os

load_dotenv()
path = os.getenv('STOCKFISH_PATH')
stockfish = Stockfish(
    path=path
)
board = chess.Board()


def normalize_eval(eval_dict):
    """
    Converts Stockfish eval dict to (centipawn equivalent, mate_in if any)
    """
    if eval_dict['type'] == 'cp':
        return eval_dict['value'], None
    elif eval_dict['type'] == 'mate':
        # Convention: mate = big value for diff, sign indicates side
        mate_score = 10000 if eval_dict['value'] > 0 else -10000
        return mate_score, eval_dict['value']
    else:
        return 0, None


def generate_evaluations_from_memory(moves):
    evaluations = []
    board.reset()

    for idx, move_san in enumerate(moves):
        color = "white" if board.turn == chess.WHITE else "black"
        move_number = idx + 1

        move = board.parse_san(move_san)

        # Set up current position
        uci_moves = [m.uci() for m in board.move_stack]
        stockfish.set_position(uci_moves)

        # Get top 3 moves
        top_moves = stockfish.get_top_moves(3)
        best_move_uci = top_moves[0]['Move']
        best_move_cp = top_moves[0]['Centipawn']
        best_move_mate = top_moves[0].get('Mate')  # Could be None

        # Normalize best move eval
        if best_move_mate is not None:
            best_eval = 10000 if best_move_mate > 0 else -10000
            best_mate_in = best_move_mate
        else:
            best_eval = best_move_cp
            best_mate_in = None

        # Played move eval
        board.push(move)
        uci_moves_played = [m.uci() for m in board.move_stack]
        stockfish.set_position(uci_moves_played)
        played_eval_raw = stockfish.get_evaluation()
        played_eval, played_mate_in = normalize_eval(played_eval_raw)

        # Absolute diff
        abs_diff = abs(played_eval - best_eval)

        # Did we play best?
        played_is_best = (move.uci() == best_move_uci)

        evaluations.append({
            'move': move_san,
            'move_number': move_number,
            'color': color,
            'stockfish_eval_cpn': played_eval,
            'mate_in': played_mate_in,
            'next_best_3_moves': top_moves,
            'is_best_move': played_is_best,
            'abs_diff_cpn': abs_diff
        })

    return evaluations
