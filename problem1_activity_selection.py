"""
Problem 1: Activity Selection Problem using a Greedy Algorithm

AI assistance declaration:
ChatGPT was used to assist with code structure, validation, testing ideas,
and comments. The student group must verify, understand, and be able to
explain every part of the submitted program.

Important assignment requirement:
The program does NOT use Python's built-in sort() or sorted(). Activities are
ordered manually using the merge sort implementation below.
"""


class Activity:
    """Stores one activity and its original input position."""

    def __init__(self, name, start, finish, input_order):
        self.name = name
        self.start = start
        self.finish = finish
        self.input_order = input_order


# ---------------------------------------------------------------------------
# General input and output helper functions
# ---------------------------------------------------------------------------

def format_number(value):
    """Displays whole-number floats without an unnecessary decimal point."""
    if value == int(value):
        return str(int(value))
    return f"{value:g}"


def print_heading(title):
    """Prints a clear section heading for console output."""
    line = "=" * len(title)
    print(f"\n{title}\n{line}")


def print_table(headers, rows):
    """Prints a simple table without using an external formatting library."""
    widths = []

    for header in headers:
        widths.append(len(str(header)))

    for row in rows:
        for column_index in range(len(row)):
            cell_length = len(str(row[column_index]))
            if cell_length > widths[column_index]:
                widths[column_index] = cell_length

    header_cells = []
    for column_index in range(len(headers)):
        header_cells.append(str(headers[column_index]).ljust(widths[column_index]))
    print(" | ".join(header_cells))

    separator_cells = []
    for width in widths:
        separator_cells.append("-" * width)
    print("-+-".join(separator_cells))

    for row in rows:
        row_cells = []
        for column_index in range(len(row)):
            row_cells.append(str(row[column_index]).ljust(widths[column_index]))
        print(" | ".join(row_cells))


def read_integer(prompt, minimum=None, maximum=None):
    """Reads an integer and repeatedly asks until a valid value is entered."""
    while True:
        raw_value = input(prompt).strip()

        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Value must not exceed {maximum}.")
            continue

        return value


def read_finite_number(prompt):
    """Reads a finite integer or decimal number from the user."""
    while True:
        raw_value = input(prompt).strip()

        try:
            value = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # NaN is the only floating-point value that is not equal to itself.
        # The two range checks reject positive and negative infinity.
        if value != value or value == float("inf") or value == float("-inf"):
            print("Invalid input. Please enter a finite number.")
            continue

        return value


# ---------------------------------------------------------------------------
# Manual sorting logic
# ---------------------------------------------------------------------------

def comes_before(first, second):
    """
    Returns True when 'first' should appear before 'second'.

    Greedy priority:
    1. Earlier finish time
    2. Earlier start time when finish times are equal
    3. Earlier input order when both times are equal
    """
    if first.finish < second.finish:
        return True
    if first.finish > second.finish:
        return False

    if first.start < second.start:
        return True
    if first.start > second.start:
        return False

    return first.input_order <= second.input_order


def merge(left_half, right_half):
    """Manually merges two already ordered activity lists."""
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if comes_before(left_half[left_index], right_half[right_index]):
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1

    return merged


def merge_sort_activities(activities):
    """
    Manually sorts activities by greedy priority using merge sort.

    Time complexity: O(n log n)
    Extra space: O(n)
    """
    if len(activities) <= 1:
        return activities[:]

    middle = len(activities) // 2
    left_half = merge_sort_activities(activities[:middle])
    right_half = merge_sort_activities(activities[middle:])

    return merge(left_half, right_half)


# ---------------------------------------------------------------------------
# Greedy activity-selection logic
# ---------------------------------------------------------------------------

def select_activities_greedily(activities):
    """
    Selects the maximum number of mutually compatible activities.

    Greedy choice:
    After manually ordering by finish time, choose the next activity whose
    start time is at or after the finish time of the last selected activity.

    The earliest-finishing compatible activity leaves the greatest remaining
    time for future activities, which makes this greedy strategy optimal for
    the unweighted activity-selection problem.
    """
    ordered_activities = merge_sort_activities(activities)
    selected = []
    decisions = []
    last_selected = None

    for stage_index in range(len(ordered_activities)):
        current = ordered_activities[stage_index]

        if last_selected is None:
            selected.append(current)
            last_selected = current
            decision = "SELECT"
            reason = "First candidate after ordering by earliest finish time."

        elif current.start >= last_selected.finish:
            selected.append(current)
            decision = "SELECT"
            reason = (
                f"Start {format_number(current.start)} >= last selected finish "
                f"{format_number(last_selected.finish)}."
            )
            last_selected = current

        else:
            decision = "REJECT"
            reason = (
                f"Start {format_number(current.start)} < last selected finish "
                f"{format_number(last_selected.finish)}; overlaps with "
                f"{last_selected.name}."
            )

        decisions.append((stage_index + 1, current, decision, reason))

    return ordered_activities, selected, decisions


