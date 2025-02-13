#Practica del Algoritmo Deffie Helman

import hashlib
import random

p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

print("\n ", "*****************************")
print("\n", "Variables Publicas Compartidas")
print("\n", "Numero primo compartido publicamente RFC 3625 ", p )
print("\n", "Numero base compartido publicamente ", g)

sAlice = random.getrandbits(256)
sBob = random.getrandbits(256)
sEve = random.getrandbits(256)

print("\n", "Numero Alice ", sAlice )
print("\n", "Numero Bob ", sBob)
print("\n", "Numero Eve ", sEve)

# Alice manda mensaje a Bob pero Eve lo intercepta
# A = g^a mod p
A = pow(g, sAlice, p)
print("\n", "Mensaje Alice ", A )

# Bob manda mensaje a Alice pero Eve lo intercepta
# B = g^b mod p
B = pow(g, sBob, p)
print("\n", "Mensaje Bob ", B )

#Eve crea sus propias llaves y se las manda a Alice y a Bob
EveA = pow(g, sEve, p) # Valor falso enviado a Bob en lugar de A
EveB = pow(g, sEve, p) # Valor falso enviado a Alice en lugar de B

# Alice calcula la llave incorrecta 
# s1 = B^a mod p
s1 = pow(EveB, sAlice, p)
print("\n", "Llave secreta compartida infiltrada", s1 )

# Bob calcula la llave incorrecta 
# s2 = A^a mod p
s2 = pow(EveA, sBob, p)
print("\n", "Llave secreta compartida infiltrada", s2 )

#Eve calcula las llaves que robadas
s3 = pow(A, sBob, p)
print("\n", "Llave secreta robada ", s3 )

s4 = pow(B, sAlice, p)
print("\n", "Llave secreta robada ", s4 )

# Comparamos llaves secretas
h1 = hashlib.sha512(int.to_bytes(s1, length=1024, byteorder="big")).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s2, length=1024, byteorder="big")).hexdigest()

if (h1 == h2):
    print ("\n Todo cool")
else:
    print("\n Oh no, han sido atacados por alguien malevolo que cambio las llaves")

# Eve Compara llaves secretas robadas
h3 = hashlib.sha512(int.to_bytes(s3, length=1024, byteorder="big")).hexdigest()
h4 = hashlib.sha512(int.to_bytes(s4, length=1024, byteorder="big")).hexdigest()

if (h3 == h4):
    print ("\n Eve es una gran hacker y pudo decifrar el mensaje de Alice y Bob\n")
else:
    print("\n Oh no, Eve es una mala hacker y no le salio la jugada\n")