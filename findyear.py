import csv
import sys

def find_year(input_file):
	name_list = create_list(input_file)
	year_list = []
	highest_year = [0,0]
	
	for x in xrange(1900, 2000):
		alive_count = 0
		year = [x]
		for y in name_list:
			temp_birth = int(y[1])
			temp_death = int(y[2])
			if (x >= temp_birth and x <= temp_death):
				alive_count+=1
		year.append(alive_count)
		year_list.append(year)
		if (alive_count > highest_year[1]):
			highest_year=year
	
	
	print "The highest number of people alive in any one year is " + str(highest_year[1]) + " which occured in the following years:"
	for n in year_list:
		temp_num_alive = n[1]
		if (temp_num_alive == highest_year[1]):
			print n[0]
	
	export_years_list(year_list)

def create_list(csv_file_name):
	output_list = []
	
	input_file = open(csv_file_name, "rb")
	reader = csv.reader(input_file)
	hdr_chk = open(csv_file_name, "rb")
	has_header = csv.Sniffer().has_header(hdr_chk.read(2048))
	
	for row in reader:
		output_list.append(row)
	
	output_list = check_list(output_list, has_header)
	return output_list

def check_list(array_of_names, hdr_status):
	
	new_list = []
	for temp_array in array_of_names:
		if (hdr_status):
			hdr_status = False
		else:
			birth_year = int(temp_array[1])
			death_year = int(temp_array[2])
			if (birth_year >= 1900 and birth_year <= 2000 and death_year >= 1900 and death_year <= 2000):
				new_list.append(temp_array)
			else:
				print "Found an invalid entry."
	return new_list

def export_years_list(list_of_years):
	exported_list = [['YEAR', 'NUMBER OF PEOPLE ALIVE']]
	for r in list_of_years:
		exported_list.append(r)
	new_csv_file = open('output.csv', 'wb')
	csv_writer = csv.writer(new_csv_file, delimiter=',')
	for s in exported_list:
		csv_writer.writerow(s)
	print "output.csv has been created.  It is a comma seperated file that contains every year, and the number of people from the original list that is alive during that year."

if __name__ == '__main__':
	find_year(sys.argv[1])