import uuid
import json
import moves_dal


def get_initial_move(board, nextPlayer):
    return {"nextPlayer": nextPlayer,
            "winner": None, "stepNumber": 0, "board": board, "reference": str(uuid.uuid1()), "previousMove": None}


initial_move = get_initial_move([None]*9, "O")


def get_initial_game_state():
    return {"state": {"current": initial_move, "history": [initial_move]}}


def new_initial_move():
    moves_dal.save(initial_move)


def __get_game_state(previous_moves, new_move):
    previous_moves.append(new_move)
    data = {"state": {}}
    data["state"]["current"] = new_move
    data["state"]["history"] = previous_moves
    return data


def get_current_game_state():
    latest_move = moves_dal.get_latest_move()
    previous_moves = moves_dal.get_previous_moves(latest_move)
    return __get_game_state(previous_moves, latest_move)


def process_new_move_into_game_state(new_move):

    print(json.dumps(new_move))

    previous_moves = moves_dal.get_previous_moves(new_move)

    if len(previous_moves) == 0:
        latest_move = moves_dal.get_latest_move()
        new_move = latest_move
        previous_moves = moves_dal.get_previous_moves(latest_move)
    else:
        moves_dal.save(new_move)

    return __get_game_state(previous_moves, new_move)