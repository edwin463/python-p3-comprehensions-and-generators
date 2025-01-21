#!/usr/bin/env python3

# Function to return a list of even elements
def return_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

# Function to add exclamation marks to each sentence
def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]

# Example usage
print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# Output: ["Hello!", "I'm doing great!", "Python is fun!"]
