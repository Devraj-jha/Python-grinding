import numpy as np

zero_array = np.zeros(7)
print(zero_array) #use to write array of zeros.
arr_linespace = np.linspace(1,5,4)  # Create 4 numbers between 1 and 5 (inclusive)
print(arr_linespace)
import numpy as np
import time

# Python List
python_list = list(range(1000000))

start_time = time.time()
python_list = [x * 2 for x in python_list]  # Double every element
end_time = time.time()
print(f"Python List Time: {end_time - start_time} seconds")

# NumPy Array
numpy_array = np.arange(1000000)

start_time = time.time()
numpy_array = numpy_array * 2  # Efficient element-wise operation
end_time = time.time()
print(f"NumPy Array Time: {end_time - start_time} seconds")
