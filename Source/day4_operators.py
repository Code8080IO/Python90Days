"""
@author : code8080.in

Let's create a program that demonstrates the various operations on strings
"""

def main():
    # Strings in Python
    print("Demonstrating String Creation:")
    print('spam eggs')  # single quotes
    print("doesn't")    # double quotes
    print('"Yes," they said.')  # double quotes can enclose single quotes without escape
    print()

    # Special Characters in Strings
    print("Demonstrating Special Characters in Strings:")
    print('First line.\nSecond line.')  # prints in two lines
    print(r'First line.\nSecond line.') # using raw strings to ignore escape sequences
    print()

    # String Concatenation and Repetition
    print("Demonstrating String Concatenation and Repetition:")
    print(3 * 'un' + 'ium')  # prints 'unununium'
    print()

    # String Indexing
    print("Demonstrating String Indexing:")
    word = "Python"
    print(word[0])  # character in position 0
    print(word[-1]) # last character
    print()

    # String Slicing
    print("Demonstrating String Slicing:")
    print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
    print(word[:2])   # character from the beginning to position 2 (excluded)
    print()

    # Strings are Immutable
    print("Demonstrating Strings are Immutable:")
    new_word = 'J' + word[1:]
    print(new_word)
    print()

    # String Length
    print("Demonstrating String Length:")
    s = 'supercalifragilisticexpialidocious'
    print(len(s))
    print()

if __name__ == "__main__":
    main()
