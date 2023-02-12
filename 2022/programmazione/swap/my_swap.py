
def	swap(n, v):
	res = -1
	vsort = sorted(v)
	for i in range(n):
		if v[i] != vsort[i]:
			res += 1
	return res


def	test(n, v, out):
	assert(swap(n, v) == out)


if __name__ == "__main__":
	n = int(input())
	v = list(map(int, input().split(" ")))
	print(swap(n, v))
	#test(5, [1, 2, 6, 5, 9], 1)
	#test(6, [1, 2, 3, 9, 5, 6], 2)
