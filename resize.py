import sys
sys.path.append('/Users/chicong/opt/anaconda3/lib/python3.8/site-packages')
import cv2

IMG_PATH = './photo/girl_xinh_2.jpg'

# read image
img = cv2.imread(IMG_PATH)
print(IMG_PATH, img.shape)

new_width = 800
new_height = 400
img_resized = cv2.resize(src=img, dsize=(new_width, new_height))
reisze_img_name = 'girl_xinh_2_%dx%d.jpg' % (new_width, new_height)
cv2.imwrite(reisze_img_name, img_resized)
print(reisze_img_name, img_resized.shape)

fx = 0.5
fy = 1.0
img_resized = cv2.resize(src=img, dsize=None, fx=fx, fy=fy)
reisze_img_name = 'girl_xinh_2_fx=%.1f_fy=%.1f.jpg' % (fx, fy)
cv2.imwrite(reisze_img_name, img_resized)
print(reisze_img_name, img_resized.shape)

print('Done')