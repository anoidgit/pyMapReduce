#coding=utf-8

class fwrter:
	
	def __init__(self, fname):
		self.f = open(fname, "wb")

	def write(self, wrtd):
		self.f.write(wrtd.encode("utf-8","ignore"))
		self.f.write("\n")

	def close(self):
		self.f.close()

def buildreader(fname):
	with open(fname, "rb") as frd:
		for line in frd:
			tmp = line.strip()
			if tmp:
				rs = False
				try:
					rs = tmp.decode("utf-8")
				except:
					pass
				if rs:
					yield rs

def getio(srcdf, rsdf):
	return buildreader(srcdf), fwrter(rsdf)
