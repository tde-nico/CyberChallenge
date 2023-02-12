
def	unbalancer(n, k, works):
	for i in range(k):
		m = max(works)
		works[works.index(m)] = 0
		works[works.index(max(works))] += m
	return max(works) - min(works)


def test(n, k, works, out):
	assert(unbalancer(n, k, works) == out)


if __name__ == "__main__":
	n, k = map(int, input().strip().split())
	works = list(map(int, input().strip().split()))
	print(unbalancer(n, k, works))
	#test(5, 1, [5,0,4,4,4], 9)
