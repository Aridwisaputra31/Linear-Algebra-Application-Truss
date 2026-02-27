import numpy as np
import pandas as pd

colf='B'
coll='Y'

colom_awal=str(colf)
colom_akhir=str(coll)
baris_dilewat=0
df=pd.read_excel('prakt_06_spl.xlsx', sheet_name='Sheet2', usecols=colom_awal+':'+colom_akhir)
print(df)


# Matriks A
delet_akhir=23


data=df.to_numpy()
s=data.shape
A=np.delete(data,delet_akhir,1)
print(s)
A_shape=A.shape
print('Matriks A :', A_shape)

# Matrik B
B_awal=0
B_akhir=23

kolom_dihapus=list(range(B_awal,B_akhir))
B=np.delete(data,kolom_dihapus,1)
print(B)
B_shape=B.shape
print(B_shape)

#perhitungan
deta=np.linalg.det(A)
A1=np.linalg.inv(A)
#print('matriks A invers =', A1)

X1=np.dot(A1,B)
print('Perkalian dot metode program \n', X1)

X2=np.linalg.solve(A,B)
print('Perkalian dot metode solve \n',X2)
