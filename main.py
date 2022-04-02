from fire import Fire

from src.image_cut import cut_image
from utils.read import read_image


def main(image_path: str = "data/Lena.png"):
    image = read_image(image_path)
    image_tiles = cut_image(
        image=image,
        x_width=100,
        x_shift=10,
        y_height=100,
        y_shift=10
    )


if __name__ == '__main__':
    main()
