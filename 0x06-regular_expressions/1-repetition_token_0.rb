#!/usr/bin/env ruby
keyword = /hb.n/
input = ARGV[0]

if keyword.match(input)
    puts "match found"
else
    puts "match not found"
end

