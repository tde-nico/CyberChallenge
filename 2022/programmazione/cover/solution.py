
def cover(n, k, ranges):
	count, level = 0, 0
	ranges.sort()
	for i in range(len(ranges)):
		level += ranges[i][1]
		if level == k:
			count += ranges[i+1][0] - ranges[i][0]
	return count

def test(n, k, ranges, out):
	assert(cover(n, k ,ranges) == out)

if __name__ == "__main__":
	n, k = map(int, input().strip().split(" "))
	ranges = []
	for i in range(n):
		start, end = list(map(int, input().strip().split(" ")))
		ranges += [[start, +1], [end+1, -1]]
	print(cover(n, k, ranges))
	#test(6, 3, [[3,10],[0,5],[6,13],[1,15],[13,19],[15,18]], 10)

