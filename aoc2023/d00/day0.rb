require "csv"
require "daru"
require "pp"
require "awesome_print"
require "polars-df"

puts "Hello - testing ruby basics before Dec 1st"

input = CSV.read("day0.txt")
puts "pretty print std obj"
PP.pp(input)
puts "awesome print std obj"
ap input

ddf = Daru::DataFrame.from_csv('day0.txt')
puts "pretty print daru obj"
PP.pp(ddf)
puts "awesome print daru obj"
ap ddf

pdf = Polars.read_csv("day0.txt")
puts "pretty print polars obj"
PP.pp(pdf)
puts "awesome print polars obj"
ap(pdf)
