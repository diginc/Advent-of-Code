from common import *


DAY = 2
p1_scores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
translate = {
    'A': rock,
    "B": paper,
    "C": scissors,
    "X": rock,
    "Y": paper,
    "Z": scissors
}
x_map = {  # LOSE
    'A': 3,
    'B': 1,
    'C': 2,
}
y_map = {  # DRAW
    'A': 1,
    'B': 2,
    'C': 3,
}
z_map = {  # WIN
    'A': 2,
    'B': 3,
    'C': 1,
}



def main(input):
    p1_answer = 0
    p2_answer = 0

    for line in input:
        win = False
        draw = False
        enemy, you = line.split(' ')
        trnsl_enemy = translate[enemy]
        trnsl_you = translate[you]
        if trnsl_you == trnsl_enemy:
            draw = True
        if you == "X":  # Rock / Lose
            if trnsl_enemy == scissors:
                win = True
            p2_answer += x_map[enemy]
        if you == "Y":  # Paper / Draw
            if trnsl_enemy == rock:
                win = True
            p2_answer += 3
            p2_answer += y_map[enemy]
        if you == "Z":  # Scissors / Win
            if trnsl_enemy == paper:
                win = True
            p2_answer += 6
            p2_answer += z_map[enemy]

        p1_answer += p1_scores[you]
        if win:
            p1_answer += 6
        if draw:
            p1_answer += 3

    # Is that your final answer
    assert p1_answer == 10310
    assert p2_answer == 14859
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    main(read_input(f"inputs/day{DAY}.txt", split='\n\n'))
