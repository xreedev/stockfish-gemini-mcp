import chess.pgn as cpgn

def read_pgn_data(filepath: str) -> dict:
    with open(filepath) as pgn:
        first_game = cpgn.read_game(pgn)
        headers = first_game.headers

        # Extract headers
        data = {
            'Event': headers.get('Event', ''),
            'Site': headers.get('Site', ''),
            'Date': headers.get('Date', ''),
            'Round': headers.get('Round', ''),
            'White': headers.get('White', ''),
            'Black': headers.get('Black', ''),
            'Result': headers.get('Result', ''),
        }

        # Extract moves and final FEN
        moves = []
        board = first_game.board()
        node = first_game

        while node.variations:
            next_node = node.variation(0)
            move_san = board.san(next_node.move)  # SAN move
            moves.append(move_san)
            board.push(next_node.move)            # Apply move to board
            node = next_node

        final_fen = board.fen()

        return {
            'metadata': data,
            'moves': moves,
            'fen': final_fen
        }
