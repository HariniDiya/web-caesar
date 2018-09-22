from helpers import alphabet_position, rotate_character

# function
def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char.isalpha():
            encrypted = encrypted + rotate_character(char,rot)
        else:
            encrypted = encrypted + char
    return encrypted

def main():
     msg1 = input("Type a message: ")
     rotate_value = input("Rotate by: ")
     print(encrypt(msg1 , rotate_value ))

if __name__ == "__main__":
    main()