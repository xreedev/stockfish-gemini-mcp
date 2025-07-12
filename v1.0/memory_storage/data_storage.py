from .data_dto import Memory
import json

def create_memory(file_path) -> Memory:
    new_memory = Memory(file_path)
    new_memory.save_to_file()
    return new_memory

def read_memory(file_path) -> Memory:
    memory = Memory(file_path)
    memory.sync_from_file()
    return memory

def read_metadata(metadata_json: str) -> str:
    memory = load_memory_from_json(metadata_json)
    memory.sync_from_file()
    return json.dumps({"metadata": memory.metadata})

def write_board_data(write_memory_json: str, fen: str, current: bool) -> str:
    memory = load_memory_from_json(write_memory_json)
    memory.sync_from_file()
    if current:
        memory.set_current_board(fen)
    else:
        memory.set_board(fen)
    memory.save_to_file()
    return json.dumps({"message": "Board updated successfully"})


def read_board_data(read_memory_json: str, current: bool) -> str:
    memory = load_memory_from_json(read_memory_json)
    memory.sync_from_file()
    board = memory.current_board if current else memory.board
    return json.dumps({"board": board})

def get_memory(updated_memory_json: str) -> str:
    memory = load_memory_from_json(updated_memory_json)
    try:
        memory.sync_from_file()
    except Exception as e:
        return json.dumps({"error": f"Memory unable to read: {str(e)}"})
    else:
        return json.dumps(memory.to_json())

def update_memory(saved_memory_json: str) -> str:
    memory = load_memory_from_json(saved_memory_json)
    try:
        memory.save_to_file()
    except Exception as e:
        return json.dumps({"error": f"Memory saving not successful: {str(e)}"})
    else:
        return json.dumps({"message": "Memory updated successfully"})

def load_memory_from_json(memory_json: str) -> Memory:
    data = json.loads(memory_json)
    memory = Memory(data['file_path'])
    memory.metadata = data.get('metadata', {})
    memory.board = data.get('board', [])
    memory.current_board = data.get('current_board', [])
    memory.evaluation = data.get('evaluation', {})
    return memory

def convert_pgn_to_memory(pgn_data : dict, memory : Memory) -> Memory:
    memory.set_metadata(pgn_data['metadata'])
    memory.set_moves(pgn_data['moves'])
    memory.set_board(pgn_data['fen'])
    memory.save_to_file()
    return memory

def set_stockfish_evaluation(memory : Memory,evaluations : dict) -> Memory:
    memory.set_evaluation(evaluations)
    memory.save_to_file()
    memory.sync_from_file()
    return memory

def get_summarized_evaluation(memory : Memory) :
    evaluations = memory.evaluation
    summary = ''

    for evaluation in evaluations:
        is_engine_move = f',is engine move' if evaluation['is_best_move'] else ''
        summary += f'{evaluation['move_number']}.{evaluation['color']} plays {evaluation['move']}, cpn difference is {evaluation['abs_diff_cpn']} {is_engine_move} '

    return summary
