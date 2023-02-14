#!/usr/bin/python3

def	selection(n, m, s, skills, candidates):
	#print(skills)
	#print(candidates)
	for c in candidates.values():
		#print(skills)
		for skill in skills:
			skills[skill].sort()
		for skill in c:
			if skill[0] in skills and skills[skill[0]][0] < skill[1]:
				skills[skill[0]][0] = skill[1]
	count = sum([sum(power) for power in skills.values()])
	return count

if __name__ == "__main__":
	tests = list(map(int, input().strip().split()))[0]
	for t in range(tests):
		n, m, s = list(map(int, input().strip().split()))
		skills = input().strip().split()
		skills = {key: [0]*skills.count(key) for key in skills}
		candidates = {}
		for i in range(n):
			id = list(map(int, input().strip().split()))[0]
			skls = [(lambda x: (x[0], int(x[1])))(input().strip().split()) for _ in range(s)]
			candidates[id] = candidates.get(id, []) + skls
		print(selection(n, m, s, skills, candidates))
