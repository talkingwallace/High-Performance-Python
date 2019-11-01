
# %load_ext memory_profiler
# %memit [0]*int(1e8) # 索引有8字节指向0对象
# %memit [i for i in range(0,int(1e8))]
# %memit
# default int type takes about 3G memory


import array
# %memit array.array('i',range(int(1e8)))
# 670 MB only
