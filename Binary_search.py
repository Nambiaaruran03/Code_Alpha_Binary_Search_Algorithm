def generate_range(start, end, step=2):
    if start > end:
        return []

    result = []
    while start <= end:
        result.append(start)
        start += step

    return result

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Input from the user
end = int(input("Enter the end of the range: "))  # User-specified range
if end < 0:
    print("End of the range must be a positive number.")
else:
    generated_range = generate_range(0, end)
    print("Generated Range:", generated_range)

    target = int(input("Enter the target number for binary search: "))
    result = binary_search(generated_range, target)
    if result != -1:
        print(f"Element {target} found at index {result} using binary search.")
    else:
        print(f"Element {target} not found in the generated range.")
