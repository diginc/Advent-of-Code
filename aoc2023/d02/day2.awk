BEGIN {
    FS="[[:space:],;:]+"
    p1_answer = 0
    p2_answer = 0

    possible["red"] = 12
    possible["green"] = 13
    possible["blue"] = 14
}

{
    # print "Full line:", $0
    game = $1
    game_num = $2
    print game, "#", game_num
    max["red"] = 0
    max["green"] = 0
    max["blue"] = 0
    for (i = 3; i <= NF; i += 2) {
        number = $i
        color = $(i + 1)
        print color ":", number
        if (number > possible[color]) {
            game_num = 0
        }
        if (number > max[color]) {
            print "new", color, "max", number
            max[color] = number
        }
    } 
    if (game_num > 0) {
        print "new possible game", game_num
        p1_answer += game_num
    }
    p2_answer += max["red"] * max["green"] * max["blue"]
    print "# P1 Answer:", p1_answer
    print "# P2 Answer:", p2_answer

}

END {
    print "END"
    print "# P1 Answer:", p1_answer
    print "# P2 Answer:", p2_answer
}
