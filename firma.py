# firma digital usando RSA

import Crypto.Random
import Crypto.Util.number
import hashlib

# Para e vamos a usar el numero 4 fermat
e = 65537

#Calculamos las llaves publicas de Alice y Bob(bob no las usa, la entidad que firma si las usaria)
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print('\n RSA numero de Alice: ', nA)

pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nB = pB * qB
#print('\n RSA numero de Bob: ', nA)

#Calculamos las llaves privadas de Alice y Bob(bob no las usa, la entidad que firma si las usaria)
phiA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiA)

print('\n RSA Llave privada de Alice: ', dA)

phiB = (pB - 1) * (qB - 1)

dB = Crypto.Util.number.inverse(e, phiB)

#print('\n RSA Llave privada de Bob: ', dB)

#firmamos el mensaje
mensaje = "Ya me quiero irrrrr"

print('\n mensaje: ', mensaje)

#generamos el hash del mensaje
hM = int.from_bytes(hashlib.sha256(mensaje.encode('utf-8')).digest(), byteorder='big')
print('\n Mensaje hasheado: ', hex(hM))

#firmamos el Hash usando la llave privada de Alice y se lo enviamos a Bob
sA = pow(hM, dA, nA)
print('\n Firma Alice: ', sA)

#Bob verifica la firma de Alice usando la llave publica de Alice
hM1 = pow(sA, e, nA)
print('\n Mensaje hasheado verificando: ', hex(hM1))

print('\n Firma Valida: ', hM == hM1, '\n')