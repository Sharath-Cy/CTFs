There's another issue caused by allowing attackers to specify their own algorithms but not carefully validating them. Attackers can mix and match the algorithms that are used to sign and verify data. When one of these is a symmetric algorithm and one is an asymmetric algorithm, this creates a beautiful vulnerability.

We've made a one-line change to the PyJWT library source code for this challenge to allow the exploit, since the library now blocks it. To create the signature, you may need to patch your JWT library too.

Play at http://web.cryptohack.org/rsa-or-hmac