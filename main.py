in_str: str = input("Enter a string: ")

print(f"You entered: {in_str}")
print(f"Length of the string: {len(in_str)}")

def encode(s: str) -> str:
    v = int(s.encode('ascii').hex(), 16)
    enc: str = ''
    while v > 0:
        v, r = divmod(v, 1114111)
        enc = chr(r) + enc
    return enc

def decode(s: str) -> str:
    v: int = 0
    for c in s:
        v = v * 1114111 + ord(c)
    r = str(hex(v))[2:]
    return str(bytes.fromhex('0' * (len(r) % 2) + r).decode('ascii'))

print(f"Encoded string: {encode(in_str)}")
print(f"Length of encoded string: {len(encode(in_str))}")

print(f"Decoded string: {decode(encode(in_str))}")
print(f"Length of decoded string: {len(decode(encode(in_str)))}")