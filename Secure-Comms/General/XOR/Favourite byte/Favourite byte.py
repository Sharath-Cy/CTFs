data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

decoded_hex = bytes.fromhex(data)

print("Hex value of Data is {}".format(decoded_hex))

print(''.join(chr(c ^ (decoded_hex[0]^ord('c'))) for c in decoded_hex))

