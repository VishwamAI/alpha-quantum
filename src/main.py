"""
Alpha Quantum Language Comprehension - Main Script

This script processes input from the user and reverses the characters in each word.
"""

import re

def reverse_characters(text):
    def reverse_word(word, is_first_word):
        # Separate word into parts: leading punctuation, main word, trailing punctuation
        match = re.match(r'^(\W*)([\w-]+)(\W*)$', word)
        if match:
            leading_punct, main_word, trailing_punct = match.groups()
            # Reverse the main word while preserving capitalization
            reversed_main = main_word[::-1]
            if is_first_word and main_word[0].isupper():
                reversed_main = reversed_main.capitalize()
            elif not is_first_word:
                reversed_main = reversed_main.lower()
            return leading_punct + reversed_main + trailing_punct
        return word  # Return the original word if it doesn't match the pattern

    # Split the text into words, reverse each word, and join them back
    words = text.split()
    reversed_words = [reverse_word(word, i == 0) for i, word in enumerate(words)]
    return ' '.join(reversed_words)

def main():
    print("Welcome to the Alpha Quantum Language Comprehension software.")
    print("This program will reverse the characters in each word of your input.")
    while True:
        user_input = input("Enter a sentence to process (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using Alpha Quantum Language Comprehension. Goodbye!")
            break
        result = reverse_characters(user_input)
        print(f"Processed result: {result}")

if __name__ == "__main__":
    main()
