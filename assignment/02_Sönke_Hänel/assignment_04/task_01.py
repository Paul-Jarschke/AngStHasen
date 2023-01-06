"""
Python supports lambda functions as a handy way to define small, anonymous, i.e., unnamed, functions inline. The basic syntax for lambda functions is:
lambda parameter1, parameter2, ... : expression

Use a lambda function only to retain the even values in an array of integers.
Test your function with an input array of your choosing.
Print the input array and the filtered output array to stdout.
"""
import numpy as np

m = np.array([[1, 2, 3], [4, 4, 6]])
print(m)

output = m[[(lambda x: x % 2 == 0)(x) for x in m]]

print(f'Input is:\n{m}\nOutput is:\n{output}')
"""
alternative:
output = (lambda x: x[np.where(x % 2 == 0)])(m)

named alternative:
lambda_scam = (lambda x: x[np.where(x % 2 == 0)])
result = lambda_scam(m)
"""

