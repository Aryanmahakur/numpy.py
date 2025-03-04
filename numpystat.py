import numpy as np

#mean
np1=np.array([1, 2, 3, 4, 5])
print(np.mean(np1))
#median
np2=np.array([1, 2, 3, 4, 5])
print(np.median(np2))
#standard deviation
np3=np.array([50,60,70,80,90])
print(np.std(np3))
#variance
np4=np.array([50,60,70,80,90])
print(np.var(np4))
#sum
np5=np.array([1, 2, 3, 4, 5])
print(np.sum(np5))
#product
np6=np.array([1, 2, 3, 4, 5])
print(np.prod(np6))
#minimum
np7=np.array([1, 2, 3, 4, 5])
print(np.min(np7))
#maximum
np8=np.array([1, 2, 3, 4, 5])
print(np.max(np8))
#correlation
np9=np.array([2,4,6,8,10])
np10=np.array([50,65,80,85,90])
print(np.corrcoef(np9, np10))
#coefficient of variation
np11=np.array([1, 2, 3, 4, 5])
print(np.std(np11)/np.mean(np11))
print(5/50*100)
#quantile
np12=np.array([1, 2, 3, 4, 5])
print(np.quantile(np12, 0.5))
#percentile
np13=np.array([45,55,60,62,65,70,75,80,85,90])
print(np.percentile(np13, 70))
#five number summary
np14=np.array([10,11,12,25,25,27,31,33,34,34,35,36,43,50,50])
print(np.percentile(np14, [0, 25, 50, 75, 100]))
#skewness
#univariate
np15=np.array([45,50,55,60,65,70,75,80,85,90])
print(np.mean(np15))
print(np.std(np15))
print(np.median(np15))
#bivariate
x=np.array([2,3,5,7,9])
y=np.array([50,60,80,90,95])

coef=np.corrcoef(x, y)
print("bivariate",coef[0,1])
#covariance
print(np.cov(x, y))



# Data
x = np.array([2, 4, 6, 8])
y = np.array([3, 7, 5, 9])

# Compute covariance matrix
cov_matrix = np.cov(x, y)

# Extract covariance between x and y
cov_xy = cov_matrix[0, 1]  # or cov_matrix[1, 0] (same value)

print("Covariance Matrix:\n", cov_matrix)
print("Covariance between x and y:", cov_xy)
#covariance matrix
x = np.array([2, 3,5,7,9])
y = np.array([40,50,70,80,90])
cov_matrix = np.cov(x, y)
print("Covariance Matrix:\n", cov_matrix)
#covariance matrix


# Data
x = np.array([2, 3, 5, 7, 9])
x2 = np.array([40, 50, 70, 80, 90])
z = np.array([6, 7, 6, 8, 9])

# Compute covariance matrix
cov_matrix = np.cov([x, x2, z])

print("Covariance Matrix:\n", cov_matrix)
#pearson correlation coefficient
x = np.array([2,4,6,8,10])
y = np.array([3,7,5,10,12])
r = np.corrcoef(x, y)[0, 1]
print("Pearson correlation coefficient:", r)



