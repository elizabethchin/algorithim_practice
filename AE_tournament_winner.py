def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ""
	scores = {currentBestTeam: 0}
	
	for i, competition in enumerate(competitions):
		
		result = resluts[i]
		homeTeam, awayTeam = competitions
		
		winningTeam = homeTeam if result == 1 else awayTeam
		
		updateScores(winningTeam, 3, scores)
		
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
			
    return currentBestTeam
			
def updateScores(team, points, scores):
	
	if team not in scores:
		scores[team] = 0
		
	scores[team] += points
