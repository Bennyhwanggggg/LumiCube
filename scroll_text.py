"""
Produce a word sliding effect.
Note: The API has scroll text, which is unfortunately not available/broken.
"""
import time


def char_to_2d_array(char, c = yellow):
    # Dictionary mapping English alphabet characters to their 6x3 2D array representations
    char_map = {
        'A': [
            [0, c, 0],
            [c, 0, c],
            [c, c, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c]
        ],
        'B': [
            [c, c, 0],
            [c, 0, c],
            [c, c, 0],
            [c, 0, c],
            [c, 0, c],
            [c, c, 0]
        ],
        'C': [
            [0, c, c],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0],
            [0, c, c]
        ],
        'D': [
            [c, c, 0],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, c, 0]
        ],
        'E': [
            [c, c, c],
            [c, 0, 0],
            [c, c, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, c, c]
        ],
        'F': [
            [c, c, c],
            [c, 0, 0],
            [c, c, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0]
        ],
        'G': [
            [0, c, c],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, c],
            [c, 0, c],
            [0, c, c]
        ],
        'H': [
            [c, 0, c],
            [c, 0, c],
            [c, c, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c]
        ],
        'I': [
            [c, c, c],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0],
            [c, c, c]
        ],
        'J': [
            [0, 0, c],
            [0, 0, c],
            [0, 0, c],
            [0, 0, c],
            [c, 0, c],
            [0, c, 0]
        ],
        'K': [
            [c, 0, c],
            [c, 0, c],
            [c, c, 0],
            [c, c, 0],
            [c, 0, c],
            [c, 0, c]
        ],
        'L': [
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, c, c]
        ],
        'M': [
            [c, 0, c],
            [c, c, c],
            [c, c, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c]
        ],
        'N': [
            [c, 0, c],
            [c, 0, c],
            [c, c, c],
            [c, c, c],
            [c, 0, c],
            [c, 0, c]
        ],
        'O': [
            [0, c, 0],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [0, c, 0]
        ],
        'P': [
            [c, c, 0],
            [c, 0, c],
            [c, 0, c],
            [c, c, 0],
            [c, 0, 0],
            [c, 0, 0]
        ],
        'Q': [
            [0, c, 0],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [0, c, c]
        ],
        'R': [
            [c, c, 0],
            [c, 0, c],
            [c, 0, 0],
            [c, c, 0],
            [c, 0, c],
            [c, 0, c]
        ],
        'S': [
            [0, c, c],
            [c, 0, 0],
            [c, c, 0],
            [0, 0, c],
            [0, 0, c],
            [c, c, 0]
        ],
        'T': [
            [c, c, c],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0]
        ],
        'U': [
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [0, c, 0]
        ],
        'V': [
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [0, c, 0],
            [0, c, 0]
        ],
        'W': [
            [c, 0, c],
            [c, 0, c],
            [c, 0, c],
            [c, c, c],
            [c, c, c],
            [c, 0, c]
        ],
        'X': [
            [c, 0, c],
            [c, 0, c],
            [0, c, 0],
            [0, c, 0],
            [c, 0, c],
            [c, 0, c]
        ],
        'Y': [
            [c, 0, c],
            [c, 0, c],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0],
            [0, c, 0]
        ],
        'Z': [
            [c, c, c],
            [0, 0, c],
            [0, c, 0],
            [c, 0, 0],
            [c, 0, 0],
            [c, c, c]
        ],
        ' ': [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]
        ],

    }
    return char_map[char]

def string_to_2d_array(text):
    # Convert a string to a 2D array representation containing all characters with extra 0s on first and last row
    result = [[0] * (len(text) * 4 + 2) for _ in range(8)]
    for i, char in enumerate(text):
        char_array = char_to_2d_array(char)
        for j, row in enumerate(char_array):
            result[j + 1][i * 4 + 1:i * 4 + 4] = row
    return result


def split_into_8x8_arrays(array):
    # Split the 2D array into lists of 8x8 arrays
    result = []
    num_columns = len(array[0])
    num_slices = (num_columns + 7) // 8  # Ceiling division to get the number of slices needed
    for i in range(num_slices):
        start_column = i * 8
        end_column = min((i + 1) * 8, len(array[0]))
        slice_arrays = []
        for row in array:
            slice_arrays.append(row[start_column:end_column])
        result.append(slice_arrays)
    return result


def shift_left_by_one(array):
    # Shift all elements in the array to the left by 1 without wrapping around
    shifted_array = []
    for row in array:
        shifted_row = row[1:] + [0]
        shifted_array.append(shifted_row)
    return shifted_array


def rotate_90_degrees_clockwise(array):
    # Transpose the array
    transposed_array = [list(row) for row in zip(*array)]

    # Reverse each row to get the final rotated array
    rotated_array = [list(reversed(row)) for row in transposed_array]

    return rotated_array


text = "Welcome home Annie the big baby"
array = string_to_2d_array(text.upper())
current_array = array
loop_frames = len(array[0]) + 16
frame_count = 1
r = red
speed = 0.75
heart = [
    [0,0,0,0,0,0,0,0],
    [0,r,r,0,0,r,r,0],
    [r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r],
    [0,r,r,r,r,r,r,0],
    [0,0,r,r,r,r,0,0],
    [0,0,0,r,r,0,0,0],
    [0,0,0,0,0,0,0,0],
]
display.set_panel('top', heart)
while True:
    if frame_count % loop_frames == 0:
        current_array = array
    split_arrays = split_into_8x8_arrays(current_array)
    display.set_panel('left', split_arrays[0])
    display.set_panel('right', split_arrays[1])
    current_array = shift_left_by_one(current_array)
    frame_count += 1
    time.sleep(speed)
    if frame_count % 3 == 0:
        heart = rotate_90_degrees_clockwise(heart)
        display.set_panel('top', heart)


