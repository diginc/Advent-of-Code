require "csv"
require "daru"
require "awesome_print"
require "polars-df"

sample_p1 = "inputs/day1-sample-p1.txt"
sample_p2 = "inputs/day1-sample-p2.txt"
day_input = "inputs/day1.txt"

def get_data(file_path)
    data = []
    File.open(file_path) { |file|
        file.each_line { |ch| 
            data.concat [ch]
        }
    }
    return data
end

def part1(input)
    puts "# Part 1"
    answer = 0
    digits = []
    input.each do |line|
        digits = line.scan(/\d/)
        # ap digits
        answer += Integer(digits[0] + digits[-1])
    end
    puts "P1 Answer: #{answer}"
    return answer
end 

def part2(input)
    numbers = {
        "one": 1,
        "two": 2, 
        "three": 3,
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9,
        "1": 1, # my is_a?(numeric) ternary/elvis operators were foot-gunning me so this is a gross fix but works, anything goes after midnight, XD
        "2": 2,
        "3": 3,
        "4": 4, 
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    puts "# Part 2"
    answer = 0
    digits = []
    input.each do |line|
        matches = line.scan(/(?=(\d|one|two|three|four|five|six|seven|eight|nine))/)
        ap matches
        first = numbers[matches.first[0].to_sym]
        last = numbers[matches.last[0].to_sym]
        combined = "#{first}#{last}"
        puts combined
        answer += combined.to_i
    end
    puts "P2 Answer: #{answer}"
    return answer
end 

# ap data

part1(get_data(sample_p1)) == 142
part2(get_data(sample_p2)) == 281

part1(get_data(day_input)) == 55488
part2(get_data(day_input)) == 55614
