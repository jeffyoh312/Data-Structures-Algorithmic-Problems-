# Ask the user for a positive integer
def get_integer_input(message):
    while True:
        try:
            number = int(input(message)) # Attempts to convert the input into an integer

            if number > 0: # Checks if value is larger than 0
                return number

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")

# Collect the names, weights, and values of the items
def get_item_details(number_of_items):
    names = []
    weights = []
    values = []

    for item_number in range(1, number_of_items + 1):
        print("\nItem", item_number)

        name = input("Enter the name of the item: ").strip()

        while name == "":
            print("Please enter a valid name.")
            name = input("Enter the name of the item: ").strip()

        weight = get_integer_input("Enter the weight of the item: ")
        value = get_integer_input("Enter the value of the item: ")

        #stores the values collected into the lists
        names.append(name)
        weights.append(weight)
        values.append(value)

    return names, weights, values

# Creates and fill the dynamic programming table
def create_dp_table(weights, values, capacity):
    number_of_items = len(weights)

    #Creates the empty list for the dynamic programming table
    dp = []

    # Creates required rows and colums for the dynamic programming table and initialises all of them to 0
    for row_number in range(number_of_items + 1):
        row = [0] * (capacity + 1)
        dp.append(row)

    # Fill the dynamic programming table
    for item_number in range(1, number_of_items + 1):
        current_weight = weights[item_number - 1]
        current_value = values[item_number - 1]

        for current_capacity in range(capacity + 1):

            # Check whether the current item fits in capacity
            if current_weight <= current_capacity:

                # Calculate the value if the item is included
                include_item = current_value + dp[item_number - 1][current_capacity - current_weight]

                # Calculate the value if the item is excluded
                exclude_item = dp[item_number - 1][current_capacity]

                # Store the larger value
                if include_item > exclude_item:
                    dp[item_number][current_capacity] = include_item
                else:
                    dp[item_number][current_capacity] = exclude_item

            else:
                # The item does not fit, copy the value from the previous row
                dp[item_number][current_capacity] = dp[item_number - 1][current_capacity]

    return dp

# Work backwards through the table to find the selected items
def find_selected_items(dp, weights, capacity):
    selected_indexes = []
    remaining_capacity = capacity
    number_of_items = len(weights)

    for item_number in range(number_of_items, 0, -1):
        current_result = dp[item_number][remaining_capacity]
        previous_result = dp[item_number - 1][remaining_capacity]

        # If current and previous results are the same, the item was not added into the knapsack
        # If current and previous results are different, the item was added into the knapsack 
        if current_result != previous_result:
            # Append the items added into the knapsack into a list to store
            selected_indexes.append(item_number - 1)

            remaining_capacity = remaining_capacity - weights[item_number - 1]

    return selected_indexes

# Display the completed dynamic programming table
def display_dp_table(dp):
    number_of_items = len(dp) - 1
    capacity = len(dp[0]) - 1

    print("\nDynamic-Programming Table")
    print("Rows = number of items considered")
    print("Columns = knapsack capacity\n")

    print("Items\\Capacity", end="\t")

    for current_capacity in range(capacity + 1):
        print(current_capacity, end="\t")

    print()

    for row_number in range(number_of_items + 1):
        print(row_number, end="\t\t")

        for current_capacity in range(capacity + 1):
            print(dp[row_number][current_capacity], end="\t")

        print()

# Display the selected items and final results
def display_output(
    names,
    weights,
    values,
    selected_indexes,
    maximum_value
):
    print("\nSelected Items")
    print("Name\t\tWeight\tValue")
    print("--------------------------------")

    total_weight = 0

    if len(selected_indexes) == 0:
        print("No items were selected.")

    else:
        # Display selected items in their original input order
        for position in range(len(selected_indexes) - 1, -1, -1):
            index = selected_indexes[position]

            print(
                names[index],
                "\t\t",
                weights[index],
                "\t",
                values[index]
            )

            total_weight = total_weight + weights[index]

    print("\nTotal weight:", total_weight)
    print("Maximum value:", maximum_value)

# Control the order in which the program runs
def main():
    print("0/1 Knapsack Using Dynamic Programming")
    print("---------------------------------------")

    # Get the number of available items inputted
    number_of_items = get_integer_input(
        "Enter the number of items you would like to choose from: "
    )

    # Get the information about each item
    names, weights, values = get_item_details(number_of_items)

    # Get the maximum weight the knapsack can carry
    capacity = get_integer_input(
        "\nEnter the knapsack capacity: "
    )

    # Create and fill the dynamic programming table
    dp = create_dp_table(weights, values, capacity)

    # Find the selected items
    selected_indexes = find_selected_items(
        dp,
        weights,
        capacity
    )

    # Obtain the maximum value from the bottom right table cell
    maximum_value = dp[number_of_items][capacity]

    # Display the table and final solution
    display_dp_table(dp)

    display_output(
        names,
        weights,
        values,
        selected_indexes,
        maximum_value
    )

# Runs main only when the file is executed directly
if __name__ == "__main__":
    main()