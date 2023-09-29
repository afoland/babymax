import numpy as np
import pickle

words = []
idx = 0
word2idx = {}
# vectors = bcolz.carray(np.zeros(1), rootdir=f'{glove_path}/6B.50.dat', mode='w')


vecwords=400000
# vecdims=200
vecdims=211

# 840B
# vecwords=2200000
# vecdims=300

#vectors=np.zeros(vecdims);

vectors=np.zeros(vecdims*vecwords)

print(vectors)

with open(f'./data/glove/glove.6B.211d.txt', 'rb') as f:
    for l in f:
        line = l.decode().split()
        word = line[0]
        words.append(word)
        word2idx[word] = idx
        idx += 1
        vect = np.array(line[1:]).astype(np.float)
#        vectors=np.append(vectors,vect)
        idxb=vecdims*(idx-1)
        idxe=vecdims*idx-1
        idxve=vecdims-1
        vectors[vecdims*(idx-1):(idx*vecdims)]=vect[0:(vecdims)]
#        vectors[idxb:idxe]=vect[0:idxve]
        if idx == 1:
            print('Index: ',idx)
            print('Word: ',word)
            print('Vect: ',vect)
            print('Vect: ',vect[0:200])
            print('Vect 199: ',vect[199])
            print('Vectors: ',vectors[idxb:idxe])
            print('Vectors: ',vectors[0:200])
            print('Size of vect: ',len(vect))

print('End of Reading')

print('Vector 199: ',vectors[199])
print('Vector 399: ',vectors[399])

vectors = vectors[0:].reshape(vecwords, vecdims)
print('End of Reshaping')
print('Checking last column')
print('Vector word 1 column 200: ',vectors[0][199])
print('Vector word 1 column last: ',vectors[0][-1])
print('Vector word 2 column 200: ',vectors[1][199])
print('Vector word 2 column last: ',vectors[1][-1])
print('Vectors last column: ',vectors[:,199])
pickle.dump(vectors, open(f'./data/glove/6B.211_vecs.pkl', 'wb'))
print('Pickled Vectors')
pickle.dump(words, open(f'./data/glove/6B.211_words.pkl', 'wb'))
print('Pickled Words')
pickle.dump(word2idx, open(f'./data/glove/6B.211_idx.pkl', 'wb'))
print('Pickled Word2Idx')

