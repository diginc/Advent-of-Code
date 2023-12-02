require "csv"
require "daru"
require "awesome_print"
require "polars-df"
require "rspec/expectations"
include RSpec::Matchers

example_p1 = "d02/d2-ex1.txt"
example_p2 = "d02/d2-ex2.txt"
real = "d02/d2-real.txt"

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
    max = {
        "red": 12,
        "green": 13,
        "blue": 13,
    }
    answer = 0
    digits = []
    input.each do |line|
        puts line
        split = line.split(":")
        add_gamenum_to_answer_if_valid = split[0].match(/\d+/)[0].to_i
        puts add_gamenum_to_answer_if_valid
        split[1].split(";").each do |game|
            game.split(",").each do |draw|
                if match_data = draw.match(/(\d+) (\w+)/)
                    number, color = match_data.captures
                end
                #ap match_data.captures
                if number.to_i > max[color.to_sym]
                    add_gamenum_to_answer_if_valid = 0
                    puts "#{number} #{color} impossible game"
                end
            end
        end
        if add_gamenum_to_answer_if_valid != 0
            answer += add_gamenum_to_answer_if_valid
            puts "ADDED GAME, now: #{answer}"
        end
    end
    puts "# P1 Answer: #{answer}"
    return answer
end 

def part2(input)
    answer = 0
    input.each do |line|
        puts line
        split = line.split(":")
        add_gamenum_to_answer_if_valid = split[0].match(/\d+/)[0].to_i
        puts add_gamenum_to_answer_if_valid
        max = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        split[1].split(";").each do |game|
            game.split(",").each do |draw|
                if match_data = draw.match(/(\d+) (\w+)/)
                    number, color = match_data.captures
                end
                #ap match_data.captures
                if number.to_i > max[color.to_sym]
                    max[color.to_sym] = number.to_i
                    puts "#{number} #{color} new max"
                end
            end
        end
        answer += max[:"red"] * max[:"green"] * max[:"blue"]
    end
    puts "# P2 Answer: #{answer}"
    return answer
end 

# ap data

puts "Examples"
expect(part1(get_data(example_p1))).to eq(8)
expect(part2(get_data(example_p2))).to eq(2286)

puts
puts "Real"
expect(part1(get_data(real))).to eq(2149)
expect(part2(get_data(real))).to eq(71274)
