from PIL import Image, ImageChops

# Abrir dos imágenes
Img1 = Image.open('Imagen1.png').convert('1')  # Convertir a blanco y negro
Img2 = Image.open('Imagen2.png').convert('1')  # Convertir a blanco y negro

# Operación Unión (OR)
def OpUnion(img1, img2):
    # Utilizar ImageChops para la unión (A or B)
    return ImageChops.logical_or(img1, img2)

Union = OpUnion(Img1, Img2)
Union.show()

# Operación Intersección (AND)
def OpInterseccion(img1, img2):
    # Utilizar ImageChops para la intersección (A and B)
    return ImageChops.logical_and(img1, img2)

Interseccion = OpInterseccion(Img1, Img2)
Interseccion.show()

# Operación Diferencia (XOR)
def OpDiferencia(img1, img2):
    # Utilizar ImageChops para la diferencia (A xor B)
    return ImageChops.difference(img1, img2)

Diferencia = OpDiferencia(Img1, Img2)
Diferencia.show()
