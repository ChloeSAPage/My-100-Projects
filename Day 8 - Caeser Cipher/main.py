alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '?', '.', ',', ';', ':', "'", '"', '`',
    '+', '-', '*', '/', '%', '=',
    '(', ')', '{', '}', '[', ']', '<', '>',
    '@', '#', '$', '&', '|', '_', '~',
    '$', '€', '¥', '£', '₹', '1','2','3','4','5','6','7','8','9','0']

# Combined
def ceaser(text, shift, direction):
    word =""
    for letter in text:
      if letter not in special_characters:
        place = alphabet.index(letter)
        if direction=="encode":
            newplace = place + shift
            word += alphabet[newplace]
        elif direction=="decode":
            newplace = place - shift
            word += alphabet[newplace]
      else:
         word += letter
    return f"Your encrypted word is {word}"

while True:
   direction = input("Do you wish to encode or decode \n")
   text = input("Choose a word \n").lower()
   shift = int(input("Choose a number \n")) % 26


print(ceaser(text, shift, direction))