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

def image_calc():
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    # calculate the number of pixels and multiply by 24 to get number of bits
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits {num_pixels} x 24 = {num_bits}")
    return answer


# main thing

image_ans = image_calc()
print(image_ans)
