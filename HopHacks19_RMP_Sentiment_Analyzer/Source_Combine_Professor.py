import Source_Professor
import os

if __name__ == '__main__':

	Source_Professor.Function_Professor()

	command = "gcloud ml language analyze-sentiment --content-file='Comments_Professor.txt'"
	command = command + " > Results_Professor.txt"
	os.system(command)

	f = open("Results_Professor.txt", "r")
	
	cnt = 0
	for i in f:
		cnt = cnt+1
		if cnt == 3:
			magnitude = i
		if cnt == 4:
			score = i
		if cnt > 4:
			break
	
	output = open("Result.txt", "w")

	output.write("Magnitude: ")
	magnitude_result = ""
	cnt = -1

	for i in magnitude:
		
		if i == ',':
			break
		if i == ':':
			cnt = 0
		if cnt != -1:
			cnt = cnt+1
		if cnt > 2:
			magnitude_result = magnitude_result + i				
	
	output.write(magnitude_result)
	output.write('\n')

	output.write("Score: ")
	score_result = ""
	cnt = -1

	for i in score:
		
		if i == ':':
			cnt = 0
		if cnt != -1:
			cnt = cnt + 1
		if cnt > 2:
			score_result = score_result + i

	output.write(score_result)
