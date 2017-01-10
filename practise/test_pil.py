<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import Image, ImageDraw, ImageFont, ImageFilter
import random

# Random character
def rndChr():
	if random.randint(0, 1) == 0:
		return chr(random.randint(65, 90))
	else:
		return chr(random.randint(97, 122))
	

# Random color 1
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# Random color 2
def rndColor2():
	return (random.randint(32, 127), random.randint( 32, 127), random.randint(32, 127))

# Compare the security code generated
def compareCode(code1, code2):
	return code1 == code2

def main():
	width = 60 * 4
	height = 60
	image = Image.new('RGB', (width, height), (255, 255, 255))
	# Create Font object
	font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 36)
	# font = ImageFont.truetype('Arial.ttf', 36)
	# Create Draw object
	draw = ImageDraw.Draw(image)
	# Fill up every pixel
	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=rndColor())
	# Output text
	codeList = []
	for t in range(4):
		codeList.append(rndChr())
		draw.text((60 * t + 10, 10), codeList[t], font=font, fill=rndColor2())
	authCode = ''.join(codeList)
	# Blur
	image = image.filter(ImageFilter.BLUR)
	image.save('code.jpg', 'jpeg')

	inputCode = raw_input("Type in the auth code:")

	print compareCode(authCode.upper(), inputCode.upper())


if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import Image, ImageDraw, ImageFont, ImageFilter
import random

# Random character
def rndChr():
	if random.randint(0, 1) == 0:
		return chr(random.randint(65, 90))
	else:
		return chr(random.randint(97, 122))
	

# Random color 1
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# Random color 2
def rndColor2():
	return (random.randint(32, 127), random.randint( 32, 127), random.randint(32, 127))

# Compare the security code generated
def compareCode(code1, code2):
	return code1 == code2

def main():
	width = 60 * 4
	height = 60
	image = Image.new('RGB', (width, height), (255, 255, 255))
	# Create Font object
	font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 36)
	# font = ImageFont.truetype('Arial.ttf', 36)
	# Create Draw object
	draw = ImageDraw.Draw(image)
	# Fill up every pixel
	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=rndColor())
	# Output text
	codeList = []
	for t in range(4):
		codeList.append(rndChr())
		draw.text((60 * t + 10, 10), codeList[t], font=font, fill=rndColor2())
	authCode = ''.join(codeList)
	# Blur
	image = image.filter(ImageFilter.BLUR)
	image.save('code.jpg', 'jpeg')

	inputCode = raw_input("Type in the auth code:")

	print compareCode(authCode.upper(), inputCode.upper())


if __name__ == '__main__':
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
	main()