import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Funzione 1
def somman(x):
  sum=0
  for i in range (0,x+1):
    sum-sum+i
  return sum

#Funzione 2
def sommasqrt(x):
  sum=0
  for i in range (0, x+1):
    sum=sum+np.sqrt(i)
  return sum

#Funzione 3
def sommaprodotto(x):
  s=0
  p=1
  for i in range(1, x+1):
    s=s+i
    p=p*i
  return s, p

#Funzione 4
def geometrica(x, alpha=1):
  sum=0
  for i in range (1, x+1):
    sum=sum+pow(i, alpha)
  return sum
