import random

numrep = 1
numpop = 10
percaff= 0.9
all=[[0,0]]*int((1-percaff)*numpop)+[[1,1]]*int(percaff*numpop)
aff=[0]*int((1-percaff)*numpop)+[1]*int(percaff*numpop)
car=[0]*int((1-percaff)*numpop)+[1]*int(percaff*numpop)
repr=[0]*1000

ctr=0
death=0

try:
	while(1):
		if len(all)==1:
			raise KeyboardInterrupt
		ctr+=1
		a=random.randint(0,len(all)-1)
		b=random.randint(0,len(all)-1)
		while b==a:
			b=random.randint(0,len(all)-1)
		p1=all[a]
		p2=all[b]
		p=[0,0]
		p[0]=p1[random.randint(0,1)]
		p[1]=p2[random.randint(0,1)]
		if p==[1,1]:
			affp=1;
		else:
			affp=0;
		if sum(p)>0:
			carp=1
		else:
			carp=0
		repr[a]+=1
		repr[b]+=1
		if (a<b):
			a,b=b,a
		if repr[a]>=numrep:
			death+=1
			del all[a]
			del aff[a]
			del car[b]
			del repr[a]
		if repr[b]>=numrep:
			death+=1
			del all[b]
			del aff[b]
			del car[b]
			del repr[b]
		all.append(p)
		aff.append(affp)
		car.append(carp)
		repr.append(0)
		
		print 'Percentage with recessive: {:.2f}; Percentage carriers: {:.2f}'.format(100.0*sum(aff)/len(aff),100.0*sum(car)/len(car))
except KeyboardInterrupt:
	print
	print 'Number of iterations:', ctr
	print
	print 'Number of people:', len(all)
	print 'Number of deaths:', death
	print 'Number of affected:', sum(aff)
	print 'Number of carriers:', sum(car)
	print
	print 'Number of non-affected carriers:', sum(car)-sum(aff)
	print 'Percentage of affected:',100.0*sum(aff)/len(aff)
	print 'Percentage of carriers:',100.0*sum(car)/len(car)
	print 'Percentage of non-affected carriers:',100.0*(sum(car)-sum(aff))/len(car)
	