import UlaModule

def test(verbose:bool=False):
	success, fail, total = 0,0,0
	for n in range(100):
		point = UlaModule.int_2_coord(n)
		backwards = UlaModule.coord_2_int(point[0], point[1])
		
		if verbose:
			print("{0} -> ({1},{2}) -> {3}".format(n, point[0], point[1], backwards))
		
		if n == backwards:
			success += 1
		else:
			fail += 1
		total += 1

	print("Succeeded on {0} out of {2} times.\n({0} successes, {1} fails)".format(success, fail, total))
	return fail

test()