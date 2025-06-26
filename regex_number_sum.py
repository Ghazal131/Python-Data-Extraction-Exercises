# This Python program reads a text file, uses a regular expression to extract all sequences of digits,
# converts them to integers, and calculates the total sum of those numbers.

# Import the regex library
import re

# Open the file
file_handle = open('regex_sum_2231604.txt')

# Read the entire content of the file
content = file_handle.read()

# Use regular expression to find all numbers
numbers = re.findall('[0-9]+', content)   # '[0-9]+' means: one or more digits

# Convert the numbers from strings to integers using list comprehension
int_numbers = [int(num) for num in numbers]

# Calculate the sum of the numbers
total_sum = sum(int_numbers)

# Print the sum
print(total_sum)   # 429665
