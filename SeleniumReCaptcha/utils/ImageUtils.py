from urllib.request import urlopen
import cv2 as cv
import numpy as np

def url_to_image(url):
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv.imdecode(image, cv.IMREAD_COLOR)
	print(url)
	return image

def cut_image_in_tiles(image, rows, columns):
	result = []
	image_info = image.shape
	tile_height = image_info[0]/columns
	tile_width = image_info[1]/rows
	for row in range(rows):
		for column in range(columns):
			result.append(image[int(tile_height*column):int(tile_height*(column+1)), int(tile_width*row):int(tile_width*(row+1))])
	return result