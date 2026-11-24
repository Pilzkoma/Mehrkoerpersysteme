import numpy as np

def dh_matrix(theta, d, a, alpha):
    """
    theta : Gelenkwinkel um z_{i-1}  [rad]
    d     : Verschiebung entlang z_{i-1}  [Laengeneinheit]
    a     : Verschiebung entlang x_i  [Laengeneinheit]
    alpha : Verdrehung um x_i  [rad]
    """
    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha), np.sin(alpha)
    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0.0,      sa,       ca,      d],
        [0.0,     0.0,      0.0,    1.0],
    ])

# Gelenk 1
theta1 = np.deg2rad(0.0)   # [rad]
d1     = 0.0
a1     = 0.0
alpha1 = np.deg2rad(0.0)   # [rad]

# Gelenk 2
theta2 = np.deg2rad(0.0)   # [rad]
d2     = 0.0
a2     = 0.0
alpha2 = np.deg2rad(0.0)   # [rad]

# Gelenk 3
theta3 = np.deg2rad(0.0)   # [rad]
d3     = 0.0
a3     = 0.0
alpha3 = np.deg2rad(0.0)   # [rad]

# Gelenk 4
theta4 = np.deg2rad(0.0)   # [rad]
d4     = 0.0
a4     = 0.0
alpha4 = np.deg2rad(0.0)   # [rad]


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    print(dh_matrix(theta1, d1, a1, alpha1))
