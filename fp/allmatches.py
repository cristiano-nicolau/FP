def allMatches(lst):
	matches = []
	for team1 in lst:
		for team2 in lst:
			if team1 != team2:
				matches.append((team1, team2))
	return matches

teams = ["FCP", "SLB", "SCP"]
print(allMatches(teams))
