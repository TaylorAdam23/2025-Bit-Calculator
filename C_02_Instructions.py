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
want_instructions = input("Press enter for instructions, or any key to continue"
                          "or any key to continue")

if want_instructions == "":
    instructions()

print("\nProgram continues")
