# Ricky Hou
def encode(orig_pass):
    result = ''
    for numbers in orig_pass:
        new_numbers = str((int(numbers) + 3) % 10)
        result += new_numbers
    return result

def decode(password):
    result = ''

    for numbers in password:
        new_numbers = str((int(numbers) - 3) % 10)
        result += new_numbers
    return result

def main():
    testing = True
    while testing:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option:"))
        if option == 1:
            orig_pass = input("Please enter your password to encode:")
            orig_pass = encode(orig_pass)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            print(f"The encoded password is {orig_pass}, and the original password is .")

        else:
            testing = False


if __name__ == "__main__":
    main()
