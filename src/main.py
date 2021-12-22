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

x2 = float(x2)
c0 = float(c0)
a = float(a)
pot = float(pot)

f1 = fun(c0, a, pot, x1)
f2 = fun(c0, a, pot, x2)

if( f1*f2 > 0 ):
  print('riprova con un altro estremo')

while(True):
  xm = (x1 + x2) / 2
  f2 = fun(c0, a, pot, xm)
  if( f1*f2 < 0 ):
    x2 = xm
  else:
    x1 = xm





