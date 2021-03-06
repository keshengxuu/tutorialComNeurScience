# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:22:02 2021

@author: ZXJ
"""

from scipy.integrate import odeint
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt

g_L = 0.1 # oK
g_Na = 35.0 # ok
g_K = 9.0 # ok
E_L = -65.0 #ok
E_Na = 55.0 #ok 
E_K = -90.0 #ok
C_m = 1.0 #ok
fai = 5.0 # ok
I_app = 3
T_start = 0
T_stop = 200
dt = 0.01



def alpha_n(v):
    return -0.01*(v+34)/(np.exp(-0.1*(v+34))-1) # ok RH
def beta_n(v):
    return 0.125*np.exp(-(v+44)/80) # ok RH
def alpha_m(v):
    return -0.1*(v+35)/(np.exp(-0.1*(v+35))-1) # ok RH
def beta_m(v):
    return 4*np.exp(-(v+60)/18) # ok RH
def alpha_h(v):
    return 0.07*np.exp(-(v+58)/20) # ok RH
def beta_h(v):
    return 1/(np.exp(-0.1*(v+28))+1) # ok RH

def m_inf(V):
    return alpha_m(V)/(alpha_m(V) + beta_m(V))

def derivative(x0):
    
    V, h, n= x0
    
    I_L = g_L*(V-E_L)
    I_Na = g_Na*m_inf(V)**3*h*(V-E_Na)
    I_K = g_K*n**4*(V-E_K)
    
    dVdt = (-I_Na-I_K-I_L+I_app)/C_m
    dhdt = fai*(alpha_h(V)*(1.0-h)-beta_h(V)*h)
    dndt = fai*(alpha_n(V)*(1.0-n)-beta_n(V)*n)
    
    return np.array([dVdt, dhdt, dndt])



# initial value
V = -70

h = 1

n = 0.3

x0 = np.array([V, h, n])
dsdt = [0,0,0]
Nstep = 20000
time1 = []
vara=[]
 

if __name__ == "__main__":
    
    #t = np.arange(T_start,T_stop,dt)
    #sol = odeint(derivative, x0, t)
    #V1 = sol[:,0]
    
     # transient state
    for i in range(1000):
        dsdt = dsdt + derivative(x0)*dt
        x0 = dsdt
        
        
    # start the  main simulation
    for i in range(Nstep):
        dsdt = dsdt + derivative(x0)*dt
        #print (dsdt )
        t = i*dt
        time1.append(t)  # append (save) each time step simulation data  list time1
        vara.append(dsdt)
        x0 = dsdt
    dsdtdata = np.array(vara)
    
    

    fig = plt.figure(1, figsize=(8,6))
    plt.clf()
    plt.plot(time1,dsdtdata[:,0],lw=2,c="k")
    plt.xlabel("time [ms]")
    plt.ylabel("V [mV]")
    #plt.ylim([-60,20])








