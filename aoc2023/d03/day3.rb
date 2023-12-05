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
    matrix = Matrix[*input.map { |line| line.chars }]
    p1_answer = 0
    matrix.row_count.times do |row|
        number = ""
        surroundings = []
        matrix.column_count.times do |col|
            cell_value = matrix[row, col]
            if numeric?(cell_value)
                number = "#{number}#{cell_value}"
                puts "Value at (#{row}, #{col}): #{cell_value}"
                surroundings += get_surrounding_chars(matrix, row, col, 1)
            else
                if number != ""
                    ap surroundings, multiline: false
                    if surroundings.to_a.flatten.any? { |element| element.match(/[^.\d]/) }
                        p1_answer += number.to_i
                        puts "#{number} INCLUDE ADDED TO ANSWSER #{p1_answer}"
                    else
                        puts "#{number} not included"
                    end
                    surroundings = []
                    number = ""
                end
            end
        end 
        # End of line processor
        if number != ""
            ap surroundings, multiline: false
            if surroundings.to_a.flatten.any? { |element| element.match(/[^.\d]/) }
                p1_answer += number.to_i
                puts "#{number} INCLUDE ADDED TO ANSWSER #{p1_answer}"
            else
                puts "#{number} not included"
            end
            surroundings = []
            number = ""
        end
    end
    return p1_answer
end

def part2(input)
    # oof, tried, deleted, looked at others' better approach with psuedomatrix (see day3-unoriginal.rb)
end


puts "Examples"
expect(part1(get_data("d03/example.txt"))).to eq(4361)
expect(part2(get_data("d03/example.txt"))).to eq(1)

# puts
puts "Real"
# expect(part1(read_file_to_matrix(real))).to eq(1)
# expect(part2(get_data(real))).to eq()