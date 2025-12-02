in_str: str = input("Enter a string: ")

print(f"You entered: {in_str}")
print(f"Length of the string: {len(in_str)}")

def encode(string: str) -> str:
    return string

def decode(string: str) -> str:
    return string

print(f"Encoded string: {encode(in_str)}")
print(f"Length of encoded string: {len(encode(in_str))}")

print(f"Decoded string: {decode(encode(in_str))}")
print(f"Length of decoded string: {len(decode(encode(in_str)))}")