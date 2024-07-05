from PIL import Image, ImageDraw, ImageFont

# Crear un nuevo bitmap en blanco
Ancho, Alto = 300, 200
Img = Image.new('RGB', (Ancho, Alto), color='white')

# Crear un objeto ImageDraw para dibujar en el bitmap
Dibujar = ImageDraw.Draw(Img)

# Dibujar un rectangulo rojo
Dibujar.rectangle([50, 50, 250, 150], fill='teal', outline='black')

# Dibujar un texto en el bitmap
Fuente = ImageFont.truetype('arial.ttf', size=40)
Dibujar.text((80, 80), "Holaaa :)", fill='black', font=Fuente)

# Guardar el bitmap
Img.save('EjemploOp.png')

# Mostrar el bitmap (opcional)
Img.show()
