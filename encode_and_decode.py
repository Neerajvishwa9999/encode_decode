alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(plain_text,shift_amount,direction_code):
  
  if direction == "encode":
    empty_text=""
    for letter in plain_text:
      position =alphabet.index(letter)
      new_position = position + shift_amount
      empty_text += alphabet[new_position]
    print(f"The encoded text is {empty_text}")

  elif direction == "decode":
    empty_text =""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      empty_text += alphabet[new_position]
    print(f"The decoded text is {empty_text}")  

ceaser(plain_text = text,shift_amount = shift,direction_code =direction)
    
  
  
  
  


