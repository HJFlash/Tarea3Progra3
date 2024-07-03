from PIL import Image, ImageDraw, ImageFont

# Crear un nuevo bitmap en blanco
width, height = 300, 200
image = Image.new('RGB', (width, height), color='white')

# Crear un objeto ImageDraw para dibujar en el bitmap
draw = ImageDraw.Draw(image)

# Dibujar un rectángulo rojo
draw.rectangle([50, 50, 250, 150], fill='teal', outline='black')

# Dibujar un texto en el bitmap
font = ImageFont.truetype('arial.ttf', size=40)
draw.text((80, 80), "Holaaa", fill='black', font=font)

# Guardar el bitmap
image.save('bitmap_example.png')

# Mostrar el bitmap (opcional)
image.show()
