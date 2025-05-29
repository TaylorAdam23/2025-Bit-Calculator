# ask user for width and loop until they enter a number that is more than zero

def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # Ask the user for number
            response = int(input(question))

            # Check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes here
for item in range(0, 2):
    integer = int_check("Integer: ", 0)
    print(integer)

print()

for item in range(0, 2):
    width = int_check("width: ", 1)
    print(width)

print()

for item in range(0, 2):
    height = int_check("height: ", 1)
    print(height)

print()