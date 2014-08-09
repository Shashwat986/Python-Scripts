#-------Assignment 2-------#
#        Question 1        #
#--------------------------#
# By:-                     #
#    Panchajanya Banerjee  #
#    and                   #
#    Shashwat Chandra      #
#--------------------------#

from __future__ import division
from scipy.interpolate import splev, splrep
import numpy as np
import pylab as pl
from math import sqrt
import httplib

a_v = 15.5
a_s = 16.8
a_c = 0.72
a_sym = 23
a_p = 34

def eps(A, Z):
    if A%2!=0:
        return 0
    elif A%2==0:
        if np.floor(Z)%2 ==0:
            return 1
        else:
            return -1
            
eps = np.vectorize(eps)


def oldB(A, Z, fix_eps=None):
    if fix_eps==None:
        return a_v*A - a_s*A**(2/3) - a_c*Z*(Z-1)*A**(-1/3) - a_sym*(A-2*Z)**2/A + eps(A, Z)*a_p*A**(-3/4)
    elif fix_eps==1:
        return a_v*A - a_s*A**(2/3) - a_c*Z*(Z-1)*A**(-1/3) - a_sym*(A-2*Z)**2/A + fix_eps*a_p*A**(-3/4)
    elif fix_eps==-1:
        return a_v*A - a_s*A**(2/3) - a_c*Z*(Z-1)*A**(-1/3) - a_sym*(A-2*Z)**2/A + fix_eps*a_p*A**(-3/4)


print "Welcome to the Awesome program made by us"
print
#------------------------------
inc=0.0
flag=[0]*5

print "Select the options you want:"
f=raw_input("1) Include the volume term?")
if f[0]=='y' or f[0]=='Y':
    flag[0]=1
f=raw_input("2) Include the surface term?")
if f[0]=='y' or f[0]=='Y':
    flag[1]=1
f=raw_input("3) Include the coulomb term?")
if f[0]=='y' or f[0]=='Y':
    flag[2]=1
f=raw_input("4) Include the asymmetry term?")
if f[0]=='y' or f[0]=='Y':
    flag[3]=1
f=raw_input("5) Include the pairing term?")
if f[0]=='y' or f[0]=='Y':
    flag[4]=1

print flag #flag[i] tells us if the i'th term should be included or not

def B(A,Z,fix_eps=None):
    inc=0.0
    if flag[0]==1:
        inc+=a_v*A
    if flag[1]==1:
        inc-=a_s*A**(2/3)
    if flag[2]==1:
        inc-=a_c*Z*(Z-1)*A**(-1/3)
    if flag[3]==1:
        inc-=a_sym*(A-2*Z)**2/A
    if fix_eps==None:
        inc+=eps(A, Z)*a_p*A**(-3/4)
    elif fix_eps==1:
        inc+=fix_eps*a_p*A**(-3/4)
    elif fix_eps==-1:
        inc+=fix_eps*a_p*A**(-3/4)
    return inc

#-----------------------------------------
print "Answer to part 1:"
A0 = 1
A1 = 250
dA = 1
A = np.arange(A0, A1, dA)           #array from A0 to A1 step dA
Z = (A + 0.00776*A**(2/3))/(1.98+0.0155*A**(2/3))   #calc Z(A)

pl.figure()
pl.plot(A, B(A, Z)/A, 'o-')         #plots B v.s. A
pl.grid()
pl.xticks(np.arange(A[0], A[-1], 10))       #x-axis values

#--------------------------
print "Answer to part 2:"

fixed_A=int(input("Enter fixed value of A for the rest of the code:"))

fZ = int((fixed_A + 0.00776*fixed_A**(2/3))/(1.98+0.0155*fixed_A**(2/3)))
print fixed_A,fZ

if flag[0]==1:
    print "Volume factor contribution:", (a_v*fixed_A)/oldB(fixed_A,fZ)
if flag[1]==1:
    print "Surface factor contribution:", (a_s*fixed_A**(2/3))/oldB(fixed_A,fZ)
if flag[2]==1:
    print "Coulomb factor contribution:", (a_c*fZ*(fZ-1)*fixed_A**(-1/3))/oldB(fixed_A,fZ)
if flag[3]==1:
    print "Asymmetry factor contribution:", (a_sym*(fixed_A-2*fZ)**2/fixed_A)/oldB(fixed_A,fZ)
if flag[4]==1:
    print "Pairing factor contribution:", (eps(fixed_A, fZ)*a_p*fixed_A**(-3/4))/oldB(fixed_A,fZ)


pl.figure()
#fixed_A = 128                  #fix A
Zmin = fZ - 8 #+-8 since we are looking at 2 alpha decay modes
Zmax = fZ + 9
Z = np.arange(Zmin, Zmax, 1)            #Z ranges from 52-10 to 52+10 (incl)
tck_even = splrep(Z[0::2], -B(fixed_A, Z[0::2], fix_eps=1)/fixed_A)
tck_odd = splrep(Z[1::2], -B(fixed_A, Z[1::2], fix_eps=-1)/fixed_A)

Z_fine = np.arange(Zmin, Zmax, 0.001)
pl.plot(Z, -B(fixed_A, Z)/fixed_A, 'o')
pl.plot(Z_fine, splev(Z_fine, tck_even), color='green')
pl.plot(Z_fine, splev(Z_fine, tck_odd), color='red')
pl.xticks(np.arange(Zmin, Zmax, 1))
pl.grid()

