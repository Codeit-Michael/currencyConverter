def convertion_list(lst=list):
	# takes a list of object and convert it into tuples
	new_list = []
	for x in lst:
		tp = (x,x)
		new_list.append(tp)
	return new_list

