from PIL import Image

def make_shape(func, width=300, height=100):
	'''
	take a function and use it to draw a shape :D
	the function will receive the arguments:
	- pixels: a 2d list
	- width: the width of the image
	- height: the eight of the image
	- black_pixel: a black pixel that can be put inside "pixels"
	'''
	img = Image.new('RGB', (width, height), "white") # create a new black image
	pixels = img.load() # create the pixel map
	black_pixel = (0, 0, 0)
	func(pixels, width, height, black_pixel)
	img.show()

# def example_random_pixels(pixels, width, height, black_pixel):
# 	''' example drawing function that put 2000 points at random '''
# 	from random import randint
# 	for i in range(2000):
# 		pixels[randint(0, width - 1), randint(0, height - 1)] = black_pixel

# # we run it with example_random_pixels
# make_shape(example_random_pixels)


# make it run with an horizontal line
# def horizontal_line(pixels, width, height, black_pixel):
# 	"""
# 	this function will show you a horizontal line
# 	"""
# 	for w in range(0, width):
# 		pixels[w, height / 2] = black_pixel   # "height / 2" -> keep the line in the middle

# make_shape(horizontal_line)


# make it run with a vertical line
# def vertical_line(pixels, width, height, black_pixel):
# 	"""
# 	this function will show you a vertical line
# 	"""
# 	for h in range(0, height):
# 		pixels[width / 2, h] = black_pixel   # "width / 2" -> keep the line in the middle

# make_shape(vertical_line)

		
# make it run with a cross
# def cross(pixels, width, height, black_pixel):
# 	"""
# 	this function will show you a cross
# 	it only works if the image is a square
# 	"""
	# for w in range(0, width):
	# 	for h in range(0, height): 
	# 		w = h
	# 		pixels[w, h] = black_pixel	
	# w = 0
	# h = 0
	# while w < width and h < height:
	# 	pixels[w, h] = black_pixel
	# 	w = w + 1
	# 	h = h + 1

	# w = 0
	# h = 700
	# while w < width and h >= 0:
	# 	pixels[w, h-1] = black_pixel
	# 	w = w + 1
	# 	h = h - 1

# make_shape(cross, width=700, height=700)	


# make it run with stripes
# def stripes(pixels, width, height, black_pixel):
# 	"""
# 	this function will show you stripes
# 	"""
# 	for h in range(0, height, 10):    # "10" -> the distance between the stripes
# 		for w in range(0, width):
# 			pixels[w, h] = black_pixel

# make_shape(stripes)


# make fat stripes
def fat_stripes(pixels, width, height, black_pixel):
	""""
	this function will show you fat stripes
	"""
	stripe_size = 38      
	for h in range(0, height, stripe_size):
		for i in range(h, h + stripe_size / 2 + 1):  
			if i < height:
				for w in range(0, width):
 					pixels[w, i] = black_pixel
			

make_shape(fat_stripes)


# make it run with a chess board


# make it run with a circle :)


# make a UK flag


















































































































































































































# mine
# def example_chess(pixels, width, height, black_pixel):
# 	''' let's see how much time it takes her to discover the solution is here '''
# 	thick_w = width / 8.0
# 	thick_h = height / 8.0
# 	for w in range(width):
# 		for h in range(height):
# 			if (w // thick_w) % 2 == (h // thick_h) % 2:
# 				pixels[w, h] = black_pixel


# make_shape(example_chess)



