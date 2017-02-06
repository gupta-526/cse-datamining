import csv, sys, os

file_name = raw_input("Please Enter a file name")
input_file = open(file_name, 'rb')
out_file = open(transformed_file.csv, 'wb')
reader = csv.reader(input_file)
writer = csv.writer(out_file)
for row in reader:
	if row[2] == 'never-worked':
		row[2] = '0'
	elif row[2] == "without-pay":
		row[2] = "1"
	elif row[2] == "self-emp-not-inc":
		row[2] = "2"
	elif row[2] == "self-emp-inc":
		row[2] = "3"
	elif row[2] == "private":
		row[2] = "4"
	elif row[2] == "local-gov":
		row[2] = "5"
	elif row[2] == "federal-gov":
		row[2] = "6"
	
	if row[6] =="married-civ-spouse":
		row[6] = "0"
	elif row[6] == "divorced":
		row[6] = "1"
	elif row[6] == "never-married":
		row[6] = "2"
	elif row[6] == "widowed":
		row[6] = "3"
	elif row[6] == "married-spouse-absent":
		row[6] = "4"
	elif row[6] == "married-af-spouse":
		row[6] = "5"

	if row[7] == "tech-support":
		row[7] = "0"
	elif row[7] == "craft-repair":
		row[7] = "1"
	elif row[7] == "other-service":
		row[7] = "2"
	elif row[7] == "sales":
		row[7] = "3"
	elif row[7] == "exec-managerial":
		row[7] = "4"
	elif row[7] == "prof-speciality":
		row[7] = "5"
	elif row[7] == "handlers-cleaners":
		row[7] = "6"
	elif row[7] == "machine-op-inspct":
		row[7] = "7"
	elif row[7] == "adm-clerical":
		row[7] = "8"
	elif row[7] == "framing-fishing":
		row[7] = "9"
	elif row[7] == "transport-moving":
		row[7] = "10"
	elif row[7] == "priv-house-serv":
		row[7] = "11"
	elif row[7] == "protective-serv":
		row[7] = "12"
	elif row[7] == "armed-forces":
		row[7] = "13"

	if row[8] == "wife":
		row[8] = "0"
	elif row[8] == "own-child":
		row[8] = "1"
	elif row[8] == "husband":
		row[8] = "2"
	elif row[8] == "not-in-family":
		row[8] = "3"
	elif row[8] == "other-relative":
		row[8] = "4"
	elif row[8] == "unmarried":
		row[8] = "5"
	
	if row[9] == "white":
		row[9] = "0"
	elif row[9] == "asian-pac-island":
		row[9] =="1"
	elif row[9] == "amer-indian-eskimo":
		row[9] =="2"
	elif row[9] == "black":
		row[9] =="3"
	
	if row[10] == "male":
		row[10] = "0"
	else:
		row[10] = "1"

	if row[14] == "united states":
		row[14] = "0"
	elif row[14] == "canada":
		row[14] = "1"
	elif row[14] == "england":
		row[14] = "2"
	elif row[14] == "cambodia":
		row[14] = "3"
	elif row[14] == "puerto-rico":
		row[14] = "4"
	elif row[14] == "germany":
		row[14] = "5"
	elif row[14] == "outlying-us":
		row[14] = "6"
	elif row[14] == "india":
		row[14] = "7"
	elif row[14] == "japan":
		row[14] = "8"
	elif row[14] == "greece":
		row[14] = "9"
	elif row[14] == "south":
		row[14] = "10"
	elif row[14] == "china":
		row[14] = "11"
	elif row[14] == "cuba":
		row[14] = "12"
	elif row[14] == "iran":
		row[14] = "13"
	elif row[14] == "honduras":
		row[14] = "14"
	elif row[14] == "phillippines":
		row[14] = "15"
	elif row[14] == "italy":
		row[14] = "16"
	elif row[14] == "poland":
		row[14] = "17"
	elif row[14] == "jamaica":
		row[14] = "18"
	elif row[14] == "vietnam":
		row[14] = "19"
	elif row[14] == "mexico":
		row[14] = "20"
	elif row[14] == "portugal":
		row[14] = "21"
	elif row[14] == "ireland":
		row[14] = "22"
	elif row[14] == "france":
		row[14] = "23"
	elif row[14] == "dominican-republic":
		row[14] = "24"
	elif row[14] == "laos":
		row[14] = "25"
	elif row[14] == "ecuador":
		row[14] = "26"
	elif row[14] == "taiwan":
		row[14] = "27"
	elif row[14] == "haiti":
		row[14] = "28"
	elif row[14] == "columbia":
		row[14] = "29"
	elif row[14] == "hungary":
		row[14] = "30"
	elif row[14] == "guatemala":
		row[14] = "31"
	elif row[14] == "nicaragua":
		row[14] = "32"
	elif row[14] == "scotland":
		row[14] = "33"
	elif row[14] == "thailand":
		row[14] = "34"
	elif row[14] == "yugoslavia":
		row[14] = "35"
	elif row[14] == "el-salvador":
		row[14] = "36"
	elif row[14] == "trinidad & tobago":
		row[14] = "37"
		elif row[14] == "peru":
		row[14] = "38"
	elif row[14] == "hong":
		row[14] = "39"
	elif row[14] == "holand-netherlands":
		row[14] = "40"
	
	
	