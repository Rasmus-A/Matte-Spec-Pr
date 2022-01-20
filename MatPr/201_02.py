import numpy as np

def make_mat_product(mat_A, mat_B):

    antal_rader = number_of_rows_in_A = A.shape[0]
    antal_kolonner = number_of_cols_in_B = B.shape[1]

    # Ta reda på antalet rader och kolonner
    # för resultatmatrisen (givet att mat_A och mat_B
    # är multiplicerbara) 
    result = np.zeros([antal_rader, antal_kolonner])

    for i in range(antal_rader):
        for j in range(antal_kolonner):
            result[i, j] = get_element(mat_A, mat_B, i+1, j+1)

    # Processa multiplikationen genom upprepade
    # anrop till get_element. Uppdatering av
    # innehållet i result.
    return result

def get_element(mat_A, mat_B, i, j):
    i -= 1
    j -= 1

    if number_of_cols_in_A == number_of_rows_in_B:
        result = 0
        for k in range(number_of_cols_in_A):
            result += np.array(mat_A) [i, k] * np.array(mat_B) [k, j]
    else:
        result = None
    # Här processas matriserna mat_A och mat_B
    # samt att värdet på result uppdateras
    return result

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris

number_of_cols_in_A = A.shape[1]
number_of_rows_in_B = B.shape[0]

# Ändra inget under denna rad,
C = make_mat_product(A, B)
if C is None:
    print("De angivna matriserna är inte multiplicerbara med varandra")
else:
    print(f"C =\n {C}")
    # Skriver ut
    # [[28. 34.]
    # [64. 79.]]
    # givet matriserna A och B som de var från början
print("Programmet avslutades normalt")
