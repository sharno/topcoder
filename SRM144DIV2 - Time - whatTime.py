class Time:
	def whatTime(self, seconds):
		h = seconds / 3600
		m = (seconds / 60) % 60
		s = seconds % 60 % 60
		return str(h)+":"+str(m)+":"+str(s)



time = Time()
print time.whatTime(5436)
