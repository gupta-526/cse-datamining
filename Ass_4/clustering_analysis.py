import os, sys, math, csv, random

def get_input(filename):
	data = open(filename, 'r')
	reader = csv.reader(data)
	print(data)
	length = len(reader)
	row = random.randint(1,length-1)
	x = row[1]
	return x

def get_average(filename):
	data = open( filename, 'r')
	reader = csv.reader(data)
	m_i = []
	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0
	count = 0
	for row in reader:
		if row[3]=="1":
			sum_1 += row[1]
			count_1 += 1
		if row[3]=="2":
			sum_2 += row[1]
			count_2 += 1
		if row[3]=="3":
			sum_3 += row[1]
			count_3 += 1
		if row[3]=="4":
			sum_4 += row[1]
			count_4 += 1
		# count += 1
	avg_1 = sum_1/count_1
	avg_2 = sum_2/count_2
	avg_3 = sum_3/count_3
	avg_4 = sum_4/count_4
	m_i.append(avg_1)
	m_i.append(avg_2)
	m_i.append(avg_3)
	m_i.append(avg_4)
	return m_i

def get_average2(filename):
	data = open(filename, 'r')
	reader = csv.reader(data)
	m_i = []
	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0
	count = 0
	for row in reader:
		if not row[3] =="1":
			sum_1 += row[1]
			count_1 += 1
		if not row[3]=="2":
			sum_2 += row[1]
			count_2 += 1
		if not row[3]=="3":
			sum_3 += row[1]
			count_3 += 1
		if not row[3]=="4":
			sum_4 += row[1]
			count_4 += 1
		# count += 1
	avg_1 = sum_1/count_1
	avg_2 = sum_2/count_2
	avg_3 = sum_3/count_3
	avg_4 = sum_4/count_4
	m_i.append(avg_1)
	m_i.append(avg_2)
	m_i.append(avg_3)
	m_i.append(avg_4)
	return m_i

def calc_sse(filename, k):
	i=1
	sse = 0
	for i in range(1,k+1):
		dist = math.sqrt(get_input(filename), get_average(filename)[i])
		total += dist
	return sse

def calc_ssb(filename, k):
 	i=1
 	ssb = 0
 	for i in range(1, k+1):
 		dist = math.sqrt(get_input(filename), get_average2[i])
 		total += dist
 	return ssb

def main():
	i=2
	k = input("Please enter a value for k: ")
	for i in range(2,int(k)+1) :
		twodimeasy = calc_sse("Data/TwoDimEasy.csv",i)
		twodimhard = calc_sse("Data/TwoDimEasy.csv",i)
		wine = calc_sse("Data/wine_quality-red.csv",i)
		print("sse for Two Dim Easy: ", twodimeasy)
		print("sse for Two Dim Hard: ", twodimhard)
		print("sse for wine quality: ", wine)
		twodimeasy2 = calc_sse("Data/TwoDimEasy.csv",i)
		twodimhard2 = calc_sse("Data/TwoDimEasy.csv",i)
		wine2 = calc_sse("Data/wine_quality-red.csv",i)
		print("ssb for Two Dim Easy: ", twodimeasy2)
		print("ssb for Two Dim Hard: ", twodimhard2)
		print("ssb for wine quality: ", wine2)
		i += 1
	return 0

main()

