from PIL import ImageFont
font = ImageFont.load_default()
text = 'Hello, Pillow!'
mask = font.getmask(text,  '1',  None, features=None, language=None)
