data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 1:
			print(len(data))
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均有', sum_len/len(data), '筆數量')