import numpy as np
a=np.load('gain.npy',allow_pickle=True)
for i in a:
    for j in i:
        for k in ['prevLV','nextLV','exp']:
            if k in i[j]:
                del i[j][k]
for idx,i in enumerate(a):
    if i!={}:
        print(idx+1,i)