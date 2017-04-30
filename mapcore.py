#coding=utf-8

from thulac import thulac

segger = thulac(deli='/')

def segline(strin):
	global segger
	try:
		tmp = tmp.encode("utf-8")
		tmp = segger.cut(tmp, text=True)
		rs = tmp.decode("utf-8")
	except:
		rs = u""
	return rs

def mapfunc(bin):
	rs = []
	for bu in bin:
		tmp = segline(bu)
		if bu:
			rs.append(bu)
	return rs
