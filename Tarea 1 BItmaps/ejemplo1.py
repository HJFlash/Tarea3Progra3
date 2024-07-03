from PIL import Image

# Crear una nueva imagen en blanco y negro
width, height = 300, 200
image = Image.new('1', (width, height), color='white')

# Convertir la imagen en un objeto de píxeles editable
pixels = image.load()

# Cambiar algunos píxeles a negro (0)
pixels[100, 50] = 0  # Cambiar el píxel en la posición (100, 50) a negro
pixels[150, 100] = 0  # Cambiar el píxel en la posición (150, 100) a negro

# Guardar la imagen modificada
image.save('ejemplo1.png')

# Mostrar la imagen (opcional)
image.show()
