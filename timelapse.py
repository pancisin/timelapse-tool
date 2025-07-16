import os
import moviepy.video.io.ImageSequenceClip
from imageio.v2 import imread
import sys

def flatten(xss):
    return [x for xs in xss for x in xs]

def filter_size(path_list):
    size = imread(path_list[0]).shape
    result = []
    for path in path_list:
        cur_size = imread(path).shape
        if cur_size == size:
            result.append(path)

    print(f"Initial list: {len(path_list)}, After filtering: {len(result)}")

    return result

print(f"Arguments: {sys.argv}")

root_folder = "."

if sys.argv:
    root_folder = sys.argv[1]

folders = [os.path.join(root_folder, f) for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f)) & f.startswith('2025-01')]

image_files = []

for folder in folders:
    folder_images = [os.path.join(folder,img) for img in os.listdir(folder) if img.endswith(".jpg")]
    image_files.append(folder_images)

print(f"Folders matching query: {len(folders)}")

image_files = filter_size(flatten(image_files))

image_files.sort()

print(f"Generating timelapse video of {len(image_files)} images. FPS=18")

if len(image_files) > 0:
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=18)
    clip.write_videofile('my_video.mp4')
else: print("Error: No images found!")


