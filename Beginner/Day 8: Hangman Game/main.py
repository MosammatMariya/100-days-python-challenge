import logo
print(logo.logo)
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser (original_text, shift_amount,encode_or_decode):
    final_text = ""
    if encode_or_decode == 'decode':
             shift_amount *= -1
    for letter  in original_text:
        
        if letter not in alphabet:
            final_text += letter

        else:
           position = alphabet.index(letter) + shift
           position %= len(alphabet)
           final_text += alphabet[position]
    print(f"Here is the {encode_or_decode}d text: ", final_text)

continue_work = True

while continue_work:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: "))

    ceaser(original_text=text,
        shift_amount=shift,
        encode_or_decode=direction)

    restart=input("if you want to continue type 'yes', if you don't type 'no'\n").lower()
    if restart == 'no':
        continue_work = False
        print("Thank you for playing! Goodbye!")
