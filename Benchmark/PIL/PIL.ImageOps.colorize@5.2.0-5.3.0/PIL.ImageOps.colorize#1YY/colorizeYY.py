from PIL import ImageOps, Image
image = Image.new('L', (100, 100), color='white')
black_color = '#000000'
white_color = '#FFFFFF'
result_image = ImageOps.colorize(image,  black_color,  white_color)