pl.show() 

print
print "Answer to part 3:"
#geiger-nuttall law: ln lambda = -a1.(Z/sqrt(E))+a2
print "Energy released in alpha decay:",    B(fixed_A, fZ) - B(fixed_A-4,fZ-2)
print "Half-life estimate:", fZ/sqrt(abs(B(fixed_A, fZ) - B(fixed_A-4,fZ-2)))
print "Energy released in beta+ decay:",    B(fixed_A, fZ) - B(fixed_A,fZ-1)
print "Half-life estimate:", fZ/sqrt(abs(B(fixed_A, fZ) - B(fixed_A,fZ-1)))
print "Energy released in beta- decay:",    B(fixed_A, fZ) - B(fixed_A,fZ+1)
print "Half-life estimate:", fZ/sqrt(abs(B(fixed_A, fZ) - B(fixed_A,fZ+1)))
print "Energy released in electron capture:",   B(fixed_A, fZ) - B(fixed_A,fZ-1)
print "Half-life estimate:", fZ/sqrt(abs(B(fixed_A, fZ) - B(fixed_A,fZ-1)))

#-------------------------------
print #RUN IN NO-PROXY ONLY
print "Answer to part 4:"
conn=httplib.HTTPConnection("ie.lbl.gov")
conn.request("GET","/toi/listnuc.asp?sql=&A1="+str(fixed_A)+"&A2="+str(fixed_A))
resp=conn.getresponse()
print resp.status
lines=resp.read()
indiv=lines.split("\t<TR>")
indiv=indiv[2:]
actZ=[]
for ind in indiv:
        actZ.append(int(ind.split("<TD >")[1].split("</TD>")[0]))
print "The actual possible values of Z are:"
print actZ
print "The values we are currently taking are:"
print range(Zmin,Zmax)

#---------------------------------
print "Answer to part 5:"
print "Spin orbit correction:"
#print "(sic) minus something dot s"

def n(Z):
    if Z<=2:
        return 1
    elif Z<=10:
        return 2
    elif Z<=18:
        return 3
    elif Z<=36:
        return 4
    elif Z<=54:
        return 5
    elif Z<=86:
        return 6
    else:
        return 7

print fZ/pow(n(fZ),3)*1e-5
#-------------------------------

print "Answer to question 2:"
#print "Kick-ass!"

def party(a):
    if a=='s':
        return 0
    elif a=='p':
        return 1
    elif a=='d':
        return 2
    else:
        return(ord(a)-99)

shells=[('1s_1/2',2),('|',0),('1p_3/2',4),('1p_1/2',2),('|',0),('1d_5/2',6),('2s_1/2',2),('1d_3/2',4),('|',0),('1f_7/2',8),('|',0),('2p_3/2',4),('1f_5/2',6),('2p_1/2',2),('|',0),('1g_9/2',10),('|',0),('1g_7/2',8),('2d_5/2',6),('2d_3/2',4),('3s_1/2',2),('1h_11/2',12),('|',0),('1h_9/2',10),('2f_7/2',8),('2f_5/2',6),('3p_3/2',4),('3p_1/2',2),('1i_13/2',14),('|',0),('2g_9/2',10),('3d_5/2',6),('1i_11/2',12),('2g_7/2',8),('4s_1/2',2),('3d_3/2',4),('1j_15/2',16)]

Z=input("Enter the Atomic Number (Number of Protons): ")
N=input("Enter the number of neutrons: ")
print
print "Nuclear Shell structure for proton: "
nZ=Z
for i in range(len(shells)):
    nZ-=shells[i][1]
    if(nZ<=0):
        break

for j in range(i):
    print shells[j][0], shells[j][1]
print shells[i][0], (shells[i][1]+nZ)

oZ=i
print "----------------"
print "Nuclear Shell structure for neutron: "
nA=N
for i in range(len(shells)):
    nA-=shells[i][1]
    if(nA<=0):
        break

for j in range(i):
    print shells[j][0], shells[j][1]
print shells[i][0], (shells[i][1]+nA)

oN=i

#--- oZ contains the index of the outermost shell of the proton ---#
#--- nZ                                                  neutron --#

if Z%2 == 0 and N%2 == 0:
    spin=0
    parity=1
elif Z%2 == 1 and N%2 == 1:
    spin=-nan
    parity=pow(-1,party(shells[oN][0][1])) * pow(-1,party(shells[oZ][0][1]))
else:
    if Z%2 == 1:
        spin=float(shells[oZ][0][3:-2])/2
        parity=pow(-1,party(shells[oZ][0][1]))
    else:
        spin=float(shells[oN][0][3:-2])/2
        parity=pow(-1,party(shells[oN][0][1]))

print "Spin =",spin
print "Parity =",parity

conn=httplib.HTTPConnection("ie.lbl.gov")
conn.request("GET","/toi/listnuc.asp?sql=&A1="+str(fixed_A)+"&A2="+str(fixed_A))
resp=conn.getresponse()
print resp.status
lines=resp.read()
indiv=lines.split("\t<TR>")
indiv=indiv[2:]
actZ=[]
for ind in indiv:
        actZ.append(int(ind.split("<TD >")[1].split("</TD>")[0]))
print "The actual possible values of Z are:"
print actZ
print "The values we are currently taking are:"
print range(Zmin,Zmax)
