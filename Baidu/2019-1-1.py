line = input()
total_list = set()
for i in range(len(line)):
	new_line = line[1:] + line[0]
	line = new_line
	if new_line not in total_list:
		total_list.append(new_line)
print(len(set(total_list)))
