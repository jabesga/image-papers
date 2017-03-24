from scipy import misc, ndimage
face = misc.imread('image.jpg', flatten=True)
misc.imsave('face_gray.png', face)

face_height, face_width = face.shape
gray = 150


for h in range(face_height):
    for w in range(face_width):
        if face[h][w] > 125:
            face[h][w] = 255
        elif face[h][w] < 140:
            face[h][w] = 0


misc.imsave('face{}.png'.format(gray), blurred_face)