import json

class Memory :
    board : list
    moves : list
    evaluation : dict
    metadata : dict
    current_board : list
    file_path : str
    gemini_evaluation : str

    def __init__(self, file_path):
        self.file_path = file_path
        self.board = []
        self.evaluation = {}
        self.metadata = {}
        self.current_board = []

    def set_board(self, fen: str):
        self.board = self.convert_fen_to_2d_array(fen)

    def set_gemini_evaluation(self, eval: str):
        self.gemini_evaluation = eval

    def set_evaluation(self, evaluation: dict):
        self.evaluation = evaluation

    def set_moves(self, moves: list):
        self.moves = moves

    def set_metadata(self, metadata: dict):
        self.metadata = metadata

    def set_current_board(self, fen: str):
        self.current_board = self.board = self.convert_fen_to_2d_array(fen)

    def to_json(self) -> dict:
        return {
            "board": self.board,
            "evaluation": self.evaluation,
            "metadata": self.metadata,
            "current_board": self.current_board,
            "file_path" : self.file_path
        }

    def save_to_file(self):
        with open(self.file_path, 'w') as fw:
            json.dump(self.to_json(), fw, indent=4) # type: ignore

    def sync_from_file(self)  :
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.evaluation = data["evaluation"]
        self.metadata = data["metadata"]
        self.board = data["board"]
        self.current_board = data["current_board"]

    def convert_fen_to_2d_array(self,fen: str) -> list:
        """
        Converts a FEN string to a 2D list (8x8).
        Empty squares are represented as '.'.
        """
        rows = fen.split()[0].split('/')
        board = []

        for row in rows:
            current_row = []
            for char in row:
                if char.isdigit():
                    current_row.extend(['.'] * int(char))  # empty squares
                else:
                    current_row.append(char)
            board.append(current_row)

        return board
