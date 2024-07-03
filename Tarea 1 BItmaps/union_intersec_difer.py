from PIL import Image, ImageChops

# Abrir dos imágenes
image1 = Image.open('bitmap_example.png').convert('1')  # Convertir a blanco y negro
image2 = Image.open('bitmap_example.png').convert('1')  # Convertir a blanco y negro

# Operación Unión (OR)
def image_union(img1, img2):
    # Utilizar ImageChops para la unión (A or B)
    return ImageChops.logical_or(img1, img2)

result_union = image_union(image1, image2)
result_union.show()

# Operación Intersección (AND)
def image_intersection(img1, img2):
    # Utilizar ImageChops para la intersección (A and B)
    return ImageChops.logical_and(img1, img2)

result_intersection = image_intersection(image1, image2)
result_intersection.show()

# Operación Diferencia (XOR)
def image_difference(img1, img2):
    # Utilizar ImageChops para la diferencia (A xor B)
    return ImageChops.difference(img1, img2)

result_difference = image_difference(image1, image2)
result_difference.show()
