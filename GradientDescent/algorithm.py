import numpy as np
import math

def gradient_descent(x,y):
    m_current = 0
    b_current = 0
    length = len(x)
    learning_rate = 0.066
    total_iterations = 10000

    for i in range(total_iterations):
        y_predicted = m_current * x + b_current
        if i != 0:
            previous_cost = cost
        else:
            previous_cost = 0
        cost = (1/length) * sum([val ** 2 for val in (y - y_predicted)])
        if math.isclose(previous_cost, cost, rel_tol=1e-20) == True:
            print(f"Cost has reached minimum: {cost}")
            break
        m_derivative = (-2/length) * sum(x*(y-y_predicted))
        b_derivative = (-2/length) * sum((y-y_predicted))
        m_current = m_current - learning_rate * m_derivative
        b_current = b_current - learning_rate * b_derivative
        print(f"m {m_current}, b {b_current}, cost {cost}, previous_cost {previous_cost} iteration {i}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)