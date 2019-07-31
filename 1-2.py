import re
import string
import time
import threading

# Create dictionaries
frequency = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8+":0}
frequency2 = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8+":0}

# Remove undesireable characters and count word lengths
def cleanAndCount(text_string, frequency):
	match_pattern = re.sub("[^a-zA-Z0-9_-]+", " ",text_string)
	words = match_pattern.split()

	# Count characters in the words
	for word in words:
		#word is a single word of len n
		wordLen = len(word)
		if wordLen < 8:
			frequency[str(wordLen)] += 1
		else:
			frequency["8+"] += 1

# Main function		
def main():
	
	# Open 1/2 document created from enwik9.txt
	document_text = open('thetext1.txt', 'r')
	text1 = document_text.read()
	# Open 2/2 document created from enwik9.txt
	document_text2 = open('thetext2.txt', 'r')
	text2 = document_text2.read()

	# Create threads to handle parsing 1/2 & 2/2 documents individually
	thread1 = threading.Thread(target = cleanAndCount, args = (text1, frequency))
	thread2 = threading.Thread(target = cleanAndCount, args = (text2, frequency2))

	# Start thread work
	thread1.start()
	thread2.start()

	# Join threads
	thread1.join()
	thread2.join()

	# Join the keys of the frequency dictionaries, i.e. word frequency counts, because they were split up into two separate files
	for key in frequency2:
		frequency[key] += frequency2[key]

	# Get total amount of word frequencies
	total = 0     
	for key in frequency:
		total += frequency[key]

	# Print the word frequencies
	for key in frequency:
		print (key, "letter-", frequency[key], "words,", (frequency[key] * 100.0/total), "%")

if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))