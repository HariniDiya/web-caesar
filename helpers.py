# helper function 1
def alphabet_position(letter):
    letter = letter.lower()
    letter_val=ord(letter) - 97 
    return letter_val

# helper function 2
def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        rotate = alphabet_position(char)
        rotate = (rotate + int(rot)) % 26
        rotate = (alphabet[rotate])
        if char.isupper():
            rotate = rotate.title()
        return rotate
    else:
        return char