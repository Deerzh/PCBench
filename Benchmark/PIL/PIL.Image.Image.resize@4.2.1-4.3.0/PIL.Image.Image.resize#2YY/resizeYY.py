from PIL import Image
image = Image.open('/home/zhang/example.jpg')
resized_image = image.resize(size=(300, 200))
resized_image.save('resized_example.jpg')
