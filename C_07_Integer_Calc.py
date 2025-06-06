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


# Get image dimensions and calculate number of pixels and multiply them by 24

def integer_calc():

    integer = int_check("integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)

    # set up to return
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

# main
integer_ans = integer_calc()
print(integer_ans)
