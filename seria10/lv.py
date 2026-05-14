import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def fun(t, vector, a, b, c, d):
    """
    vector = [x, y]
    dx/dt = (a-by)x
    dy/dt = (c-dx)y
    [x, y] -> [(a-by)x, (-c+dx)y]
    """
    return [(a-b*vector[1])*vector[0], (-c+d*vector[0])*vector[1]]

def solver(a, b, c, d, x0, y0, t_max, n_eval):
    time = np.linspace(0, t_max, n_eval)
    sol = solve_ivp(fun, (0, t_max), [x0, y0], t_eval=time, args=(a, b, c, d))
    return sol.t, sol.y[0], sol.y[1]

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=float)
    parser.add_argument('b', type=float)
    parser.add_argument('c', type=float)
    parser.add_argument('d', type=float)
    parser.add_argument('x0', type=float)
    parser.add_argument('y0', type=float)
    parser.add_argument('t_max', type=float)
    parser.add_argument('n_eval', type=int)
    args = parser.parse_args()

    t, x, y = solver(args.a, args.b, args.c, args.d, args.x0, args.y0, args.t_max, args.n_eval)
    plt.plot(t, x, label='x(t)')
    plt.plot(t, y, label='y(t)')
    plt.xlabel('t')
    plt.legend()
    plt.show()