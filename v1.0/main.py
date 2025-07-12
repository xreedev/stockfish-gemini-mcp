from memory_storage import create_memory, convert_pgn_to_memory,set_stockfish_evaluation,get_summarized_evaluation,read_memory
from gemini import generate_evaluation
from pgn_parser import read_pgn_data
from stockfish_analyse import generate_evaluations_from_memory

#config (need to move to env,along with API key)
path_to_pgn = 'public/data.pgn'
path_to_json = 'public/data.json'

#read pgn data and save to memory
pgn_data = read_pgn_data(path_to_pgn)
memory = create_memory(path_to_json)
memory = convert_pgn_to_memory(pgn_data,memory)

#generate stockfish evaluations and add to memory
evaluations = generate_evaluations_from_memory(memory.moves)
memory = set_stockfish_evaluation(memory,evaluations)

summary = get_summarized_evaluation(memory)

print(generate_evaluation(summary))

