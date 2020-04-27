#!/usr/bin/python3
def union_intersect():
	lines_1st = input("1st list: ")
	lines_2nd = input("2nd list: ")
	
	list_1st=[]
	list_2nd=[]
	
	marks=[',','[',']']
	for mark in marks:
		lines_1st = lines_1st.replace(mark,' ')
		lines_2nd = lines_2nd.replace(mark,' ')

	for i in lines_1st.split():
		list_1st.append(int(i))
	for i in lines_2nd.split():
		list_2nd.append(int(i))

	#print(list_1st)
	#print(list_2nd)

	"""union=[]
	intersection=[]
	for i in list_1st:
		for j in list_2nd:
			if i == j:
				if j not in intersection:
					intersection.append(j)
				if j not in union:
					union.append(j)
			else:
				if j not in union:
					union.append(j)
		if i not in union:
			union.append(i)"""
	set1 = set(list_1st)
	set2 = set(list_2nd)
	
	#union.sort()
	#intersection.sort()
	"""print("=> union [",end='')
	for i in range(len(union)):
		if i==0:
			print("{0}".format(union[i]),end='')
		else:
			print(",{0}".format(union[i]),end='')
	print("]")
	
	print("=> intersection [",end='')
	for i in range(len(intersection)):
		if i==0:
			print("{0}".format(intersection[i]),end='')
		else:
			print(",{0}".format(intersection[i]),end='')
	print("]")
	"""
	union = list(set1|set2)
	intersection = list(set1&set2)
	print("=> union {0}".format(union))
	print("=> intersection {0}".format(intersection))




if __name__== '__main__':
	print("this is union/intersection module")

