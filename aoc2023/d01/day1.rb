require "awesome_print"
require "rspec/expectations"
include RSpec::Matchers

example_p1 = "d01/d1-ex1.txt"
example_p2 = "d01/d1-ex2.txt"
real = "d01/d1-real.txt"

def get_data(file_path)
    data = []
    File.open(file_path) { |file|
        file.each_line { |line| 
            data.concat [line.chomp]
        }
    }
    return data
end

def numeric?(value)
  value.to_s.match?(/\A-?\d+(\.\d+)?\z/)
end

def part1(input)
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
    }
    answer = 0
    input.each do |line|
        matches = line.scan(/(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))/)
        # ap matches
        first = numeric?(matches.first[0]) ? matches.first[0] : numbers[matches.first[0].to_sym]
        last = numeric?(matches.last[0]) ? matches.last[0] : numbers[matches.last[0].to_sym]
        combined = "#{first}#{last}"
        # puts combined
        answer += combined.to_i
    end
    puts "P2 Answer: #{answer}"
    return answer
end 

# ap data

puts "Examples"
expect(part1(get_data(example_p1))).to eq(142)
expect(part2(get_data(example_p2))).to eq(281)

puts "Real"
expect(part1(get_data(real))).to eq(55488)
expect(part2(get_data(real))).to eq(55614)
