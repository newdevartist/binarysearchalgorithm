def binary_search(sorted_list, target):
    """
    Perform a binary search on a sorted list.

    Parameters:
    sorted_list (list): A list of sorted elements.
    target: The element to search for.

    Returns:
    int: The index of the target in the sorted list, or -1 if not found.
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow

        # Check if target is present at mid
        if sorted_list[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif sorted_list[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the list
    return -1

# Example usage
if __name__ == "__main__":
    # Sorted list to search
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7

    result = binary_search(numbers, target_value)

    if result != -1:
        print(f"Element {target_value} found at index {result}.")
    else:
        print(f"Element {target_value} not found in the list.")