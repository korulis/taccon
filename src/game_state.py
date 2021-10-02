import uuid
import json


initial_board = [None]*9

def get_initial_move(board, nextPlayer):
    return {"nextPlayer": nextPlayer,
                 "winner": None, "stepNumber": 0, "board": board, "reference": str(uuid.uuid1()), "previousMove": None}

initial_move = get_initial_move([None]*9, "O")

def get_initial_game_state():
    return {"state": {"current": initial_move, "history": [initial_move]}} 


def generate_state(data, new_move):
    
    print(json.dumps(new_move))

    old_history = data["state"]["history"]
    old_connected_moves = list(filter(
        lambda move: move["reference"] == new_move["previousMove"], old_history))
    
    if len(old_connected_moves) == 0:
        result = data
    else:
        old_connected_move = old_connected_moves[0]
        old_connected_move_index = old_connected_move["stepNumber"]
        healthy_history = data["state"]["history"][0:old_connected_move_index+1]
        data["state"]["history"] = healthy_history

        data["state"]["current"] = new_move
        data["state"]["history"].append(new_move)
        result = data

    return result, data