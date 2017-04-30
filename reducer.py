#coding=utf-8

import sys

import zmq, json

import threading

import reducecore

getio = reducecore.getio

def decodelist(lin, decm="utf-8"):
	return [lu.decode(decm) for lu in lin]

def trand(lin):
	curid = 0
	rs = {}
	for lu in lin:
		rs[curid] = lu
		curid += 1
	return rs

def tranl(din):
	rs = []
	for i in xrange(len(din)):
		rs.extend(din[i])
	return rs

def starthread(func, argv, run=True):
	t = threading.Thread(target=func, args=argv)
	t.setDaemon(True)
	if run:
		t.start()
	return t

def infgen(lin):
	while True:
		for lu in lin:
			yield lu

def getsocket(serv):
	if not serv.startswith("tcp://"):
		serv = "tcp://"+serv
	socket = zmq.Context().socket(zmq.REQ)
	socket.connect(serv)
	return socket

def getsockets(servl):
	return [getsocket(servu) for servu in servl]

def processUnit(socket, data):
	socket.send(json.dumps(data))
	return json.loads(socket.recv())

def sendTERM(connect):
	return processUnit(connect, "TERM")

def loadcache(reader, bubsize, bsize):
	rs=[]
	cache=[]
	curldrs=0
	curldcache=0
	for ru in reader:
		cache.append(ru)
		curldcache += 1
		if curldcache == bubsize:
			rs.append(cache)
			cache = []
			curldcache = 0
			curldrs += 1
			if curldrs == bsize:
				yield rs
				rs = []
				curldrs = 0
	if rs:
		if cache:
			rs.append(cache)
		yield rs

def writecache(writer, cache):
	for cu in cache:
		writer.write(cu)

def oneReducer(mapperl):
	global srccache, rscache, idlck, idpool, runsgn
	while runsgn:
		if idpool:
			with idlck:
				if idpool:
					doid = idpool.pop()
					rscache[doid] = processUnit(mapperl.next(), srccache[doid])

def saver(writer):
	global wcache, runsgn
	while runsgn:
		if wcache:
			writecache(writer, wcache)
			print wcache
			wcache = []

def cacheManager(reader, writer, bsize, bubsize, connects):
	global srccache, rscache, idpool, nsavd, wcache, runsgn
	for cache in loadcache(reader, bubsize, bsize):
		rscache = {}
		srccache = trand(cache)
		lsrc = len(cache)
		idpool = set([i for i in xrange(lsrc)])
		while len(rscache) != lsrc or wcache:
			pass
		wcache = tranl(rscache)
	writer.close()
	for connect in connects:
		sendTERM(connect)
	runsgn = False
	sys.exit()

def startCacheManager(reader, writer, bsize, bubsize, connects):
	return [starthread(cacheManager, (reader, writer, bsize, bubsize, connects)), starthread(saver, (writer,))]

def startReduce(mapperc):
	return starthread(oneReducer, (mapperc,))

def loadReducer(args):
	global runsgn
	srcdf, rsdf = args[:2]
	reader, writer = getio(srcdf, rsdf)
	bsize, bubsize, nthread = [int(i) for i in args[2:5]]
	connects = getsockets(args[5:])
	mappers = infgen(connects)
	tpool = []
	tpool.extend(startCacheManager(reader, writer, bsize, bubsize, connects))
	for i in xrange(nthread):
		tpool.append(startReduce(mappers))
	while runsgn:
		pass

if __name__ == "__main__":
	srccache = {}
	idpool = set()
	rscache = {}
	wcache = []
	idlck = threading.Lock()
	runsgn = True
	loadReducer(decodelist(sys.argv[1:]))
