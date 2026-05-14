import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.constants import g

def fun(t, vector, l):
    """
    dx/dt = v
    dv/dt = sin(x)

    bierzemy parę [x, v] i zwracamy [v, a] = [v, g/l*sin(x)]
    """
    return np.array([vector[1], -g/l*np.sin(vector[0])])

def solver(l, theta0, omega0, t_eval, n_eval, method):
    time = np.linspace(0, t_eval, n_eval)
    sol = solve_ivp(fun, (0, time[-1]), [theta0, omega0], method, t_eval=time, args=(l,))
    return sol.t, sol.y[0], sol.y[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('l', type=float)
    parser.add_argument('theta0', type=float)
    parser.add_argument('omega0', type=float)
    parser.add_argument('t_eval', type=float)
    parser.add_argument('n_eval', type=int)
    parser.add_argument('--method', type=str, default='RK45')
    args = parser.parse_args()

    t, theta, omega = solver(args.l, args.theta0, args.omega0, args.t_eval, args.n_eval, args.method)
    print(t, theta, omega)
    plt.plot(t, theta)
    plt.xlabel(r"t")
    plt.ylabel(r"$\theta(t)$")
    plt.show()
    plt.plot(theta, omega)
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$\omega(\theta)$")
    plt.show()