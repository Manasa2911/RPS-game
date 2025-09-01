import random

def random_player(prev_play):
    return random.choice(["R", "P", "S"])

def quincy(prev_play):
    # Always cycles through the same sequence
    sequence = ["R", "P", "P", "R", "S"]
    if not hasattr(quincy, "counter"):
        quincy.counter = 0
    result = sequence[quincy.counter % len(sequence)]
    quincy.counter += 1
    return result

def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return "R"

    # Frequency analysis: count what the opponent plays the most
    most_common = max(set(opponent_history), key=opponent_history.count)
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]

def kris(prev_play):
    # Mimics what the opponent played last round
    if not prev_play:
        return "R"
    return prev_play

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 4:
        return "R"

    # Looks at the opponent's most frequent 2-move sequence
    pattern_dict = {}
    for i in range(len(opponent_history) - 2):
        key = "".join(opponent_history[i:i+2])
        next_move = opponent_history[i + 2]
        if key not in pattern_dict:
            pattern_dict[key] = {"R": 0, "P": 0, "S": 0}
        pattern_dict[key][next_move] += 1

    last_two = "".join(opponent_history[-2:])
    if last_two in pattern_dict:
        prediction = max(pattern_dict[last_two], key=pattern_dict[last_two].get)
    else:
        prediction = "R"

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]

def play(player1, player2, num_games=1000, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0
    ties = 0

    for i in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if verbose:
            print(f"Game {i+1}:")
            print(f"\tPlayer 1: {p1_move}")
            print(f"\tPlayer 2: {p2_move}")

        if p1_move == p2_move:
            ties += 1
            result = "Tie"
        elif (
            (p1_move == "R" and p2_move == "S") or
            (p1_move == "S" and p2_move == "P") or
            (p1_move == "P" and p2_move == "R")
        ):
            p1_score += 1
            result = "Player 1 wins"
        else:
            p2_score += 1
            result = "Player 2 wins"

        if verbose:
            print(f"\tResult: {result}\n")

        p1_prev = p1_move
        p2_prev = p2_move

    print("Final results:")
    print(f"\tPlayer 1 won {p1_score} times")
    print(f"\tPlayer 2 won {p2_score} times")
    print(f"\tTies: {ties}")
    win_rate = p1_score / num_games * 100
    print(f"\tWin rate for Player 1: {win_rate:.2f}%")
    return win_rate
