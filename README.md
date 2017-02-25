# Python
# My python to analyze text

def make_length_wordcount(file_name):
	with open(file_name,'r') as infile:
		len_count=dict()
		word_count=infile.read().lower().split()
		for word in word_count:
			length=len(word)
			if length in len_count:
				len_count[length]+=1
			else:
				len_count[length]=1
	return len_count
# Q.3:
def make_word_count(file_name):
	with open(file_name,'r') as infile:
		type_count=dict()
		word_count=infile.read().lower().split()
		for word in word_count:
			if word in type_count:
				type_count[word]+=1
			else:
				type_count[word]=1
	return type_count
# Q.4:
def analyze_text(file_name):
	with open(file_name,'r') as infile:
		word_list=infile.read().lower().split()
		file_name1=file_name[:-4]
	outfile =open(file_name1+'_analyzed_NIRANJAN_NAIK.txt','w')
	len1=make_length_wordcount(file_name)
	wor1=make_word_count(file_name)
	for i, j in sorted(len1.items()):
		outfile.write('Words of length ' + str(i) + ' : ' + str(j) + '\n')
	for m, n in sorted(wor1.items()):
		outfile.write(str(m) + ' : ' + str(n) + '\n')
