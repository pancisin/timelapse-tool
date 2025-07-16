import moviepy.video.io.ImageSequenceClip
import sys
import logging_custom

from image_loader import ImageLoader

logger = logging_custom.get_logger(__name__)

root_folder = "."
file_name = "output"
folder_filter = ""

if sys.argv:
    root_folder = sys.argv[1]

for idx in range(len(sys.argv)):
    arg = sys.argv[idx]
    if arg.startswith("--name"):
        file_name=sys.argv[idx + 1]
    if arg.startswith("--filter"):
        folder_filter=sys.argv[idx + 1]

loader = ImageLoader(root_folder)
image_files = loader.load(folder_filter)

logger.info(f"Generating timelapse video of {len(image_files)} images. FPS=18")

if len(image_files) > 0:
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=18)
    clip.write_videofile(f"{file_name}.mp4")
else:
    logger.error("No images found!")


