class BinaryCode:
	def decode(self, message):
		message = [int(i) for i in message]

		x = [0]
		for i in range(len(message)):
			if i==0:
				e = message[i]-x[i]
			else:
				e = message[i]-x[i]-x[i-1]
			#last element subtraction should be 0
			if e not in [0,1] or (i==len(message)-1 and e!=0):
				x = "NONE"
				break
			# don't add last element because it was just a check for correctness
			if i<len(message)-1:
				x.append(e)
		x = "".join([str(i) for i in x])

		y = [1]
		for i in range(len(message)):
			if i == 0:
				e = message[i]-y[i]
			else:
				e = message[i]-y[i]-y[i-1]
			#last element subtraction should be 0
			if e not in [0,1] or (i==len(message)-1 and e!=0):
				y = "NONE"
				break
			# don't add last element because it was just a check for correctness
			if i<len(message)-1:
				y.append(e)
		y = "".join([str(i) for i in y])

		return (x, y)



bin = BinaryCode()
print bin.decode("1")
