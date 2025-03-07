import lxml.etree as ET

# Cargar el XML del CFDI
xml_tree = ET.parse("cfdi.xml")

# Cargar la hoja XSLT oficial del SAT
xslt_tree = ET.parse("cadenaoriginal_4_0.xslt")
transform = ET.XSLT(xslt_tree)

# Aplicar la transformación XSLT al CFDI
cadena_original = str(transform(xml_tree))

print("✅ Cadena Original Generada:")
print(cadena_original)