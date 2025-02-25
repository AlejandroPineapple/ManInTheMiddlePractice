# firma digital usando RSA

import Crypto.Random
import Crypto.Util.number
import hashlib

# Para e vamos a usar el numero 4 fermat
e = 65537

#Calculamos las llaves publicas de Alice y la AC
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print('\n RSA numero de Alice: ', nA)

pAc = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qAc = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nAc = pAc * qAc
print('\n RSA numero de la AC: ', nAc)

#Calculamos las llaves privadas de Alice y la AC
phiA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiA)

print('\n RSA Llave privada de Alice: ', dA)

phiAc = (pAc - 1) * (qAc - 1)

dAc = Crypto.Util.number.inverse(e, phiAc)

print('\n RSA Llave privada de la AC: ', dAc)

#firmamos el mensaje
nda = 'NDA.pdf'

try:
    with open(nda, 'rb') as file:
        file_content = file.read()

    print(f'\nMensaje: {nda}')
except FileNotFoundError:
    print(f'\nError: No se encontró el archivo {nda}')

#generamos el hash del mensaje
hM = int.from_bytes(hashlib.sha256(file_content).digest(), byteorder='big')
print('\n Mensaje hasheado: ', hex(hM))

#firmamos el Hash usando la llave privada de Alice y se lo enviamos a la AC
sA = pow(hM, dA, nA)
print('\n Firma Alice: ', sA)

#La AC verifica la firma de Alice usando la llave publica de Alice
hM1 = pow(sA, e, nA)
print('\n Ac verificando el mensaje hasheado: ', hex(hM1))

if (hM == hM1):
    print ("\n Firma Validada. Mandando a Bob")

else:
    print("Error, ya valio los hashes son diferentes")
    breakpoint

#firmamos el Hash usando la llave privada de AC y se lo enviamos a Bob
sAc = pow(hM, dAc, nAc)
print('\n Firma de la AC: ', sAc)

#Bob verifica la firma de AC usando la llave publica de AC
hM2 = pow(sAc, e, nAc)
print('\n Bob verificando el mensaje: ', hex(hM2))

print("\n Bob recibio correctamente el mensaje firmado por la AC: ", (hM1 == hM2), '\n')