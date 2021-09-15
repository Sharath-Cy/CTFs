connect to nc socket.cryptohack.org 13389 via terminal

in the next line pass:
{"document":"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"}
again when server says the documnet added

in the next line pass:
{"document":"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"}

there you go the flag 
{"error": "Document system crash, leaking flag: crypto{m0re_th4n_ju5t_p1g30nh0le_pr1nc1ple}"}

when strings of same hash value tries to add to the system, it crashes and leaks the flag

so i got this string values in hex form @https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value/15889#15889
