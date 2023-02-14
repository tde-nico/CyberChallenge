#!/usr/bin/python3

def	national(n, t, cks):
	w = [0 for _ in range(int(sum(cks)/t))]
	#print(len(w))
	c = 0
	while c < len(cks):
		c = 0
		w = [0 for _ in range(len(w) + 1)]
		#print(len(w), c, len(cks))
		s = 0
		while s < t and c < len(cks):
			for _ in range(len(w)):
				w.sort()
				if w[0] == s and c < len(cks) and w[0] + cks[c] <= t:
					w[0] += cks[c]
					c += 1
				else:
					break
			s = w[0]
	return len(w)
    
if __name__ == "__main__":
	n, t = map(int, input().strip().split())
	checks = list(map(int, input().strip().split()))
	print(national(n ,t, checks))
