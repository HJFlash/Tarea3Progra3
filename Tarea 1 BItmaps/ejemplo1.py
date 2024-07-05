from PIL import Image

# Crear una nueva imagen en blanco y negro
Ancho, Alto = 300, 200
Img = Image.new('1', (Ancho, Alto), color='white')

# Convertir la imagen en un objeto de pixeles editable
pixels = Img.load()

# Cambiar algunos pixeles a negro (0)
pixels[100, 50] = 0  # Cambiar el pixel en la posicion (100, 50) a negro
pixels[150, 100] = 0  # Cambiar el pixel en la posicion (150, 100) a negro

# Guardar la imagen modificada
Img.save('Ej1.png')

# Mostrar la imagen (opcional)
Img.show()
