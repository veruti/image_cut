import os
import shutil
from pathlib import Path

from src.image_cut import cut_image
from utils.read import read_image
from utils.write import write_image

# TODO: Write README.md
def main(
        image_path: str = "data/Lena.png",
        result_path: str = "results",
        x_width=256,
        x_shift=32,
        y_height=256,
        y_shift=32
):
    image = read_image(image_path)
    image_tiles = cut_image(
        image=image,
        x_width=x_width,
        x_shift=x_shift,
        y_height=y_height,
        y_shift=y_shift
    )

    shutil.rmtree(Path(result_path).absolute(), ignore_errors=True)
    Path(result_path).absolute().mkdir(exist_ok=True)

    for num, tile in enumerate(image_tiles):
        filename = os.sep.join([result_path, f"tile_{num + 1}.png"])
        write_image(filename=filename, image=tile)


if __name__ == '__main__':
    main()
