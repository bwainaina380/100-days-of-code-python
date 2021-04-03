encode_or_decrypt = input("Type 'encode' to encrypt, type 'decrypt' to decrypt:\n").lower()
message = input(f"Enter the message to {encode_or_decrypt}:\n")
shift_by = int(input("Enter the shift number:\n"))

def encode(text, shift_number):
    encoded_text = ''
    for character in text:
        encoded_text += chr(ord(character) + shift_number)
    return encoded_text

def decode(text, shift_number):
    decoded_text = ''
    for character in text:
        decoded_text += chr(ord(character) - shift_number)
    return decoded_text

if encode_or_decrypt == "encode":
    print(encode(message, shift_by))

else:
    print(decode(message, shift_by))
