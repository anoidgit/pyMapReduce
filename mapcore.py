#coding=utf-8

from thulac import thulac

segger = thulac(deli='/')

def segline(strin, segger):
	try:
		tmp = strin.encode("utf-8")
		tmp = segger.cut(tmp, text=True)
		rs = tmp.decode("utf-8")
	except:
		rs = u""
	return rs

def mapfunc(bin):
	global segger
	rs = []
	for bu in bin:
		tmp = segline(bu, segger)
		if tmp:
			rs.append(tmp)
	return rs
