encoded_key = input()
key = sum(int(input()).to_bytes(2, "little"))

print("".join(chr(ord(s) + key) for s in encoded_key))
