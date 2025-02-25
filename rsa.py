import Crypto.Util.number
import random
import hashlib

e = 65537

# Primer primo de Alice
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
# Segundo primo de Alice
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

print(f'\nNúmeros primos de Alice: {pA} \n y {qA}')

# Cálculo de llave pública de Alice (nA)
nA = pA * qA
print(f'\nLlave pública de Alice: {nA}')

# Cálculo de phi de Alice
phiA = (pA - 1) * (qA - 1)
print(f'\nPhi de Alice: {phiA}')

# Cálculo de la llave privada
dA = Crypto.Util.number.inverse(e, phiA)
print(f'\nLlave privada de Alice: {dA}')

lyrics = """Yo soy tu gominola
Yo soy tu gominola
Osito gomi gomi gomi
Gomi gominola
Yo soy tu gominola
Yo soy tu gominola
Osito gomi gomi
Dulce gomi gomi
Gomi gominola oeo
Gomi gomi gomi
Gomi gominola
Gomi gomi gomi
Gomi gominola
Baile, and gomi fiesta
Baile, and gomi fiesta
Breding and gomi fiesta
Fiesta pop
Baile, and gomi fiesta
Baile, and gomi fiesta
Breding and gomi fiesta
Fiesta pop
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Gomi gomi gomi
Gomi gominola
Baile, and gomi fiesta
Baile, and gomi fiesta
Breding and gomi fiesta
Fiesta pop
Baile, and gomi fiesta
Baile, and gomi fiesta
Breding and gomi fiesta
Fiesta pop
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Tres besitos dulces
Los amos del can-can
No tenemos pelo
Y cantamos un refrán
Pa pa virovirovirulo
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Pa pa virovirovirulo
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Gomi gomi gomi
Gomi gominola
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Pa pa virovirovirulo
Pa pa virovirovirulo
Tres besitos dulces
Fiesta pop
Fiesta pop
Fiesta pop
Fiesta pop"""

#hash del mensaje
h1 = int.from_bytes(hashlib.sha256(lyrics.encode('utf-8')).digest(), byteorder='big')
print('\n Mensaje hasheado: ', hex(h1))

# Dividir el mensaje en fragmentos de 128 caracteres
mensaje = [lyrics[i:i+128] for i in range(0, len(lyrics), 128)]

# Bob cifra el mensaje con la clave pública de Alice
mensajes_cifrados = [pow(int.from_bytes(frag.encode('utf-8'), byteorder='big'), e, nA) for frag in mensaje]

# Mostrar los fragmentos cifrados
for i, cifrado in enumerate(mensajes_cifrados):
    print(f'\nFragmento {i+1} cifrado: {cifrado}')

# Alice descifra el mensaje con su llave privada
mensajes_descifrados = [pow(c, dA, nA) for c in mensajes_cifrados]

# Convertir los fragmentos descifrados de enteros a texto
fragmentos_descifrados = [int.to_bytes(d, length=(d.bit_length() + 7) // 8, byteorder='big').decode('utf-8', errors='ignore') for d in mensajes_descifrados]

# Mostrar los fragmentos descifrados
print("\nMaravilloso super cool mensaje descifrado:")
for i, frag in enumerate(fragmentos_descifrados):
    mensajeCool = frag
    print(f'\n{mensajeCool}')

#hash del mensaje
h2 = int.from_bytes(hashlib.sha256(lyrics.encode('utf-8')).digest(), byteorder='big')
print('\n Mensaje hasheado: ', hex(h2))

# Verificar si los hashes coinciden
verificacion = (h1 == h2)
print('\n¿Los mensajes son iguales después de descifrar? ', verificacion)