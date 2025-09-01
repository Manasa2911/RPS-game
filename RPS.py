import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    last3 = "".join(opponent_history[-3:])
    predictions = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        if pattern == last3:
            next_move = opponent_history[i+3]
            if next_move in predictions:
                predictions[next_move] += 1

    if sum(predictions.values()) == 0:
        predicted_move = random.choice(["R", "P", "S"])
    else:
        predicted_move = max(predictions, key=predictions.get)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted_move]

