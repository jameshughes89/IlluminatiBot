'''
Script to generate a nunch of triangle images for training an ANN to find triangles. 
The hope is that we can apply this ANN to other images to find triangles. 
The triangles will be somewhat equilateral. 
'''
import numpy
import PIL
import PIL.Image
import PIL.ImageDraw

imageSizes = [250,
				500,]

# Colours of the (background, triangle, and width)
imageColours = [('black', 'white', 1), 
				('white','black', 1), 
				('white', 'pink', 5)]	# for testing purposes

for iSize in imageSizes:
	for i in range(50):
		# top point (make it near the top centre)
		x1 = numpy.random.randint(low=(iSize/2)*0.8, high=(iSize/2)*1.1)
		y1 = numpy.random.randint(low=0, high=iSize*.1)
	
		## left point
		x2 = numpy.random.randint(low=0, high=x1)
		y2 = numpy.random.randint(low=iSize/2, high=iSize)

		# right point
		x3 = numpy.random.randint(low=(x2+(x1-x2)*2)*0.9, high= (x2+(x1-x2)*2)*1.1)
		y3 = numpy.random.randint(low=(y2)*0.9, high= min((y2)*1.1,iSize))

		print x1, y1
		print x2, y2
		print x3, y3		

		for iCol in imageColours:

			img = PIL.Image.new('RGB', (iSize,iSize), iCol[0])
	
			draw = PIL.ImageDraw.Draw(img)
			draw.line((x1,y1, x2, y2), iCol[1], width=iCol[2])
			draw.line((x2,y2, x3, y3), iCol[1], width=iCol[2])
			draw.line((x3,y3, x1, y1), iCol[1], width=iCol[2])

			img.save('./trainingTriangles/' + str(i) + '_' + iCol[1] + '.bmp')
