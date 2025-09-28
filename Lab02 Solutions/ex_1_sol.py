"""
Continuously prompts the user for a floating-point number between -1 and 1 (excluded).
- Must be something that float() accepts but int() would not (so it should contain a '.').
- Keeps asking until the input is valid.
- Finally prints the number rounded to 2 decimal places (with tolerance ±0.005).
"""
#Loop until valid input is received
while True:
    try:
        # Prompt user for input
        x = input('Enter a floating point number between -1 and 1 excluded: ')

        # Check: must contain a decimal point
        if '.' not in x:
            raise ValueError

        # Convert to float
        x = float(x)

        # Check: must be strictly between -1 and 1
        if not (-1 < x < 1):
            raise ValueError

        # Valid input, stop loop
        break
    except ValueError:
        # If any check fails, ask again
        print('You got that wrong, try again!\n')

# Format the result to 2 decimal places
print(f'\nUp to +/-0.005, you input {x:.2f}')