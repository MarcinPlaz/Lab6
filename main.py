def encode(password):  # Encoding function, iterates through each character and adds 3
    encoded = ""
    for x in str(password):
        encoded += str((int(x) + 3) % 10)  # add space
    return encoded


def decode(encoded):
    decoded = ""
    # insert decode function here
    for character in encoded:
        decoded_character = (int(character) - 3)
        if decoded_character < 0:
            decoded_character += 10  # add 10 if value less than 0
        decoded += str(decoded_character)
    return decoded


def main():
    while 0 == 0:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        menu_select = int(input("Please enter an option: "))
        if menu_select == 1:
            password = input("PLease enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")

        elif menu_select == 2:
            print(f"The encoded password is {encoded}, and the original is {decode(encoded)}")

        else:
            break


if __name__ == '__main__':
    main()
