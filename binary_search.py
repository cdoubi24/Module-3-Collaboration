binary_search = lambda arr, low, high, x: (
    low if low == high and arr[low] == x else
    -1 if low > high else
    binary_search(arr, mid + 1, high, x) if arr[mid] < x else
    binary_search(arr, low, mid - 1, x) if arr[mid] > x else
    mid
)

# Example usage:
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    x = 7
    print(binary_search(arr, 0, len(arr) - 1, x))
