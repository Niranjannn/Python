#Group 12: Niranjan Naik, Anurag Patil, Dhaval Metre
# Code to extract unique images for android and ios 

#import pakages
from bs4 import BeautifulSoup
import json
import os
from lxml import html
#Define file path
folder = r'C:\Users\Niranjan Naik\Desktop\pokemon_5378\data'
#json file used to load the data
outfile = open('image.json', 'w')
image1=set()
image=[]
image2=[]
ix1=[]
#open directory
for dirName, dirs, files in os.walk(folder):

	print("directory name---->>>>",dirName)

	for fileName in files:

        #android images select
		if 'android' in fileName :
			print("inside android---->>>>",fileName)
			soup = BeautifulSoup(open(dirName + '/' + fileName), 'lxml')
			image=soup.find_all("img",class_="screenshot")
			for i in image:
				image1.add(i.get('src'))
		#ios images select
		if 'ios' in fileName:
			print("inside ios---->>>>",fileName)
			soup = BeautifulSoup(open(dirName + '/' + fileName), 'lxml')
			image2=soup.find_all("img",class_="portrait")
			for i in image2:
				image1.add(i.get('src'))
		
#dump the data into json
json.dump(list(image1), outfile,indent=4)

