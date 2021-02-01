marks = [40,80,45,70,66,86]

maxmarks= marks[0];

for mark in marks:
	if (mark > maxmarks):
		maxmarks = mark

print(f'Maximum marks : {maxmarks}')