def knapsack(values, weights, capacity):
    # Create a 2D DP array to store the maximum value for each item and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]

    for item in range(1, len(values) + 1):
        for weight in range(1, capacity + 1):
            if weights[item - 1] <= weight:
                # Compare including the item and excluding it
                dp[item][weight] = max(dp[item - 1][weight - weights[item - 1]] + values[item - 1], dp[item - 1][weight])
            else:
                # If item cannot be included, inherit the value from above row
                dp[item][weight] = dp[item - 1][weight]
    
    # The last element in the dp array is the maximum value achievable
    return dp[-1][-1]


while True:
    try:
        print("\nPress Ctrl+C to terminate...")

        # Input the number of items
        n = int(input('Enter number of items: '))

        # Input the values and weights, ensuring they match the number of items
        values = list(map(int, input("Enter values of items (space-separated): ").split()))
        weights = list(map(int, input("Enter weights of items (space-separated): ").split()))

        if len(values) != n or len(weights) != n:
            print("Error: The number of values and weights must match the number of items.")
            continue

        # Input the knapsack capacity
        capacity = int(input("Enter maximum weight capacity: "))

        # Calculate the maximum value that can be carried
        maximum_value = knapsack(values, weights, capacity)
        print(f'The maximum value of items that can be carried: {maximum_value}')

    except ValueError:
        print("Error: Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break
