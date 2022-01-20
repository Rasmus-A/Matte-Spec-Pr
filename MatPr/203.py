import numpy as np

x = np.array([150, 250, 450, 600, 725]) #punkternas x-värden
y = np.array([74.3, 127, 230, 289, 367]) #punkternas y-värden
A = np.empty((len(x), 2))
C = np.empty((len(x), 1))

if len(x) != len(y):
    print("Lika många y-värden och x-värden krävs.")
else:
    A[:, 0] = np.ones(len(x))
    A[:, 1] = x

    C[:, 0] = y

    #Transposerar A till A_T
    A_T = A.transpose()

    #Multiplicerar A_T med A
    A_TA = A_T@A

    #Multiplicerar A_T med C
    A_TC = A_T@C

    #A_inv är inversen av A
    AT_A_inv = np.linalg.inv(A_TA)

    #Sökta matrisen B är inversen av A Multiplicerat med C
    Beta = AT_A_inv@A_TC

    print(Beta)