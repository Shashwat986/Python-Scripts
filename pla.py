# Perceptron learning algorithm

import random

def getpt():
	x=random.random()*2-1
	y=random.random()*2-1
	return [x,y]

def sign(k):
	if k >=0:
		return 1
	else:
		return -1

# y=((y2-y1)/(x2-x1))*(x-x1) + y1

N=100
iterations = 1000
avg=0
pravg=0
for _ in range(iterations):
	[x1,y1]=getpt()
	[x2,y2]=getpt()
	train=[]
	for n in range(N):
		[x,y]=getpt()
		if y - y1 >= ((y2-y1)/(x2-x1))*(x-x1):
			v = 1
		else:
			v = -1
		#print y - y1 >= ((y2-y1)/(x2-x1))*(x-x1)
		train.append([[1,x,y],v])
	w=[0,0,0]
	ctr=0
	while 1:
		flag = 0
		ctr += 1
		b=range(len(train))
		random.shuffle(b)
		#print b
		for i in b:
			ele=train[i]
			#print ele
			[kx0,kx1,kx2] = ele[0]
			if sign(kx0*w[0]+kx1*w[1]+kx2*w[2]) != ele[1]:
				w[0]=w[0]+ele[1]*kx0
				w[1]=w[1]+ele[1]*kx1
				w[2]=w[2]+ele[1]*kx2
				flag = 1
				break
		if flag == 0:
			break
		if ctr >= 10000:
			break
	#print ctr
	prctr=0.0
	for __ in range(1000):
		[tx,ty]=getpt()
		if sign(1*w[0]+tx*w[1]+ty*w[2]) != sign((ty - y1) - ((y2-y1)/(x2-x1))*(tx-x1)):
			prctr+=1
	prctr=prctr/1000
	pravg+=prctr
	avg+=ctr

print "The average number of iterations:", (avg/iterations)
print "The average bad probability:", (pravg/iterations)