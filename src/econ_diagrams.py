'''
Created on Mar 18, 2020

@author: kirkkittell
'''

import matplotlib.pyplot as plt
import numpy as np

# (1) Draw a supply curve
# (2) Draw a demand curve

def figure_1():
    Q = np.linspace(0, 2, 100)
    S = 0 + 2 * Q
    D = 2 - 2 * Q
    
    plt.plot(Q, S)
    plt.plot(Q, D)
    plt.show()
    
    return

def figure_2():
    m_1 = -10
    b_1 = 120
    m_2 = -2
    b_2 = 60 
    
    # P = mQ + b
    P_min = 0
    P_max = max(b_1, b_2)
    
    Q_min = 0
    # Q_max = Q(P=0)
    Q_max = max(-b_1/m_1, -b_2/m_2) 
    
    Q = np.linspace(Q_min, Q_max, 100)
    
    P_1 = m_1 * Q + b_1
    P_1[P_1 < 0] = 0
    plt.plot(Q, P_1)
    
    P_2 = m_2 * Q + b_2
    P_2[P_2 < 0] = 0
    plt.plot(Q, P_2)
    
    plt.show()
    return

figure_2()
