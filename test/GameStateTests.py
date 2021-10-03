import unittest
import uuid
from src.game_state import new_initial_move, process_new_move_into_game_state
import src.migrator as migrator


class GameStateTests(unittest.TestCase):

    def test_queue_budding_move_gets_discarded(self):
        # Arrange
        migrator.migrate_down()
        migrator.migrate_up()
        new_initial_move()

        move1 = {"nextPlayer": "O",
                 "winner": None, "stepNumber": 0, "board": [], "reference": "4872cbc4-af44-4242-a6a5-9fb1990c34a2", "previousMove": None}
        move2 = {"nextPlayer": "X",
                 "winner": None, "stepNumber": 1, "board": [], "reference": "93c03f63-4f1b-4397-92e4-2ffefd1751b7", "previousMove": move1["reference"]}
        process_new_move_into_game_state(move1)
        process_new_move_into_game_state(move2)


        new_move = {"nextPlayer": "O",
                    "winner": None, "stepNumber": 2, "board": [], "reference": str(uuid.uuid1()), "previousMove": str(uuid.uuid1())}

        # Act
        new_state= process_new_move_into_game_state(new_move)

        # Assert
        self.assertEqual(new_state["state"]["history"][-1], move2)
        

    def test_redo_move_rewrites_history(self):
        # Arrange
        migrator.migrate_down()
        migrator.migrate_up()
        new_initial_move()

        move1 = {"nextPlayer": "O",
                 "winner": None, "stepNumber": 0, "board": [], "reference": "4872cbc4-af44-4242-a6a5-9fb1990c34a2", "previousMove": None}
        move2 = {"nextPlayer": "X",
                 "winner": None, "stepNumber": 1, "board": [], "reference": "93c03f63-4f1b-4397-92e4-2ffefd1751b7", "previousMove": move1["reference"]}
        process_new_move_into_game_state(move1)
        process_new_move_into_game_state(move2)
        
        new_move = {"nextPlayer": "O",
                    "winner": None, "stepNumber": 2, "board": [], "reference": str(uuid.uuid1()), "previousMove": move1["reference"]}

        # Act
        new_state = process_new_move_into_game_state(new_move)

        # Assert
        self.assertEqual(new_state["state"]["history"][-1], new_move)


if __name__ == '__main__':
    unittest.main()
