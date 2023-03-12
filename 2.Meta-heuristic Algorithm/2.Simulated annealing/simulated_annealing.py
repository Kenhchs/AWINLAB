import math
import random
import matplotlib.pyplot as plt

# Read capacity, weight, profit file and store in variable capcity, weights, profits respectively
def ReadFile(capacity_file, weight_file, profit_file):
    with open(capacity_file) as f:
        global capacity
        capacity = int(f.read())
    with open(weight_file) as f:
        global weights
        for weight in f:
            weights.append(int(weight))
    with open(profit_file) as f:
        global profits
        for profit in f:
            profits.append(int(profit))
    return

# Initial state
def InitialSolution():
    global solution, weight, best_profit, iteration_score
    solution = [0 for i in range(len(weights))] # Do not select any item
    weight = 0
    best_profit = 0
    for i in range(0, len(weights)):
        if weight + weights[i] <= capacity and random.random() >= 0.6: # Use random to generate different initial solution
            solution[i] = 1
            weight = weight + weights[i]
            best_profit = best_profit + profits[i]
    iteration_score.append(best_profit)
    return

# Calculate the total profit
def Evaluate(solution):
    value = 0
    for i in range(0, len(solution)):
        if solution[i] == 1:
            value = value + profits[i]
    return value

# Calculate solution's weight
def Calculate_Weight(solution):
    w = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            w = w + weights[i]
    return w

# Find neighbor node
def Neighbor(solution):
    candidate = solution.copy()
    while True:
        i = random.randint(0, len(candidate) - 1)
        if candidate[i] == 1: 
            candidate[i] = 0 # Change selected item to non-selected item
            break
        elif candidate[i] == 0 and Calculate_Weight(candidate) + weights[i] <= capacity:
            candidate[i] = 1 # Change non-selected item item to selected 
            break
    return candidate

temperature = 1600 # Initial temperature
alpha = 0.999 # Used to decrease temperature
iteration_num = 500 # Number of iteration
capacity = -1 # Bag's capacity
profits = [] # Profit of items. profit[i] = p means the profit of item "i" is p
weights = [] # Weight of items. weights[i] = w means the weight of item "i" is w
x_axis = [i for i in range(0, iteration_num + 1)] # Used to draw x-axis, its value = [0, 1, 2, ...... , iteration_num - 1, iteration_num]
best_profit = -1 # Best profit so far
solution = [] # Current solution. solution[i] = 1 means item "i" is selected, solution[i] = 0 means item "i" is not selected
iteration_score = [] # History of best profits

ReadFile('./../p07_c.txt', './../p07_w.txt', './../p07_p.txt')
InitialSolution()
for i in range(0, iteration_num):
    candidate = Neighbor(solution)
    if Evaluate(candidate) > Evaluate(solution):
        solution = candidate # Accept
        if Evaluate(candidate) > best_profit:
            best_profit = Evaluate(candidate)
    else:
        if random.random() < math.exp((Evaluate(candidate) - Evaluate(solution)) / temperature): # accept candidate with small probability
            solution = candidate # Accept
    temperature = temperature * alpha # Decrease temperature
    iteration_score.append(best_profit) # Store history


# Plot graph
fig = plt.figure()
plt.plot(x_axis, iteration_score, '.b-')
plt.show()