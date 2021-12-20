import math
import cmath

def fun(c0, a, pot, x):
  c = 3.0e8
  hbar = 6.58e-16
  m = 0.511e6
  cost = math.sqrt(m)/(math.sqrt(2)*hbar*c*1e10)
  f = math.cos(cost*math.sqrt(c0)*a*math.sqrt(x)) - math.sqrt(x/pot)
  return f

x1 = 0
x2 = input('scrivi secondo estremo: ')
c0 = input('scrivi peso massa: ')
a = input('scrivi larghezza buca: ')
pot = input('scrivi profondità buca: ')

if( fun( float(c0), float(a), float(pot), float(x1) )*fun( float(c0), float(a), float(pot), float(x2) ) < 0 ):
  while(True):
    
  
else:
    #if(fun(c0,a,pot,x1) < epsilon):
     # break
  print('f(x2) = ' fun( float(c0), float(a), float(pot), float(x2) ) )
  print('prova con un altro estremo')



#for():



