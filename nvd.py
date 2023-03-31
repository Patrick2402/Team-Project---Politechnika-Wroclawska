#! /usr/bin/env python3
import os
import requests
import json
import zipfile
from collections import OrderedDict, Counter
from datetime import datetime, timedelta
import os
import time
import urllib.request


		



class CVE_item():
	def __init__(self,cve_item):
		self.raw = (cve_item)
		self.ID = cve_item['cve']['CVE_data_meta']['ID'] # ID - string 
		self.description = cve_item['cve']['description']["description_data"][0]["value"] # opis -string
		datetime_object = datetime.strptime(cve_item["publishedDate"], '%Y-%m-%dT%H:%MZ')
		self.publishedDate = datetime_object # data opublikowania - datetime.datetime
		self.score2 = '' 	# ocena podatności cvss 2.0 - float
		self.score3 = '' 	# ocena podatności cvss 3.1 - float
		self.severity2 = '' # kategorii klasyfikacji cvss 2.0: low, medium, high - string
		self.severity3 = '' # kategorii klasyfikacji cvss 3.1 : low, medium, high, critical, niektóre 3.1 mają klasyfikacje z cvss 2.0 - string

		for key in ['baseMetricV2', 'baseMetricV3']:
			if key in cve_item["impact"]:
				try:
					if key == 'baseMetricV2':
						self.score2 = float(cve_item["impact"][key]['impactScore'])
						self.severity2 = cve_item["impact"][key]["severity"]
		
					elif key == 'baseMetricV3':
						self.score3 = float(cve_item["impact"][key]['impactScore'])
						self.severity3 = cve_item['impact']['baseMetricV3']['cvssV3']['baseSeverity']
				except:
					pass
	def __str__(self):
		return ' ID: {},\n Description: {},\n Published date: {},\n Score 2: {},\n Score 3: {},\n Severity 2: {},\n Severity 3: {}'.format( \
			self.ID, \
			self.description,\
			self.publishedDate,\
			self.score2,\
			self.score3,\
			self.severity2,\
			self.severity3\
			)

def parse_NVD_CVE_files(year):

	cwd = os.getcwd()
	path = r"nvdcve-1.1-" + str(year) + ".json"
	path_to_json_file = os.path.join(cwd,path)

	cve_items = dict()

	with open(path_to_json_file, encoding="utf-8") as json_file:
		print('Parsing file {}'.format(path_to_json_file))
		cve_data = json.load(json_file)
		CveEntry_list = [CVE_item(cve_dict) for cve_dict in cve_data['CVE_Items']]
		return CveEntry_list		

def extract_ZIP_files(directory=os.getcwd()):
	if not os.path.isdir(directory):
		print('Directory {} does not exist!'.format(directory))
		return list()
	
	zip_file_count = 0
	for my_file in os.listdir(directory):
		if my_file.lower().endswith('.zip'):
			if not os.path.isfile(my_file.lower()[:-4]):
				path_to_zip_file = os.path.join(directory, my_file)
				zip_file_count += 1
				print('Extracting ZIP file {}: {}'.format(zip_file_count, path_to_zip_file))
				try:
					with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
						zip_ref.extractall()

				except Exception as e:
					print('FAILED to extract ZIP file: {}'.format(path_to_zip_file))
					print(e)

   
def download_NVD_CVE_files(directory=os.getcwd()):
   
	year = 2002
	for i in range(0,21):
		url = r"https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-20xx"
		url = url[:-4] + str(year) + ".json.zip"
		year+=1
		
		local_filename = os.path.join(directory, url.split('/')[-1])

		if not os.path.isfile(local_filename):
			download_remote_file(url, local_filename)

				

def download_remote_file(url, local_filename):
	if not '/' in url:
		print('No URL provided!')
		return None
	print("Downloading: ",url)
	# try to download the file
	try:
		urllib.request.urlretrieve(url, local_filename)
		return local_filename
	except Exception as e:
		print('FAILED to download URL: {}'.format(url))
		print(e)
	
	return None

def main():

	download_NVD_CVE_files()  # pobiera zipy plików json, jeden plik na rok, rok 2002 posiada wszystkie od 1988-2002   
	extract_ZIP_files() #rozpakowuje zipy, które nie zostały jeszcze odpakowane
	
	######### Od tego miejsca można zmieniać co się chce, w ramach funkcji main ###########

	objc = parse_NVD_CVE_files("2002") # zwraca liste, której każdy element to pojedyńcza podatność z podanego roku, argument od 2002-2022 zakładając istnienie plików (2 poprzednie funkcje)

	print(objc[0])  # wypsiuje wszystkie informacje jakie zostały sparsowane (parser parsuje tylko informacje potrzebne do wykonania projektu)
	

"""

	objc[0] - pierwsza podatność
	objc[1] - druga podatność

	print(len(objc)) - liczba podatności dla danego roku

	
	Dostęp do poszczególnych danych, pierwszej podatności dla danego roku

	objc[0].ID 				
	objc[0].description 	
	objc[0].publishedDate	
	objc[0].score2			 
	objc[0].score3
	objc[0].severity2
	objc[0].severity3
	
	objc[0].raw - surowe dane podatności w formacie json

"""

if __name__ == '__main__':
	main()
