# numpy ini sering dipakai dalam Data Science & Machine Learning, karena berbasis array/matrix

import numpy as np

listA = [1, 2, 3, 4, 5]
vectorA = np.array([1, 2, 3, 4, 5])
vectorB = np.array([1, 10, 2, 11, 3])
print(f"listA     = {listA}")
print(f"vectorA   = {vectorA}")
print(f"vectorB   = {vectorB}\n")

# print(listA**a)   <- Akan Error
print(f"listA*2   = {listA*2}") 
print(f"vectorA^2 = {vectorA**2}")
print(f"vectorA*5 = {vectorA*5}\n")

matrixC = np.array([(1,2), (3,4)])
print(f"matrixC   =\n{matrixC}")
print(f"matrixC^2 =\n{matrixC**2}\n")

zerosD = np.zeros((2,2))
print(f"zerosD    =\n{zerosD}\n")

onesE = np.ones((2,2))
print(f"onesE     =\n{onesE}\n")

jumlah = matrixC + (matrixC**2) + onesE
print(f"Jumlah dari matrixC + (matrixC**2) + onesE =\n{jumlah}")

#00ff00
#rgb(0,0,0)
#ef5350
#42a5f5
