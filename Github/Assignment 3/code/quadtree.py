import boundingbox as bb
import math
import numpy as np
class QuadTree:
	"""
	The QuadTree class is a tree data structure in which each internal
	non leave node has exactly four children.
	
	the internal data structre `self.quads = {}` is a dictionary where its
	keys represent depth (starting from 0) and has a list of BoundingBoxes representing
	the partions/space. The total area of at each level should remain equal to the initial
	bounding box.
	
	self.quads = 
	{
		0: [1    x BoundingBox ]
		1: [4    x BoundingBox ]
		.. 
		n: [4**n x BoundingBox ]
	}
	
	Generation of the QuadTree is slow, using it to reduce your dataset it fast.

	"""
	def __init__(self,bbox, depth):
		"""
		Create a new QuadTree instance.
		:param bbox: the initial BoundingBox
		:param depth: the depth of the QuadTree

		:Example:
		>>> bbox = bb.BoundingBox(2,9,1,7)
		>>> qt = QuadTree(bbox, 2)
		"""
		self.quads = {}
		self.depth = depth

		for x in range(depth):
			self.quads[x]= []

		self.quads[0] = [bbox]
		self.recurse(bbox, 1)

	def recurse(self, bbox, depth):
		"""
		Internal function called on class contruction, this should 
		create the BoundingBoxes.

		:param bbox: the initial BoundingBox
		:param depth: the depth of the QuadTree

		:To be implemented by the student:		
		"""

		current_level = 1;
		while (current_level <= 1):
			for k, v in self.quads.items():
				print(k, len(v))
				for x in v:

					# currLevelBB = bb.BoundingBox.from_dataset(np.transpose(x.data), xindex= 0, yindex= 1)
					currLevelBB = bb.BoundingBox.from_matrix(x.data)
					print(currLevelBB)
					bbWidth = currLevelBB.width()
					bbHeight = currLevelBB.height()
					lowerleft = currLevelBB.lower_left()

					bottom_left = bb.BoundingBox(lowerleft[0], lowerleft[0] + bbWidth / 2, lowerleft[1], lowerleft[1] + bbHeight / 2)
					bottom_right = bb.BoundingBox(lowerleft[0] + bbWidth / 2, lowerleft[0] + bbWidth, lowerleft[1], lowerleft[1] + bbHeight / 2)
					top_left = bb.BoundingBox(lowerleft[0], lowerleft[0] + bbWidth / 2, lowerleft[1] + bbHeight/2, lowerleft[1] + bbHeight)
					top_right = bb.BoundingBox(lowerleft[0] + bbWidth / 2, lowerleft[0] + bbWidth, lowerleft[1] + bbHeight/2, lowerleft[1] + bbHeight)

					self.quads[current_level] = [bottom_left, bottom_right, top_left, top_right]

					print(current_level)
			current_level += 1

		# print(self.quadrants())
		for k,v in self.quads.items():
			print (k,len(v))
			for x in v:
				print(x.data)


	@staticmethod	
	def at_least(size):
		"""
		Returns the amount of BoundingBoxes when the user
		request `at least` an amount of bboxes. The returned
		value is >= than size.
		
		:param size: minimum requested size

		:Example:
		>>> print(QuadTree.at_least(900))
		>>> 1024	
		"""
		return 4**int(math.ceil(math.log(size,4)))

	@staticmethod	
	def at_most(size):
		"""
		Returns the amount of BoundingBoxes when the user
		request `at most` an amount of bboxes. The returned
		value is <= than size.
		
		:param size: maximum requested size

		:Example:
		>>> print(QuadTree.at_most(900))
		>>> 256
		"""
		return 4**int(math.floor(math.log(size,4)))

	@staticmethod	
	def level(size):
		"""
		Returns the level required (rounded up)
		for a given size of elements. 
		return int(math.ceil(math.log(size,4)))
	
		:param size: requested size
		>>> print(QuadTree.level(1))
		>>> 0
		>>> print(QuadTree.level(5))
		>>> 2
		"""
		return int(math.ceil(math.log(size,4)))

	def quadrants(self):
		"""
		Returns the quads member
		"""
		return self.quads

if __name__ == '__main__':

	bbox = bb.BoundingBox(2,9,1,7)
	# print(QuadTree.at_least(900))
	# print(QuadTree.at_most(900))
	# print(QuadTree.level(1))
	# print(QuadTree.level(5))
	# print(QuadTree.level(900))

	qt = QuadTree(bbox, 2)
	# for k,v in qt.quads.items():
	# 	print (k,len(v))
	# 	for x in v:
	# 		print(x.data)

