# pyMapReduce
Python parallelization like MapReduce.

There is a example for Chinese word segmentation with thulac,
To use this framework, you need to:
1: implement `mapfunc`(process a batch of data) in `mapcore.py` and `getio`(see the example for details) in `reducecore.py`;
2: change `runMR.sh` to feed your requirement(number of threads, etc.);
3: execute `runMR.sh` to start the MapReduce Procedure.

These code can work now, but not strong enough.
