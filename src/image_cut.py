import matplotlib.pyplot as plt
import numpy as np


def get_start_finish_coords(image_size, tile_size, tile_shift):
    start = np.arange(0, image_size, tile_size)
    start[1:] = start[1:] - tile_shift

    if image_size <= (start[-1] + tile_size):
        start = start[:-1]

    finish = start + tile_size
    if finish[-1] != (image_size - 1):
        start = np.append(start, image_size - tile_size - 1)
        finish = np.append(finish, image_size - 1)

    return list(zip(start, finish))


def cut_image(
        image: np.array,
        x_width: int,
        y_height: int,
        x_shift: int,
        y_shift: int
):
    if x_width < x_shift:
        raise f"x_shift must be less than x_width"

    if y_height < y_shift:
        raise f"y_shift must be less than y_height"

    image_height, image_width = image.shape[:2]

    x_pairs = get_start_finish_coords(image_width, x_width, x_shift)
    y_pairs = get_start_finish_coords(image_height, y_height, y_shift)

    tiles = []
    for x in x_pairs:
        x_s, x_f = x
        for y in y_pairs:
            y_s, y_f = y

            tiles.append(image[y_s:y_f, x_s:x_f])

    return tiles
