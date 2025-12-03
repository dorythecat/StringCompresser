in_str: str = input("Enter a string: ")

print(f"You entered: {in_str}")
print(f"Length of the string: {len(in_str)}")

def encode(s: str) -> str:
    v = int(s.encode('utf-8').hex(), 16)
    enc = ''
    while v > 0:
        v, r = divmod(v, 65536)
        enc = chr(r) + enc
    return enc

def decode(s: str) -> str:
    v = 0
    for c in s:
        v = v * 65536 + ord(c)
    r = str(hex(v))[2:]
    return bytes.fromhex('0' * (len(r) % 2) + r).decode('utf-8')

print(f"Encoded string: {encode(in_str)}")
print(f"Length of encoded string: {len(encode(in_str))}")

print(f"Decoded string: {decode(encode(in_str))}")
print(f"Length of decoded string: {len(decode(encode(in_str)))}")