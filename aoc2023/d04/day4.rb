require "awesome_print"
require "rspec/expectations"
include RSpec::Matchers
require "matrix"

def get_data(file_path)
    return File.readlines(file_path, chomp: true)
end

def numeric?(value)
    return value.to_s.match?(/\A-?\d+(\.\d+)?\z/)
end

def get_surrounding_chars(matrix, row, col, radius)
    rows, cols = matrix.row_count, matrix.column_count
    start_row = [0, row - radius].max
    end_row = [rows - 1, row + radius].min
    start_col = [0, col - radius].max
    end_col = [cols - 1, col + radius].min
  
    submatrix = matrix.minor(start_row..end_row, start_col..end_col)
    return submatrix.to_a.flatten
end

def matrix_contains?(matrix, set_of_characters)
    return matrix.to_a.flatten.any? { |element| set_of_characters.include?(element) }
end

def part1(input)
    answer = 0
    input.each do |line|
        ap line
        win_count = 0
        game, cards = line.split(":")
        winning, cards = cards.split("|").map { |nums| nums.split(" ")}
        cards.each do |card|
            if winning.include?(card)
                win_count += 1
                puts "#{card} is winner, count: #{win_count}"
            else
                # puts "#{card} is not winner"
            end
        end
        if win_count > 0 
            answer += 2**(win_count - 1)
        end
        puts "Final points #{2**(win_count - 1)}"
    end
    return answer
end

def parse_line(line)
    game, cards = line.split(":")
    game_num = game.match(/\d+/)[0]
    winning, cards = cards.split("|").map { |nums| nums.split(" ")}
    return game_num, cards.select { |card| winning.include?(card) }
end

Card = Struct.new(:wins, :count, :copies, :matches) do
    # matches/copies are just for debug
    def initialize(wins, count, copies = [], matches = [])
      super(wins, count, copies, matches)
    end
  end
cards = {}

def add_copy(cards, i, j)
    #puts "Card #{i} gets a copy of #{j}"  # bad idea on real lol
    cards[i].copies << j
    cards[i].count += 1
    if cards[j].wins.length > 0
        cards[j].wins.each do |won_copy|
            add_copy(cards, j, won_copy)
        end
    end
end

def part2(input)
    cards = input.map.with_index { |line, i| 
        game_num, wins = parse_line(line)
        if ! wins.nil?
            puts "#{i} #{wins} OOB check #{i + wins.length} > #{input.length - 1}"
            last_copy = i + wins.length > input.length - 1 ? input.length - 1 : i + wins.length
            copies_this_card_wins = (i + 1...last_copy+1).to_a
            ap copies_this_card_wins, multiline: false
        end
        Card.new(copies_this_card_wins, 1, matches=wins)  # initialize with no copies yet, process recursively later
    }
    
    cards.each_with_index { |card, i|
        # puts "#{i} #{card}"
        card.wins.each do |copy|
            add_copy(cards, i, copy)
        end
        puts "End of original for #{i}: #{card}"
    }
    
    # cards = add_copies(cards)
    return cards.map { |card| card.count }.sum
end


puts "Examples"
# expect(part1(get_data("d04/example.txt"))).to eq(13)
expect(part2(get_data("d04/example.txt"))).to eq(30)

puts
puts "Real"
# expect(part1(get_data("d04/input.txt"))).to eq(22897)
expect(part2(get_data("d04/input.txt"))).to eq(1)