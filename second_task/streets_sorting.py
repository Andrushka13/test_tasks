from pprint import pprint


with open('input.csv', encoding='utf-8') as input_file:
	head_line = input_file.readline()
	dlist = input_file.read().splitlines()
	print(head_line)

new_dlist = []

for line in dlist:
	new_line = line.split(',')
	if new_line[2] == 'да':
		new_line[0] = new_line[0].split()
		new_dlist.append(new_line)
dlist.clear()

sorted_list = sorted(new_dlist)
new_dlist.clear()


for row in sorted_list:
	for elem in row:
		if str != type(elem):
			elem = ' '.join(map(str, elem))
			new_dlist.append(elem)
		else:
			new_dlist.append(elem)
sorted_list.clear()

#pprint(new_dlist)

#string = ','.join(new_dlist)
#print(string)

output_file = open('output.csv', 'w')

output_file.write(head_line)
#output_file.writelines(new_dlist[0])
#output_file.write(',')
for i in range(len(new_dlist)):
	output_file.writelines(new_dlist[i])
	if (i + 1) % 3 != 0:
		output_file.write(',')
	else:
		output_file.write('\n')
output_file.close()
