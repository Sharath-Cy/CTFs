from pwn import xor
string = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# as we already know the flag format i.e crypto{}
flag = xor(string[:7], 'crypto{') + xor(string[-1], '}')
print(flag)
print(xor(string, flag))