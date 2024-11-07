# %% [markdown]
# # Implement Gradient Descent Algorithm to find the local minima of a function.
# For example, find the local minima of the function y=(x+3)² starting from the point x=2.
# 

# %% [markdown]
# ![Graph.png](attachment:Graph.png)

# %% [markdown]
# ##  We know the answer just by looking at the graph. y = (x+3)² reaches it’s minimum value when x = -3 (i.e when x=-3, y=0). Hence x=-3 is the local and global minima of the function.Below is the implementation in python 

# %%
current_x = 2 # The algorithm starts at x=3
rate = 0.01 # Learning rate
precision = 0.000001 #This tells us when to stop the algorithm
previous_step_size = 1 
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter
df = lambda x: 2*(x+3) #Gradient of our function

# %%
while previous_step_size > precision and iters < max_iters: #When Previous Step SIze will be less than Precision then we will reach the global maxima
    previous_x = current_x #Store current x value in prev_x
    current_x = current_x - rate * df(previous_x) #Grad descent
    previous_step_size = abs(current_x - previous_x) #Change in x
    iters = iters+1 #iteration count
    print("Iteration",iters,"\nX value is",current_x) #Print iterations
    
print("The local minimum occurs at", current_x)

# %%



