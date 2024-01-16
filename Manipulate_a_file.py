# Finds the longest word in a file, returns it, replace it, and returns the
# number that a target word occurs in a file

import string

def is_alphanumeric(char):
    return 'a' <= char.lower() <= 'z' or '0' <= char <= '9'

def find_longest_word_in_file(file_path):
    
    # takes a file path as input and
    # returns the longest word found in the file. If there are
    # multiple longest words, return the first one encountered.
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            max_length = 0
            current_word = ''
            longest_word = ''

            for char in content:
                if ('a' <= char.lower() <= 'z' or '0' <= char <= '9'):
                    current_word += char
                elif current_word:
                    if len(current_word) > max_length:
                        max_length = len(current_word)
                        longest_word = current_word
                    current_word = ''

            # Check the last word
            if current_word and len(current_word) > max_length:
                longest_word = current_word

            return longest_word.strip(string.punctuation)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def replace_word_in_file(file_path, target_word, replacement_word):
    
    # replace all occurrences of the target word with the
    # replacement word

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            modified_content = content.replace(target_word, replacement_word)
        with open(file_path, 'w') as file:
            file.write(modified_content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def count_word_occurrences_in_file(file_path, target_word):

    #  count the number of times the target word appears
    # in the file and return the count.
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = 0
            current_word = ''

            for char in content:
                if ('a' <= char.lower() <= 'z' or '0' <= char <= '9'):
                    current_word += char
                elif current_word:
                    if current_word == target_word:
                        count += 1
                    current_word = ''

            # Check the last word
            if current_word == target_word:
                count += 1

            return count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def main():
    input_file = "input.txt"
    
    # Task 1
    longest_word = find_longest_word_in_file(input_file)
    print(f"Longest word in the file: {longest_word}")

    # Task 2
    target_word = "test"
    replacement_word = "exam"
    replace_word_in_file(input_file, target_word, replacement_word)
    print(f'Replaced "{target_word}" with "{replacement_word}" in the file.')

    # Task 3
    word_to_count = "exam"
    word_occurrences = count_word_occurrences_in_file(input_file, word_to_count)
    print(f'Occurrences of "{word_to_count}" in the file: {word_occurrences}')

if __name__ == "__main__":
    main()
