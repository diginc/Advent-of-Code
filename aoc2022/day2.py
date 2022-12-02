
# Opponent
# A=Rock 1 B=Paper 2 C=Scissors 3
# Your Strat
# Y=Paper 2 X=Rock 1 Z=Scissors 3 win +6

p1_scores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

x_map = {  # LOSE
    'rock': 3,
    'paper': 1,
    'scissors': 2,
}
y_map = {  # DRAW
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
z_map = {  # WIN
    'rock': 2,
    'paper': 3,
    'scissors': 1,
}



def day2(input, title):
    input = input.replace('A', "rock")
    input = input.replace('B', "paper")
    input = input.replace('C', "scissors")
    # input = input.replace('X', "rock")
    # input = input.replace('Y', "paper")
    # input = input.replace('Z', "scissors")
    input_list = input.split('\n')

    p1_answer = 0
    p2_answer = 0

    for line in input_list:
        win = False
        lose = False
        draw = False
        enemy, you = line.split(' ')
        if you == enemy:
            draw = True
        if you == "X":  # Rock
            if enemy == "scissors":
                win = True
            p2_answer += x_map[enemy]
        if you == "Y":  # Paper
            if enemy == "rock":
                win = True
            p2_answer += 3
            p2_answer += y_map[enemy]
        if you == "Z":  # Scissors
            if enemy == "paper":
                win = True
            p2_answer += 6
            p2_answer += z_map[enemy]
        if not win and not draw:
            lose = True

        p1_answer += p1_scores[you]
        if win:
            p1_answer += 6
        if draw:
            p1_answer += 3

    # Is that your final answer
    print(f"{title} Part 1: {p1_answer}")
    print(f"{title} Part 2: {p2_answer}")

