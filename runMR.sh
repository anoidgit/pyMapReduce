#!/bin/bash

export srcfile=weibo.txt
export rsfile=segrs.txt

export cachebatch=72
export batchperunit=36
export nthreads=6

#if you want to use pypy, use py rather than pyo
python -O -m py_compile *.py 

python mapper.pyo 127.0.0.1:20001 &
python mapper.pyo 127.0.0.1:20002 &
python mapper.pyo 127.0.0.1:20003 &
python mapper.pyo 127.0.0.1:20004 &
python mapper.pyo 127.0.0.1:20005 &
python mapper.pyo 127.0.0.1:20006 &

python reducer.pyo $srcfile $rsfile $cachebatch $batchperunit $nthreads 127.0.0.1:20001 127.0.0.1:20002 127.0.0.1:20003 127.0.0.1:20004 127.0.0.1:20005 127.0.0.1:20006

# Warning: this command will kill all python process, better comment it
#pkill python
