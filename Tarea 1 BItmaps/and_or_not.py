from PIL import Image, ImageChops

# Abrir dos imágenes
image1 = Image.open('bitmap_example.png').convert('1')  # Convertir a blanco y negro
image2 = Image.open('bitmap_example2.png').convert('1')  # Convertir a blanco y negro

# Operación AND
result_and = ImageChops.logical_and(image1, image2)
result_and.show()

# Operación OR
result_or = ImageChops.logical_or(image1, image2)
result_or.show()

# Operación NOT
result_not = ImageChops.invert(image1)
result_not.show()
