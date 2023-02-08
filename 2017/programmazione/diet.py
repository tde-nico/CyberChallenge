
def	diet(n, v):
	w = [0 for _ in range(n)]
	p = [-1 for _ in range(n)]
	for i in range(n-1, -1, -1):
		w[i] = v[i]
		for j in range(i+1, n):
			if v[j] <= v[i]:
				if w[j]+v[i] > w[i]:
					w[i] = w[j] + v[i]
					p[i] = j
	idx = 0
	for i in range(n):
		if w[i] > w[idx]:
			idx = i
	out = []
	while idx != -1:
		out.append(str(v[idx]))
		idx = p[idx]
	return len(out), out


def	test(n, v, len, out):
	res = diet(n, v)
	assert(res[0] == len)
	assert(res[1] == out)



if __name__ == "__main__":
	n = int(input())
	v = [int(_) for _ in input().split(" ")]
	res = diet(n, v)
	print(res[0])
	print(''.join(res[1]))
	'''
	test(8, [389, 207, 155, 300, 299, 170, 158, 65],
		6, ['389', '300', '299', '170', '158', '65'])
	test(4, [16, 93, 107, 224],
		1, ['224'])
	'''
