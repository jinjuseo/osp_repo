#!/usr/bin/python3
def conversion():
	user_input=int(input("input binary number : "))
	str_user_input = str(user_input)
	result =0
	
	for i in range(len(str(user_input))):
		result = ((user_input%(10**(i+1)))//(10**i))*(2**i) + result
	o = format(result,'o')
	h = format(result,'X')
	#h = hex(result)
	print("=> OCT> {0}".format(o))
	print("=> DEC> {0}".format(result))
	print("=> HEX> {0}".format(h))
	

if __name__== '__main__':
	print("this is conversion module")


