#Euopean passport problem -1
from hashlib import sha1
def get_sha_1(seed):
	sha1Obj = sha1()
	sha1Obj.update(seed)
	return sha1Obj.hexdigest()
def alter(A):
	a = []
	a.append([bin(int(b,16)).count('1') for b in [A[i:i+2] for i in range(0, len(A), 2)]])
	print a

inf = '12345678<811101821111167'
kseed = get_sha_1(inf)[0:32]+'00000001'
print "kseed = " + kseed + '\n'

D = ''.join([chr(int(b, 16)) for b in [kseed[i:i+2] for i in range(0, len(kseed), 2)]])       #decode hex
print kseed.decode("hex")==D
result = get_sha_1(D)
ka = result[0:16]
kb = result[16:32]
print "ka = "+ka+'\n'
print "kb = "+kb+'\n'
a = []
a.append([bin(int(b,16)) for b in [kb[i:i+2] for i in range(0, len(kb), 2)]])
print a
a = []
a.append([bin(int(b,16)).count('1') for b in [kb[i:i+2] for i in range(0, len(kb), 2)]])
print a

print "After edit"
ka = 'ea8645d97ff725a8'
print "ka = "+ka+'\n'
kb = '98942aa280c43179'
print "ka = "+kb+'\n'
