#!/bin/bash

python mapper.py 0.0.0.0:20001 &
python mapper.py 0.0.0.0:20002 &
python mapper.py 0.0.0.0:20003 &
python mapper.py 0.0.0.0:20004 &

python reducer.py weibo.txt segrs.txt 64 64 1 127.0.0.1:20001 0.0.0.0:20002 127.0.0.1:20003 0.0.0.0:20004 &
