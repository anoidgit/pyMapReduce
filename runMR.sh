#!/bin/bash

#if you want to use pypy, use py rather than pyo
python -O -m py_compile *.py 

python mapper.pyo 127.0.0.1:20001 &
python mapper.pyo 127.0.0.1:20002 &
python mapper.pyo 127.0.0.1:20003 &
python mapper.pyo 127.0.0.1:20004 &
python mapper.pyo 127.0.0.1:20005 &
python mapper.pyo 127.0.0.1:20006 &

python reducer.pyo weibo.txt segrs.txt 128 32 6 127.0.0.1:20001 127.0.0.1:20002 127.0.0.1:20003 127.0.0.1:20004 127.0.0.1:20005 127.0.0.1:20006

# Warning: this command will kill all python process, better comment it
#pkill python
