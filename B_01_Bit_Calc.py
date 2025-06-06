# gen heading(s)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# display instructions
def instructions():
    statement_generator("Instructions", "-")

    print(""""
instructions go here
- instruction 1 
- instruction 2
- You get the point
    """)


# main routine goes here

# Display instructions if needed



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

# Get image dimensions and calculate number of pixels and multiply them by 24


def image_calc():
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    # calculate the number of pixels and multiply by 24 to get number of bits
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits {num_pixels} x 24 = {num_bits}")
    return answer


def calc_text_bits():
    # get text from user
    response = input("Enter some text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits.")
    return answer


# ask user for file type (integer / image / text / xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response
        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"
        # check if it's an image
        elif response in ['image', 'img', 'picture', 'p']:
            return "image"
        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"
        # if the response is invalid
        else:
            print("Enter valid file type, you rat.")


# main routine goes here

want_instructions = input("Press enter for instructions, or any key to continue "
                          "or any key to continue")
if want_instructions == "":
    instructions()

while True:

    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i', ask if they want image or integer
    if file_type == 'i':

        want_image = input("Press <enter> for integer or any key for image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)


