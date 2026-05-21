import argparse
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def solve_heat(T0: float, T1: float, T2: float, T3: float, T4: float):
    alpha = 2
    delta_x = 1
    delta_t = delta_x**2/(4*alpha)
    N = 50

    T = np.full((N, N), T0)
    T[0,:] = T1
    T[:,-1] = T2
    T[-1,:] = T3
    T[:,0] = T4