# ---------------------------------------------------------------------------
# Program input and result presentation
# ---------------------------------------------------------------------------

def enter_activities():
    """Collects and validates a custom set of activities from the user."""
    print_heading("CUSTOM ACTIVITY INPUT")
    activity_count = read_integer("Number of activities: ", minimum=1, maximum=1000)
    activities = []

    for activity_index in range(activity_count):
        print(f"\nActivity {activity_index + 1}")
        default_name = f"A{activity_index + 1}"
        name = input(f"Name [{default_name}]: ").strip()

        if name == "":
            name = default_name

        start = read_finite_number("Start time: ")

        while True:
            finish = read_finite_number("Finish time: ")
            if finish <= start:
                print("Finish time must be greater than start time.")
            else:
                break

        activities.append(Activity(name, start, finish, activity_index))

    return activities


def display_problem_input(activities):
    """Displays the activities in their original input order."""
    print_heading("ORIGINAL ACTIVITIES")
    rows = []

    for activity in activities:
        rows.append([
            activity.input_order + 1,
            activity.name,
            format_number(activity.start),
            format_number(activity.finish),
            format_number(activity.finish - activity.start),
        ])

    print_table(["Input #", "Activity", "Start", "Finish", "Duration"], rows)


def display_ordered_activities(ordered_activities):
    """Displays the manually sorted order used by the greedy algorithm."""
    print_heading("GREEDY PRIORITY ORDER")
    print("Rule: earliest finish time first; ties use earlier start time.")
    rows = []

    for position in range(len(ordered_activities)):
        activity = ordered_activities[position]
        rows.append([
            position + 1,
            activity.name,
            format_number(activity.start),
            format_number(activity.finish),
        ])

    print_table(["Priority", "Activity", "Start", "Finish"], rows)


def display_greedy_stages(decisions):
    """Shows the greedy choice and justification at every stage."""
    print_heading("GREEDY CHOICE AT EACH STAGE")
    rows = []

    for stage, activity, decision, reason in decisions:
        rows.append([
            stage,
            activity.name,
            f"[{format_number(activity.start)}, {format_number(activity.finish)})",
            decision,
            reason,
        ])

    print_table(["Stage", "Candidate", "Time Interval", "Decision", "Reason"], rows)


def display_final_solution(selected, total_activity_count):
    """Displays the selected schedule and a concise solution summary."""
    print_heading("FINAL OPTIMAL SCHEDULE")
    rows = []

    for position in range(len(selected)):
        activity = selected[position]
        rows.append([
            position + 1,
            activity.name,
            format_number(activity.start),
            format_number(activity.finish),
        ])

    print_table(["Order", "Selected Activity", "Start", "Finish"], rows)

    selected_names = []
    for activity in selected:
        selected_names.append(activity.name)

    print(f"\nSelected path: {' -> '.join(selected_names)}")
    print(f"Maximum compatible activities selected: {len(selected)}")
    print(f"Activities rejected because of conflicts: {total_activity_count - len(selected)}")
    print("Time complexity: O(n log n) for manual merge sort + O(n) selection scan.")
    print("Why suitable: choosing the compatible activity that finishes earliest")
    print("leaves the most time available for all remaining activities.")


def solve_and_display(activities):
    """Runs the complete algorithm and displays all required output."""
    display_problem_input(activities)
    ordered, selected, decisions = select_activities_greedily(activities)
    display_ordered_activities(ordered)
    display_greedy_stages(decisions)
    display_final_solution(selected, len(activities))
    return selected


# ---------------------------------------------------------------------------
# Sample data and automated validation tests
# ---------------------------------------------------------------------------

