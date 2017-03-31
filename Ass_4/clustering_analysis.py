import os, sys, math

def get_input(filename):
	data = csv.reader('Data/'+ filename, 'r')
	x = random.choice(data[1])
	return x

def get_average(filename):
	data = csv.reader('Data/'+filename, 'r')
	m_i = []
	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0
	count = 0
	for row in data:
		if row[3]=="1":
			sum_1 += row[1]
		if row[3]=="2":
			sum_2 += row[1]
		if row[3]=="3":
			sum_3 += row[1]
		if row[3]=="4":
			sum_4 += row[1]
		count += 1
	avg_1 = sum_1/count
	avg_2 = sum_2/count
	avg_3 = sum_3/count
	avg_4 = sum_4/count
	m_i.append(avg_1)
	m_i.append(avg_2)
	m_i.append(avg_3)
	m_i.append(avg_4)
	return m_i

def calc_sse(cluster_num, filename, k):
	i=1
	sse = 0
	for i<=k
		dist = sqrt(get_input(filename), get_average[i])
		total += dist
	return sse

def calc_ssb():

	return 0