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
	while True:
		socket.send(json.dumps(mapfunc(json.loads(socket.recv()))))

if __name__ == "__main__":
	loadServer(sys.argv[1].decode("utf-8"))
