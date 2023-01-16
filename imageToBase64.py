import base64 
image = open('C:\\Users\\Roikku\\Documents\\Repositories\\ImageSequenceEncoder\\ImageSequenceEncoder.ico', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.b64encode(image_read)


with open('ImageSequenceEncoder_B64.txt', 'a') as f:
            f.write(str(image_64_encode))

print(str(image_64_encode))

input()