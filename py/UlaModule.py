from math import floor, sqrt

def int_2_point(num:int):
	point = [0,0]
	# get largest square smaller than num
	root = floor(sqrt(num))
	square = root ** 2
	# get smallest square larger than num
	big_root = root + 1
	big_square = big_root ** 2
	# calculate a difference of squares
	diff = big_square - square

	remainder = num - square

	halfway = floor(diff/2)

	if root % 2 == 0:
		point = [-floor(root / 2), floor(root / 2)]
		point[1] -= min(halfway, remainder)
		remainder -= min(halfway, remainder)
		point[0] += remainder
	else:
		point = [floor(root / 2) + 1, -floor(root / 2)]
		point[1] += min(halfway, remainder)
		remainder -= min(halfway, remainder)
		point[0] -= remainder
	return point

def point_2_int(px:int,py:int):
	absx, absy = abs(px), abs(py)

	root = max(absx, absy) * 2 - 1 * (px+py > 0)

	layer = floor(root/2)
	root_pt = [0,0]
	if root % 2 == 0:
		root_pt = [-layer, layer]
	else:
		root_pt = [layer+1, -layer]

	dist = abs(root_pt[0] - px) + abs(root_pt[1] - py)

	num = root ** 2 + dist
	return num
