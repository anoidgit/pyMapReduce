#coding=utf-8

import sys

import zmq, json

from mrmethods import mapcore

def loadServer(bindaddr):
	socket = zmq.Context().socket(zmq.PUB)
	socket.bind(bindaddr)
	while True:
		socket.send(json.dumps(mapcore(json.loads(socket.recv()))))

if __name__ == "__main__":
	loadServer(sys.argv[1].decode("utf-8"))
