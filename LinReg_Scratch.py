from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use("ggplot")

# Sample data to visualize and manually check
x_test = np.array([1,2,3,4,5,6], dtype = np.float64)
y_test = np.array([6,5,4,3,2,1], dtype = np.float64)

# Show test data
# plt.scatter(x_test, y_test)
# plt.show()

# To test our linear regression model with random datasets
## Function to make random datasets
### hm (how much) is the length of the dataset
### variance is how variable we want our dataset
### step is avg. change in y value
### correlation is boolean to determine positive or negative correlation
def create_dataset(hm, variance, step = 2, correlation = False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == "pos":
            val += step
        elif correlation and correlation == "neg":
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64)
    
x_test, y_test = create_dataset(40, 40, 2, correlation = False)
    
# Define function to find slope of best fit line
def best_fit_slope(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = (x_mean * y_mean) - np.mean(x*y)
    denominator = x_mean*x_mean - np.mean(x*x)
    m = numerator/denominator
    return m
# Define function to find the intercept of the best fit line
def best_fit_intercept(x, y):
    m = best_fit_slope(x,y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    b = y_mean - m*x_mean
    return b

m = best_fit_slope(x_test, y_test)
b = best_fit_intercept(x_test, y_test)
print("m equals " + str(m), "intercept is " + str(b))

regression_line = [(m*x)+b for x in x_test]

# Performing prediction via regression model
predict_x = 8
predict_y = m * predict_x + b


# Calculating accuracy and confidence
## Define squared error function
def squared_error(y, y_line):
    se = sum((y_line - y)**2)
    return se
## Coefficient of determination
def coeff_determination(y, y_hat):
    # Line with y means not to be confused with y_hat
    y_mean_line = [np.mean(y) for i in y]
    squared_error_regr = squared_error(y, y_hat)
    squared_error_ymean = squared_error(y, y_mean_line)
    return (1 - squared_error_regr/squared_error_ymean)

r_squared = coeff_determination(y_test, regression_line)
print("R^2 = " + str(r_squared))

#Plot points with the regression line
plt.scatter(x_test, y_test)
plt.scatter(predict_x, predict_y, color = 'g')
plt.plot(x_test, regression_line)
plt.show()