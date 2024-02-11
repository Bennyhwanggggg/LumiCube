def rotate_90_degrees_clockwise(array):
    # Transpose the array
    transposed_array = [list(row) for row in zip(*array)]

    # Reverse each row to get the final rotated array
    rotated_array = [list(reversed(row)) for row in transposed_array]

    return rotated_array

if __name__ == "__main__":
    # Example usage:
    original_array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotated_array = rotate_90_degrees_clockwise(original_array)

    # Print the rotated array
    for row in rotated_array:
        print(row)
