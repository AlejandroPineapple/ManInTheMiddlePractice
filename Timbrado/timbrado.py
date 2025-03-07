import base64
import lxml.etree as ET
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# Ruta a los archivos CSD
CERT_PATH = "CSD_Sucursal_1_XOJI740919U48_20230118_134855.cer"
KEY_PATH = "CSD_Sucursal_1_XOJI740919U48_20230118_134855.key"
XML_PATH = "cfdi.xml"  # Tu archivo XML

# 1. Leer y extraer la clave privada
def load_private_key():
    with open(KEY_PATH, "rb") as key_file:
        private_key = serialization.load_der_private_key(
            key_file.read(), password="12345678a".encode(), backend=None
        )
    return private_key

# 2. Obtener número de serie del certificado
def get_cert_serial_number():
    with open(CERT_PATH, "rb") as cert_file:
        cert_data = cert_file.read()
        cert = serialization.load_der_x509_certificate(cert_data, backend=default_backend())
    return format(cert.serial_number, 'X')

# 3. Cargar y firmar el XML
def sign_cfdi():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    # Extraer la cadena original (simplificado)
    cadena_original = "||4.0|A|12345|2024-03-05T12:00:00|01||Contado|1000.00|MXN|1160.00|I||PUE|64000|AAA010101AAA|EMPRESA EMISORA S.A. DE C.V.|601|BBB020202BBB|CLIENTE EJEMPLO|||G03|01010101|1|H87|Producto de prueba|1000.00|1000.00||1000.00|002|Tasa|0.160000|160.00|1000.00|002|Tasa|0.160000|160.00|160.00||"  # cadena original creada con el archivo cadena.py

    # Firmar la cadena original
    private_key = load_private_key()
    signature = private_key.sign(
        cadena_original.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    sello = base64.b64encode(signature).decode()

    # Insertar el sello en el XML
    root.set("Sello", sello)

    # Guardar el XML firmado
    tree.write("cfdi_firmado.xml", encoding="UTF-8", xml_declaration=True)
    print("XML firmado correctamente y guardado como 'cfdi_firmado.xml'.")

# Ejecutar la firma
sign_cfdi()
print("cfdi firmado yupi yupi")