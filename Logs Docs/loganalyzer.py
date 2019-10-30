import re

filename = "ssh.log"
regex_pattern = r'^([\d\.]+\s+(\w+)\s+([\d\.]+))'
outcomes = {}

with open(filename,'r') as f:
	line = f.readline().strip()
	while line:
		results = re.search(regex_pattern,line)
		if (results ):
			# This value determines which group to tally
			fromgroup = 3
			thisgroup = results.group(fromgroup)
			if thisgroup in outcomes.keys():
				outcomes[thisgroup] += 1
			else:
				outcomes[thisgroup] = 1
		line = f.readline()

out_sorted = sorted(outcomes.items(),key=lambda x: x[1],reverse=True)

for k,v in out_sorted:
	print(k,":\t", v)