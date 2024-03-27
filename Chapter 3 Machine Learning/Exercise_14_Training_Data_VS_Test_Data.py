import numpy as np
from io import StringIO

# Define the training data
train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

# Define the test data
test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Read in the training data and separate it to x_train and y_train
    train_data = np.genfromtxt(StringIO(train_string), skip_header=1)
    x_train = train_data[:, :-1]
    y_train = train_data[:, -1]
    
    # Add a column of ones to x_train for the intercept term
    x_train = np.hstack([np.ones((x_train.shape[0], 1)), x_train])
    
    # Fit a linear regression model to the data and get the coefficients
    c, _, _, _ = np.linalg.lstsq(x_train, y_train, rcond=None)
    
    # Read in the test data and separate x_test from it
    test_data = np.genfromtxt(StringIO(test_string), skip_header=1)
    x_test = test_data[:, :-1]
    
    # Add a column of ones to x_test for the intercept term
    x_test = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
    
    # Print out the linear regression coefficients
    print("Coefficients of the linear regression:")
    print(c)
    
    # This will print out the predicted prices for the two new cabins in the test data set
    print("Predicted prices:")
    print(x_test @ c)

main()
