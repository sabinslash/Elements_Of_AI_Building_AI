import numpy as np
from io import StringIO


def fit_model(input_file):
  """
  Fits a linear regression model to cabin data and prints coefficients and predicted prices.

  Args:
      input_file: A file-like object containing cabin data in CSV format.
  """

  # Read data from CSV using genfromtxt, skipping header
  data = np.genfromtxt(input_file, skip_header=1)

  # Separate features (all columns except last) and target prices (last column)
  X = data[:, :-1]
  y = data[:, -1]

  # Add a column of ones for the intercept term
  X = np.c_[np.ones(len(X)), X]

  # Fit the linear regression model using lstsq
  c, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

  # Print coefficients with one decimal place precision
  print("Estimated Coefficients:", c.round(1))

  # Calculate predicted prices using fitted coefficients
  predicted_prices = X @ c

  # Print predicted prices with zero decimal places
  print("Predicted Prices:", predicted_prices.astype(int))


# Simulate reading a file with sample data
input_string = """
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
"""

np.set_printoptions(precision=1)  # Set output precision for easier reading

input_file = StringIO(input_string)
fit_model(input_file)
