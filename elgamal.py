#Algoritmo Elgamal

import random
import Crypto.Util.number

p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

x = random.getrandbits(256)

# Calculamos y
# y = g^bob mod p
y = pow(g,x,p)
print ("\n Llave privada de Bob: ", x)
print ("\n llave publica de Bob ", p, g, y)

# generar llaves de Alice
k = random.getrandbits(256)

a = pow(g,k,p)
print ("\n Llave privada de Alice: ", k)
print ("\n llave publica de Alice ", p, g, a)

m = 420
print('\n Mensaje Original: ', m)

# Cifrado
b = (pow(y,k,p)*m) % p

print('\n Mensaje cifrado: ', b)

m1 = (b* Crypto.Util.number.inverse(pow(a,x,p),p)) % p

print ('\n Mensaje decifrado: ', m1)