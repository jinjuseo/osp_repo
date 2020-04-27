#!/usr/bin/python3
import my_pkg

if __name__== '__main__':
	
	while True:
		n=int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
		if n==1:
			my_pkg.conversion()
		elif n==2:
			my_pkg.union_intersect()
		elif n==3:
			print("exit the program...")
			break

		
		

	
