#!/usr/bin/python3

def	winner(m, n, s, tasks, subs):
	grades = [[i+1, 0, -1, [0 for _ in range(n)]] for i in range(m)]
	for sub in subs:
		#print(sub, "\t", end="")
		if sub[2] == tasks[sub[1]-1][1]:
			if not grades[sub[0]-1][3][sub[1]-1]:
				grades[sub[0]-1][1] += tasks[sub[1]-1][2]
				if grades[sub[0]-1][2] < sub[3]:
					grades[sub[0]-1][2] = sub[3]
			grades[sub[0]-1][3][sub[1]-1] = 1
		#print(grades)
	grades.sort(key=lambda x: (x[1], -x[2], -x[0]), reverse=True)
	return grades

if __name__ == "__main__":
	m, n, s = map(int, input().strip().split())
	tasks = [list((lambda x: (int(x[0]), x[1], int(x[2])))(input().strip().split())) for _ in range(n)]
	submissions = [list((lambda x: (int(x[0]), int(x[1]), x[2], int(x[3])))(input().strip().split())) for _ in range(s)]
	grades = winner(m, n, s, tasks, submissions)
	for grade in grades:
		print(grade[0], grade[1])
		#print(grade[0], grade[1], grade[2])
