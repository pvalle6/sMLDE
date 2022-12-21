# EARLY SCRIPT USED TO GET ALIGNMENT OF GB1
# MARK FOR DELETE
# NOT USED


import sys
import re

remove_lower = lambda text: re.sub('[a-z]', '', text)

input_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\GB1_alignment.a2m"
new_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\GB1_alignment___.a2m"

with open(input_file) as file:
    lines = file.readlines()
    lines = [remove_lower(line.rstrip()).replace(".", "") for line in lines]


with open(new_file, 'w') as f:
	sys.stdout = f
	for item in lines:
		print(item)