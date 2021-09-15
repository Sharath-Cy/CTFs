from Crypto.Util.number import long_to_bytes

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

string_value = long_to_bytes(integer)
print("Integer to Message Conversion flag :")
print(string_value)
