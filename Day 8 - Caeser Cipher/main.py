alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Do you wish to encode or decode \n")
text = input("Choose a word \n")
shift= int(input("Choose a number \n"))

# Encrypt
def encode(text, shift):
  encrypt=""
  for letter in text:
        place = alphabet.index(letter)
        newplace = place + shift
        encrypt += alphabet[newplace]
  return f"Your encrypted word is {encrypt}"

#encode(text, shift)

# Decrypt

def decode(text, shift):
  decrypt = ""
  for letter in text:
    place = alphabet.index(letter)
    newplace = place - shift
    decrypt += alphabet[newplace]
  return f"Your decoded word is {decrypt}"

#To decode or not decode
match direction:
    case "encode":
      print(encode(text, shift))
    case "decode":
      print(decode(text, shift))