import string
from itertools import cycle


def solution_6_1():
    """
    Prompts the user for a strictly positive integer n and prints a character triangle of height n.
    This version constructs each line by explicitly adding spaces on the left (using string
    multiplication).

    Example:
        Input: 4
        Output:
               A
              BCB
             DEFED
            GHIJIHG
    """
    n = int(input("Enter a strictly positive integer: "))

    letters = string.ascii_uppercase  # Alphabet A–Z
    iterator = cycle(letters)  # Cycle through alphabet indefinitely
    lines = []

    for i in range(1, n + 1):
        # Build ascending part of row
        line = ""
        for letter in range(i):
            line += next(iterator)
        # [:-1] removes the last letter — because slice stops before the end index.
        # [::-1] reverses the sequence — because a negative step means go backward.
        # Together they make a mirrored pattern, like “ABC” → “ABCBA”.
        line += line[:-1][::-1]
        # Prepend spaces for triangle alignment
        line = " " * (n - i) + line
        lines.append(line)

    for line in lines:
        print(line)


def solution_6_2():
    """
    Prompts the user for a strictly positive integer n and prints a character triangle of height n.
    This version uses str.center() to automatically align the triangle to the center.
    """
    n = int(input("Enter a strictly positive integer: "))

    letters = string.ascii_uppercase
    iterator = cycle(letters)
    lines = []
    spaces = n * 2 - 1                      # total width of the last line

    for i in range(1, n + 1):
        # Build row
        # "".join() accepts any iterable, so we can use a generator expression
        # without creating an intermediate list
        line = "".join(next(iterator) for _ in range(i))
        line = line + line[:-1][::-1]
        # Center the string with spaces
        lines.append(line.center(spaces))
        # Or you can use format with ^ to center text
        # lines.append(format(line, f"^{spaces}"))

    for line in lines:
        print(line.rstrip())


def solution_6_hint_ord():
    """
    #############################################
    ###              EXTRA QUESTION            ###
    #############################################

    ❓ Problem 1:
        By default the triangle starts from 'A'.
        But what if it should start from ANY given
        uppercase letter (e.g., 'K', 'Z')?

    ❓ Problem 2:
    What if instead of letters, the triangle
    should be printed with DIGITS (0–9)?
    e.g., rows using 12321, 4567654, etc.

    💡 Think about:
        - Use ord() to convert characters to numbers.
        - gap = ord(starting_from) - ord('A').
        - Generate letters with:
              chr(ord('A') + (gap + step) % 26)
        - This way, after 'Z' it wraps back to 'A'.

    #############################################
    ###           END OF EXTRA HINT            ###
    #############################################
    """
    pass