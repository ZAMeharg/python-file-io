### Code for doing exercise 6 ###

import re

#word_finder is the variable being defined to find the variations of heritable, inherit, inheritance. This can be done using regular expresions
word_finder = re.compile(r'\w*herit\w*', re.IGNORECASE)

print('Now opening origin.txt')
with open('origin.txt', 'r') as in_stream:
	print('Writing origin_output.txt')
	with open('origin_output.txt', 'w') as out_stream:
		for line_num, line in enumerate(in_stream):
			line = line.strip()
			for matches in word_finder.findall(line):
			    out_stream.write(f"{line_num}\t{matches}\n")			
