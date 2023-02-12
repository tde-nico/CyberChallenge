
def isderivable(old_password, new_password):
	m, n = len(old_password), len(new_password)
	if abs(m - n) > 1:
		return False

	i, j, count = 0, 0, 0
	while i < m and j < n:
		if old_password[i] != new_password[j]:
			count += 1
			if m > n:
				i += 1
			elif m < n:
				j += 1
			else:
				i += 1
				j += 1
		else:
			i += 1
			j += 1
	if i < m or j < n:
		count += 1
	return count <= 1

def ppo(pas, old):
	if 8 > len(pas) > 16:
		return 0
	flags = [0,0,0,0] #lower upper, digit, special
	previous = ""
	for char in pas:
		if char.islower():
			flags[0] = 1
		elif char.isupper():
			flags[1] = 1
		elif char.isdigit():
			flags[2] = 1
		else:
			flags[3] = 1
		if char == previous:
			return 0
		previous = char
	if not all(flags):
		return 0
	if isderivable(pas, old):
		return 0
	return 1

def test(pas, old, out):
	assert(ppo(pas, old) == out)

if __name__ == "__main__":
	n = int(input())
	pas, old = [], []
	# inp = """
	# short abcdEFGH1234!*-?
	# veryverylongpassw abcdEFGH1234!*-?
	# ALLUPPER abcdEFGH1234!*-?
	# UpperLower abcdEFGH1234!*-?
	# P4ssword! abcdEFGH1234!*-?
	# bcdEFGH1234!*-? abcdEFGH1234!*-?
	# xabcdEFGH1234!*-? abcdEFGH1234!*-?
	# xbcdEFGH1234!*-? abcdEFGH1234!*-?
	# ?3CuR3P4s?w0rd abcdEFGH1234!*-?
	# """.strip().split("\n")
	# 	outs = [0, 0, 0, 0, 0, 0, 0, 0, 1]
	for i in range(n):
		p, o = input().strip().split(" ")
		pas.append(p)
		old.append(o)
	for i in range(n):
		print(ppo(pas[i], old[i]))
	#	test(pas[i], old[i], outs[i])

