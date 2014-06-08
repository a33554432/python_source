import numpy as np
from scipy import stats

# ****** config ******
x_datafile_name = './data_pc/data.dat'
y_datafile_name = './data_pc/y.dat'
delimiter = ' '
#delimiter = ','
#delimiter = '\t'

# ****** read dataset ( := x) and y ******
x_temp = []
f = open(x_datafile_name, 'r')
for line in f:
    itemList = line.split(delimiter)
    nums = []
    for item in itemList:
        nums.append(int(item))
    x_temp.append(nums)

x = np.array(x_temp)
#print "x_data"
#print x

y_temp = []
f2 = open(y_datafile_name, 'r')
for line in f2:
    y_temp.append(int(line))
y = np.array(y_temp).T
print "y"
print y
print ""


# ****** calc R ( = correlation_coefficient_matrix of x ) ******
R = np.corrcoef(x.T)
dim = R.shape[0]
print "corr_coef_mat of_x"
print R
print ""


# ****** calc eigen_value and _vector of R ******
(la, eigv) = np.linalg.eig(R)
eigv_sorted = eigv[:, la.argsort()[-dim:][::-1]]
la_sorted = sorted(la)[::-1]
print "eig_val and eig_vec of R"
print la_sorted
print eigv_sorted
print ""

# ****** calc diagonalized-dataset ******
diaged_x = np.dot(x, eigv_sorted)
print "diaged_x"
print diaged_x
print ""

# calc 
#slope, intercept, r, _, _ = stats.linregress(diaged_x[:,0], y)
#print slope
#print intercept
#print r

for i in range(3):
    slope, intercept, r, _, _ = stats.linregress(diaged_x[:,i], y)
    print "%dth PC lambda = %f" % (i , la_sorted[i])
    print "slope = %f, intercept = %f, r = %f\n" % (slope, intercept, r)
    # + " intercept = " + intercept + " r = " + r
