class BinaryCode:
	def decode(self, message):
		if len(message) <= 1:
			return ("NONE", "NONE")
		message = [int(i) for i in message]

		x = [0, message[0]]
		for i in range(1, len(message)):
			e = message[i]-x[i]-x[i-1]
			if e not in [0,1]:
				x = "NONE"
				break
			# don't add last element because it was just a check for correctness
			if i<len(message)-1:
				x.append(e)
		x = "".join([str(i) for i in x])

		y = [1, message[0]-1]
		for i in range(1, len(message)):
			e = message[i]-y[i]-y[i-1]
			if e not in [0,1]:
				y = "NONE"
				break
			# don't add last element because it was just a check for correctness
			if i<len(message)-1:
				y.append(e)
		y = "".join([str(i) for i in y])

		return (x, y)



bin = BinaryCode()
print bin.decode("123210122")
