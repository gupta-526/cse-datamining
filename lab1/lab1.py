import csv, sys, os, string

file_name = input("Please Enter a file name: ")
input_file = open(file_name, 'r')
out_file = open('dataset/transformed_file.csv', 'w')
reader = (csv.reader(input_file))
writer = csv.writer(out_file)
i=0
for row in reader:
	if "?" in row:
		print(row[0])
	else:
		if row[2] == ' Never-worked':
			row[2] = '0'
		elif row[2] == " Without-pay":
			row[2] = "1"
		elif row[2] == " Self-emp-not-inc":
			row[2] = "2"
		elif row[2] == " Self-emp-inc":
			row[2] = "3"
		elif row[2] == " Private":
			row[2] = "4"
		elif row[2] == " Local-gov":
			row[2] = "5"
		elif row[2] == " Federal-gov":
			row[2] = "6"
		elif row[2] == " State-gov":
			row[2] = "7"
		
		if row[6] ==" Married-civ-spouse":
			row[6] = "0"
		elif row[6] == " Divorced":
			row[6] = "1"
		elif row[6] == " Never-married":
			row[6] = "2"
		elif row[6] == " Widowed":
			row[6] = "3"
		elif row[6] == " Married-spouse-absent":
			row[6] = "4"
		elif row[6] == " Married-AF-spouse":
			row[6] = "5"
		elif row[6] == " Separated":
			row[6] = "6"
		
		if row[7] == " Tech-support":
			row[7] = "0"
		elif row[7] == " Craft-repair":
			row[7] = "1"
		elif row[7] == " Other-service":
			row[7] = "2"
		elif row[7] == " Sales":
			row[7] = "3"
		elif row[7] == " Exec-managerial":
			row[7] = "4"
		elif row[7] == " Prof-specialty":
			row[7] = "5"
		elif row[7] == " Handlers-cleaners":
			row[7] = "6"
		elif row[7] == " Machine-op-inspct":
			row[7] = "7"
		elif row[7] == " Adm-clerical":
			row[7] = "8"
		elif row[7] == " Farming-fishing":
			row[7] = "9"
		elif row[7] == " Transport-moving":
			row[7] = "10"
		elif row[7] == " Priv-house-serv":
			row[7] = "11"
		elif row[7] == " Protective-serv":
			row[7] = "12"
		elif row[7] == " Armed-forces":
			row[7] = "13"
		
		if row[8] == " Wife":
			row[8] = "0"
		elif row[8] == " Own-child":
			row[8] = "1"
		elif row[8] == " Husband":
			row[8] = "2"
		elif row[8] == " Not-in-family":
			row[8] = "3"
		elif row[8] == " Other-relative":
			row[8] = "4"
		elif row[8] == " Unmarried":
			row[8] = "5"

		if row[9] == " White":
			row[9] = "0"
		elif row[9] == " Asian-Pac-Islander":
			row[9] ="1"
		elif row[9] == " Amer-Indian-Eskimo":
			row[9] ="2"
		elif row[9] == " Black":
			row[9] ="3"
		elif row[9] == " Other":
			row[9] = "4"
		
		if row[10] == ' Male':
			row[10] = '0'
		elif row[10] == ' Female':
			row[10] = '1'
		
		if row[14] == " United-States":
			row[14] = "0"
		elif row[14] == " Canada":
			row[14] = "1"
		elif row[14] == " England":
			row[14] = "2"
		elif row[14] == " Cambodia":
			row[14] = "3"
		elif row[14] == " Puerto-Rico":
			row[14] = "4"
		elif row[14] == " Germany":
			row[14] = "5"
		elif row[14] == " Outlying-us":
			row[14] = "6"
		elif row[14] == " India":
			row[14] = "7"
		elif row[14] == " Japan":
			row[14] = "8"
		elif row[14] == " Greece":
			row[14] = "9"
		elif row[14] == " South":
			row[14] = "10"
		elif row[14] == " China":
			row[14] = "11"
		elif row[14] == " Cuba":
			row[14] = "12"
		elif row[14] == " Iran":
			row[14] = "13"
		elif row[14] == " Honduras":
			row[14] = "14"
		elif row[14] == " Philippines":
			row[14] = "15"
		elif row[14] == " Italy":
			row[14] = "16"
		elif row[14] == " Poland":
			row[14] = "17"
		elif row[14] == " Jamaica":
			row[14] = "18"
		elif row[14] == " Vietnam":
			row[14] = "19"
		elif row[14] == " Mexico":
			row[14] = "20"
		elif row[14] == " Portugal":
			row[14] = "21"
		elif row[14] == " Ireland":
			row[14] = "22"
		elif row[14] == " France":
			row[14] = "23"
		elif row[14] == " Dominican-Republic":
			row[14] = "24"
		elif row[14] == " Laos":
			row[14] = "25"
		elif row[14] == " Ecuador":
			row[14] = "26"
		elif row[14] == " Taiwan":
			row[14] = "27"
		elif row[14] == " Haiti":
			row[14] = "28"
		elif row[14] == " Columbia":
			row[14] = "29"
		elif row[14] == " Hungary":
			row[14] = "30"
		elif row[14] == " Guatemala":
			row[14] = "31"
		elif row[14] == " Nicaragua":
			row[14] = "32"
		elif row[14] == " Scotland":
			row[14] = "33"
		elif row[14] == " Thailand":
			row[14] = "34"
		elif row[14] == " Yugoslavia":
			row[14] = "35"
		elif row[14] == " El-salvador":
			row[14] = "36"
		elif row[14] == " Trinadad&Tobago":
			row[14] = "37"
		elif row[14] == " Hong":
			row[14] = "39"
		elif row[14] == " Holand-netherlands":
			row[14] = "40"
		row[15]=""
		j=4
		while(j<14):
			row[j]=row[j+1]
			j=j+1
		row[14]=""
		writer.writerow(row)


out_file.close()
input_file.close()