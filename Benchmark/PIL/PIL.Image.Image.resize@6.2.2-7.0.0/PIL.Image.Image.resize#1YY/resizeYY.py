from PIL import Image
image = Image.open('/home/zhang/example.jpg')
resized_image_resample = image.resize((100, 100))
