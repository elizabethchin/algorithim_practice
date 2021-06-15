def minimumWaitingTime(queries):
    # Write your code here.
	
	queries.sort() #sort in place
	
	total_waiting_time = 0
	
	for i, duration in enumerate(queries):
		queries_left = len(queries) - (i + 1)
		total_waiting_time += duration * quereis
	return total_waiting_time

#O(nLogn) time | O(1) space