import csv


# get dictionary of unique characters
# count # unique chars in entire dataset 
def get_char_vocabulary(filepath, dictionary, total_char, datatype, access_type, token_type):
	dt = "{}_message".format(datatype)

	with open(filepath, access_type) as csvfile:
		reader = csv.DictReader(csvfile)
		for status in reader:
			if dt not in status:
				# 2 rows are being read at a time for the statuses csv for some reason...
				# handled with monkey patching below
				# print status.items()
				msg1, msg2 = status.items()[1]
				# print msg1
				# print msg2

				for char in msg1:
					dictionary.add(char)
					total_char += 1
				for char in msg2:
					dictionary.add(char)
					total_char += 1
			else:
				msg = status[dt]
				# print msg 
				for char in msg:
					dictionary.add(char)
					total_char += 1

	print 'Dictionary of len', len(dictionary), 'is', dictionary
	print 'Total characters in {} dataset is'.format(token_type), total_char
	return dictionary, total_char

# dictionary, total_char = get_char_vocabulary("CUSTOM_NAMES/custom_name_token_comments.csv", set([]), 0, "comment", "rU", "CUSTOM_NAMES")
# dictionary, total_char = get_char_vocabulary("beaverconfessions_facebook_statuses.csv", dictionary, total_char, "status", "r", "CUSTOM NAMES")

dictionary, total_char = get_char_vocabulary("FILTERED_NAMES/filtered_names_comments.csv", set([]), 0, "comment", "rU", "filtered names")
dictionary, total_char = get_char_vocabulary("beaverconfessions_facebook_statuses.csv", dictionary, total_char, "status", "r", "filtered names")
