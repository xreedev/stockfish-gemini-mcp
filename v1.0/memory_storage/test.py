import json
from data_storage import (
    create_memory,
    read_metadata,
    write_board_data,
    read_board_data,
    get_memory,
    update_memory
)

# Replace `your_module` with the actual Python filename (without `.py`) that contains your logic.

# 1. Setup the path

json_file_path = "../public/data.json"

# 2. Create initial memory and save its JSON
print("🧠 Creating memory...")
memory_json = create_memory(json_file_path)
print(json.dumps(json.loads(memory_json), indent=4))

# 3. Set board data using a FEN string
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
print("\n📥 Writing board...")
response = write_board_data(memory_json, fen, current=True)
print(json.loads(response)["message"])

# 4. Read current board
print("\n📤 Reading current board...")
current_board_json = read_board_data(memory_json, current=True)
print(json.dumps(json.loads(current_board_json), indent=4))

# 5. Read metadata
print("\n📋 Reading metadata...")
metadata_json = read_metadata(memory_json)
print(json.dumps(json.loads(metadata_json), indent=4))

# 6. Get entire memory state
print("\n🔁 Getting memory...")
full_memory_json = get_memory(memory_json)
print(json.dumps(json.loads(full_memory_json), indent=4))

# 7. Update memory (simulate saving to file again)
print("\n💾 Updating memory (saving to file)...")
update_response = update_memory(full_memory_json)
print(json.loads(update_response)["message"])
