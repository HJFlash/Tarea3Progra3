from PIL import Image

# Abrir una imagen existente
Ruta_Img = 'Imagen2.png'
Img = Image.open(Ruta_Img)

# Convertir la imagen a escala de grises
Img_Gris = Img.convert('L')

# Guardar la imagen en escala de grises
Img_Gris.save('Ej2.png')

# Mostrar la imagen
Img_Gris.show()
