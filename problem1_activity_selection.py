# Ask the user for an integer that meets the minimum value
def get_integer_input(message, minimum):
    while True:
        try:
            # Attempt to convert the user's input into an integer
            number = int(input(message))

            # Return the number if it meets the minimum requirement
            if number >= minimum:
                return number

            print("Please enter a number of at least", minimum)

        except ValueError:
            print("Please enter a valid whole number.")

# Collect the start and finish times of each activity
def get_activity_details(number_of_activities):
    activities = []

    for activity_number in range(1, number_of_activities + 1):
        print("\nActivity", activity_number)

        # Allow the start time to be 0 or greater
        start_time = get_integer_input(
            "Enter the start time: ",
            0
        )

        while True:
            # Allow the finish time to be 0 or greater
            finish_time = get_integer_input(
                "Enter the finish time: ",
                0
            )

            # The finish time must be later than the start time
            if finish_time > start_time:
                break

            print("The finish time must be greater than the start time.")

        # Store the activity name, start time, and finish time
        activity = [
            "Activity " + str(activity_number),
            start_time,
            finish_time
        ]

        activities.append(activity)

    return activities

# Sort the activities from earliest to latest finish time
def sort_by_finish_time(activities):
    number_of_activities = len(activities)

    # Move through every position except the final position
    for current_position in range(number_of_activities - 1):

        # Assume the current activity has the earliest finish time
        earliest_position = current_position

        # Check all activities after the current position
        for next_position in range(
            current_position + 1,
            number_of_activities
        ):
            # Compare the finish times at index 2
            if activities[next_position][2] < activities[earliest_position][2]:
                # Store the position of the earlier finishing activity
                earliest_position = next_position

        # Swap the current activity with the earliest finishing activity
        temporary = activities[current_position]
        activities[current_position] = activities[earliest_position]
        activities[earliest_position] = temporary

# Select the maximum number of non overlapping activities
def select_activities(activities):
    selected_activities = []

    # Select the first activity because it finishes earliest
    selected_activities.append(activities[0])

    # Store the finish time of the last selected activity
    last_finish_time = activities[0][2]

    # Check every remaining activity
    for position in range(1, len(activities)):
        current_activity = activities[position]
        current_start_time = current_activity[1]

        # Select it if it starts at or after the last activity finishes
        if current_start_time >= last_finish_time:
            selected_activities.append(current_activity)

            # Update the finish time for the next comparison
            last_finish_time = current_activity[2]

    return selected_activities

# Display the activities in a table
def display_activities(title, activities):
    print("\n" + title)
    print("-" * 42)
    print("Activity\t\tStart\tFinish")
    print("-" * 42)

    for activity in activities:
        print(
            activity[0] + "\t" +
            str(activity[1]) + "\t" +
            str(activity[2])
        )

# Run the main parts of the program
def main():
    print("Activity Selection Problem")

    # At least one activity is required
    number_of_activities = get_integer_input(
        "Enter the number of activities: ",
        1
    )

    # Collect the activity information
    activities = get_activity_details(number_of_activities)

    # Arrange the activities by their finish times
    sort_by_finish_time(activities)

    # Apply the greedy algorithm
    selected_activities = select_activities(activities)

    # Display the sorted activities
    display_activities(
        "Activities sorted by finish time:",
        activities
    )

    # Display the activities selected by the algorithm
    display_activities(
        "Selected non overlapping activities:",
        selected_activities
    )

    print(
        "\nMaximum number of activities:",
        len(selected_activities)
    )

# Run main only when this Python file is executed directly
if __name__ == "__main__":
    main()