from PIL import Image

# Abrir una imagen existente
image_path = 'bitmap_example2.png'
image = Image.open(image_path)

# Convertir la imagen a escala de grises
gray_image = image.convert('L')

# Guardar la imagen en escala de grises
gray_image.save('ejemplo2.png')

# Mostrar la imagen original y la imagen en escala de grises (opcional)
#image.show()
gray_image.show()
