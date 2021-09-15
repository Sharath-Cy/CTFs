import base64

Hex_String = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte_value = bytearray.fromhex(Hex_String)
base64_value = base64.b64encode(byte_value)
print("Byte to Base64 Conversion flag :")
print(base64_value)