def build_activities(raw_activities):
    """Converts test data tuples into Activity objects."""
    activities = []

    for index in range(len(raw_activities)):
        name, start, finish = raw_activities[index]
        activities.append(Activity(name, float(start), float(finish), index))

    return activities


def sample_activities():
    """Returns the classic activity-selection sample data set."""
    return build_activities([
        ("A1", 1, 4),
        ("A2", 3, 5),
        ("A3", 0, 6),
        ("A4", 5, 7),
        ("A5", 3, 9),
        ("A6", 5, 9),
        ("A7", 6, 10),
        ("A8", 8, 11),
        ("A9", 8, 12),
        ("A10", 2, 14),
        ("A11", 12, 16),
    ])


def selections_match(selected, expected_names):
    """Checks whether a test produced the expected selected activity names."""
    if len(selected) != len(expected_names):
        return False

    for index in range(len(selected)):
        if selected[index].name != expected_names[index]:
            return False

    return True


def run_automated_tests():
    """
    Runs several deterministic tests covering normal and edge cases.

    These tests strengthen validation without replacing manual understanding
    or explanation of the algorithm.
    """
    print_heading("AUTOMATED VALIDATION TESTS")

    tests = [
        (
            "Classic overlapping data",
            [
                ("A1", 1, 4), ("A2", 3, 5), ("A3", 0, 6),
                ("A4", 5, 7), ("A5", 3, 9), ("A6", 5, 9),
                ("A7", 6, 10), ("A8", 8, 11), ("A9", 8, 12),
                ("A10", 2, 14), ("A11", 12, 16),
            ],
            ["A1", "A4", "A8", "A11"],
        ),
        (
            "All activities compatible",
            [("B1", 0, 2), ("B2", 2, 4), ("B3", 4, 6), ("B4", 6, 8)],
            ["B1", "B2", "B3", "B4"],
        ),
        (
            "All activities overlap",
            [("C1", 0, 10), ("C2", 1, 9), ("C3", 2, 8), ("C4", 3, 7)],
            ["C4"],
        ),
        (
            "Equal finish-time tie",
            [("D1", 1, 4), ("D2", 0, 4), ("D3", 4, 6), ("D4", 6, 9)],
            ["D2", "D3", "D4"],
        ),
        (
            "Unordered decimal times",
            [("E1", 4.5, 7.0), ("E2", 0.0, 1.5), ("E3", 1.5, 3.25), ("E4", 3.25, 4.5)],
            ["E2", "E3", "E4", "E1"],
        ),
        (
            "Single activity",
            [("F1", 10, 12)],
            ["F1"],
        ),
    ]

    result_rows = []
    passed_count = 0

    for test_index in range(len(tests)):
        test_name, raw_activities, expected_names = tests[test_index]
        activities = build_activities(raw_activities)
        _, selected, _ = select_activities_greedily(activities)

        actual_names = []
        for activity in selected:
            actual_names.append(activity.name)

        passed = selections_match(selected, expected_names)
        if passed:
            passed_count += 1
            status = "PASS"
        else:
            status = "FAIL"

        result_rows.append([
            test_index + 1,
            test_name,
            " -> ".join(expected_names),
            " -> ".join(actual_names),
            status,
        ])

    print_table(["#", "Test Case", "Expected", "Actual", "Status"], result_rows)
    print(f"\nTests passed: {passed_count}/{len(tests)}")

    if passed_count == len(tests):
        print("All automated validation tests passed.")
    else:
        print("At least one test failed. Review the algorithm before submission.")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def display_menu():
    """Displays the program's main menu."""
    print_heading("ACTIVITY SELECTION - GREEDY ALGORITHM")
    print("1. Enter a custom activity set")
    print("2. Run the classic sample problem")
    print("3. Run automated validation tests")
    print("4. Exit")


def main():
    """Controls the complete console-based program."""
    while True:
        display_menu()
        choice = read_integer("Choose an option (1-4): ", minimum=1, maximum=4)

        if choice == 1:
            activities = enter_activities()
            solve_and_display(activities)
            input("\nPress Enter to return to the main menu...")

        elif choice == 2:
            solve_and_display(sample_activities())
            input("\nPress Enter to return to the main menu...")

        elif choice == 3:
            run_automated_tests()
            input("\nPress Enter to return to the main menu...")

        else:
            print("\nProgram ended.")
            break


if __name__ == "__main__":
    main()
