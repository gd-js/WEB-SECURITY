#!/usr/bin/env python3

# problem: convert ascii int to string
# solution: use join map, chr to convert to string

input = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73,
         73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

text = ''.join(map(chr, input))

print(text)
