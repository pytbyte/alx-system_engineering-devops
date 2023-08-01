#!/usr/bin/env ruby
keyword = /hbt*n/
input = ARGV[0]

if keyword.match(input)
    puts "match found"
else
    puts "match not found"
end

