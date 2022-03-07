from sys import stdin as s
from itertools import combinations as c

def sol(team1_list, scoreboard):
	score1 = 0
	score2 = 0
	n = len(scoreboard)
	team2_list = [i for i in range(n) if i not in team1_list]
	for i in team1_list:
		for j in team1_list:
			score1 += scoreboard[i][j]
	for p in team2_list:
		for q in team2_list:
			score2 += scoreboard[p][q]
	return abs(score1 - score2)

n = int(s.readline())
score = [ ]
for _ in range(n):
	score.append(list(map(int, s.readline().split())))

team_with_0 = list(c(range(1, n), n // 2 - 1))

m = 1000
for team in team_with_0:
	team1 = [0] + list(team)
	m = min(m, sol(team1, score)) 
print(m)