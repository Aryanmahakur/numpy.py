import numpy as np
np1 = np.array([10, 20, 30, 40, 50])
x=[False, True, False, True, True]
result = np1[x]
print(result)
np2=np.array([5, 12, 17, 24, 31, 40])
filter=np2%2==0
print(np2[filter])
np3=np.array([[10, 20, 30, 40, 50, 60, 70]])
print(np3[1:5])
print(np3[0:5:2])
np4=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np4[1,1])
print(np4[1,1:4])
print(np4[0:2,4])
np5=np.array([5,10,15,20])
np5[3]=25
print(np5)
np6=np.array([[1,2,3,4],[5,6,7,8]])
np6[1,2]=10
print(np6)
np7=np6.view()
print(np7)
print(np6)

np9=np.array([1,2,3,4,5,6,7,8,9,10])
print(np9)
np10=np9.copy()
print(np10)
np9[0]=10
print(np9)
print(np10)
np12=np.array([1,2,3,4,5,6,7,8,9,10])
np13=np12.reshape(2,5)

print(np13)
np14=np.array([1,2,3,4,5,6,7,8,9,10])
for x in np14:
    print(x)