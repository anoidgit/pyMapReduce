#coding=utf-8

import sys

import zmq, json

import mapcore

mapfunc = mapcore.mapfunc

def loadServer(bindaddr):
	socket = zmq.Context().socket(zmq.REP)
	if not bindaddr.startswith("tcp://"):
		bindaddr = "tcp://"+bindaddr
	socket.bind(bindaddr)
	while 1:
		req = json.loads(socket.recv())
		if isinstance(req, str) or isinstance(req, unicode):
			if req.lower().startswith("term"):
				socket.send(json.dumps("EXIT"))
				break
		else:
			socket.send(json.dumps(mapfunc(req)))

if __name__ == "__main__":
	loadServer(sys.argv[1].decode("utf-8"))
