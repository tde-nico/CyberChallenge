
def cover(n, k, ranges):
	expanded = []
	out = []
	for ran in ranges:
		expanded += list(range(ran[0], ran[1]+1))
	for num in expanded:
		if num not in out and expanded.count(num) == k:
			out.append(num)
	return len(out)

def test(n, k, ranges, out):
	assert(cover(n, k ,ranges) == out)

if __name__ == "__main__":
	n, k = map(int, input().strip().split(" "))
	ranges = []
	for i in range(n):
		ranges.append(list(map(int, input().strip().split(" "))))
	print(cover(n, k, ranges))
	#test(6, 3, [[3,10],[0,5],[6,13],[1,15],[13,19],[15,18]], 10)

