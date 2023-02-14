#!/usr/bin/python3

def	pretest(q, correct, ans):
	res = 0
	for i in range(q):
		if correct[i] == ans[i]:
			res += 1
	return res

if __name__ == "__main__":
	q, n = map(int, input().strip().split())
	correct = input().strip()
	ans = [input().strip() for _ in range(n)]
	for a in ans:
		print(pretest(q, correct, a))
