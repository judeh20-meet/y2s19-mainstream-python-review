# Part 2 of the Python Review lab.
def prime(x,y):
	if x < 1:
		return "Invalid input: Outside range"
	else:
		for i in range(2,x):
			if i % 2 ==0:
				for i in range(2,y):
					if i % 2 ==0:
						return(x,y)
					else:
						y+=1 
			else:
				x+=1

def encode(x, y):

	if 1 < y < 250 and 500 < x < 1000:
		if prime(x,y):
		
			return(x*y)
		else:
			pass

	else:
		print("Invalid input: Outside range")

		return(None)


def decode(coded_message):
	pass	

