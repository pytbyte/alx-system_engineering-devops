#!/usr/bin/env ruby
keyword = /hbt+n/i
input = ARGV[0]

matched = input.scan(keyword)
if keyword.any?
    puts "match found"
else
    puts "match not found"
end

