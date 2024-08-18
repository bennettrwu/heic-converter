from PIL import Image
import piexif
from os import listdir, path, makedirs
from tqdm import tqdm
from pillow_heif import register_heif_opener

register_heif_opener()

in_directory = input('Input directory: ')
out_directory = input('Output directory: ')
file_ext = input('Output extension (jpg, png, bmp, ...): ')

makedirs(out_directory, exist_ok=True)

progress_bar = tqdm(
    sorted(
        filter(
            lambda f: f.lower().endswith('.heic'),
            listdir(in_directory)
        )
    )
)

import time
for f in progress_bar:
    progress_bar.set_description(f'Working on: "{f}"')

    in_file = path.join(in_directory, f)
    img = Image.open(in_file)
    exif_dict = piexif.load(img.info["exif"])
    exif_bytes = piexif.dump(exif_dict)
    
    out_file = path.join(out_directory, f[:-4] + file_ext)
    img.save(out_file, exif=exif_bytes)
