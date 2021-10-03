import unittest
import uuid
from src.game_state import process_new_move_into_game_state


class GameStateTests(unittest.TestCase):

    def test_queue_budding_move_gets_discarded(self):
        # Arrange
        move1 = {"nextPlayer": "O",
                 "winner": None, "stepNumber": 0, "board": [], "reference": "someref1", "previousMove": None}
        move2 = {"nextPlayer": "X",
                 "winner": None, "stepNumber": 1, "board": [], "reference": "someref2", "previousMove": move1["reference"]}
        game_state = {"state": {"current": move2, "history": [move1, move2]}}

        new_move = {"nextPlayer": "O",
                    "winner": None, "stepNumber": 2, "board": [], "reference": str(uuid.uuid1()), "previousMove": str(uuid.uuid1())}

        # Act
        new_state, current_data = process_new_move_into_game_state(game_state, new_move)

        # Assert
        self.assertEqual(new_state["state"]["history"][-1], move2)

    def test_redo_move_rewrites_history(self):
        # Arrange
        move1 = {"nextPlayer": "O",
                 "winner": None, "stepNumber": 0, "board": [], "reference": "someref1", "previousMove": None}
        move2 = {"nextPlayer": "X",
                 "winner": None, "stepNumber": 1, "board": [], "reference": "someref2", "previousMove": move1["reference"]}
        game_state = {"state": {"current": move2, "history": [move1, move2]}}

        new_move = {"nextPlayer": "O",
                    "winner": None, "stepNumber": 2, "board": [], "reference": str(uuid.uuid1()), "previousMove": move1["reference"]}

        # Act
        new_state, current_data = process_new_move_into_game_state(game_state, new_move)

        # Assert
        self.assertEqual(new_state["state"]["history"][-1], new_move)


if __name__ == '__main__':
    unittest.main()
