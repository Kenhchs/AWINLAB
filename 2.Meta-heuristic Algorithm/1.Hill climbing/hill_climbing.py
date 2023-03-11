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

# Find neighbor node
def Neighbor(solution, weight):
    flip_bit = -1
    value_changed = -1
    
    # Try to flip bit from 0 to 1 if possible
    for i in range(len(solution)):
        if solution[i] == 0:
            if weight + weights[i] <= capacity:
                if value_changed <= profits[i]:
                    flip_bit = i
                    value_changed = profits[i]
    if flip_bit != -1:
        solution[flip_bit] = 1
        return solution

    # Try to swap the selected item before with non-selected item before
    for i in range(0, len(solution)):
        for j in range(i + 1, len(solution)):
            if solution[i] != solution[j]:
                solution[i], solution[j] = solution[j], solution[i]
                if Calculate_Weight(solution) > capacity or Evaluate(solution) <= best_profit:
                    solution[i], solution[j] = solution[j], solution[i]
                else:
                    return solution

    # Random-Restart Hill-Climbing
    weight = 0
    sequence = [i for i in range(0, len(solution))] # sequence = [0, 1, 2, ...... , 499, 500]
    solution = [0 for i in range(0, len(solution))] # Do not select any item
    random.shuffle(sequence)
    for i in sequence:
        if weight + weights[i] <= capacity and random.random() >= 0.6:
            solution[i] = 1
            weight = weight + weights[i]

    return solution

# Calculate solution's weight
def Calculate_Weight(solution):
    w = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            w = w + weights[i]
    return w
    
    

iteration_num = 500 # Number of iteration
capacity = -1 # Bag's capacity
profits = [] # Profit of items. profit[i] = p means the profit of item "i" is p
weights = [] # Weight of items. weights[i] = w means the weight of item "i" is w
x_axis = [i for i in range(0, iteration_num + 1)] # Used to draw x-axis, its value = [0, 1, 2, ...... , iteration_num - 1, iteration_num]

best_profit = -1 # Best profit so far
weight = -1 # Weight of current solution
solution = [] # Current solution. solution[i] = 1 means item "i" is selected, solution[i] = 0 means item "i" is not selected
iteration_score = [] # History of best profits

ReadFile('./../p07_c.txt', './../p07_w.txt', './../p07_p.txt')
InitialSolution()
for i in range(0, iteration_num):
    solution = Neighbor(solution, weight)
    weight = Calculate_Weight(solution)
    if Evaluate(solution) > best_profit:
        best_profit = Evaluate(solution)
    iteration_score.append(best_profit) # Store history


# Plot graph
fig = plt.figure()
plt.plot(x_axis, iteration_score, '.b-')
plt.show()