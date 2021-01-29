'''
Let's assume that we want to maximize the profits of a state-of-the-art factory that manufactures 
two different types of robots:
    Advanced model (A): This provides full functionality. Manufacturing each unit of the 
        advanced model results in a profit of $4,200.
    Basic model (B): This only provides basic functionality. Manufacturing each unit of the 
        basic model results in a profit of $2,800.
    
    There are three different types of people needed to manufacture a robot. The exact number of 
    days needed to manufacture a robot of each type are as follows:
    
    Type of Robot            Technician    AI Specialist      Engineer
    Robot A: advanced model    3 days        4 days            4 days
    Robot B: basic model       2 days        3 days            3 days
    
    The factory runs on 30-day cycles. A single AI specialist is available for 30 days in a cycle. 
    Each of the two engineers will take 8 days off in 30 days. So, an engineer is available only for 
    22 days in a cycle. There is a single technician available for 20 days in a 30-day cycle.
    
    The factory runs on 30-day cycles.
    The following table shows the number of people we have in the factory in a cycle:
    
                          Technician            AI Specialist    Engineer
    Number of people        1                        1                2
    Total number of days  1 x 20 = 20 days    1 x 30 = 30 days    2 x 22 = 44 days
    
    So now this can be modeled as follows:
        maximum profit = 4200A + 2800B
            subjected to,
                A >= 0
                B >= 0
                3A + 2B <= 20
                4A + 3B <= 30
                4A + 3B <= 44
    
    Let's solve this using a python package called pulp which implements Linear Programming.

        
'''

import pulp

solver_list = pulp.listSolvers(onlyAvailable=True)
print solver_list

# let's instantiate our problem class
model = pulp.LpProblem('Profit maximizing problem', pulp.LpMaximize)

# let's define to linear variables A and B
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')

# Objective Function
model += 4200 * A + 2800 * B, 'Profit'

# Constraints
model += 3 * A + 2 * B <= 20 
model += 4 * A + 3 * B <= 30 
model += 4 * A + 3 * B <= 44

# let's solve the problem
model.solve()

pulp.LpStatus[model.status]


