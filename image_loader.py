import os
import logging_custom
from imageio.v2 import imread

logger = logging_custom.get_logger(__name__)

class ImageLoader:
    def __init__(self, root_folder):
        self.__root_path = root_folder

    def __flatten(self, xss):
        return [x for xs in xss for x in xs]

    def __filter_size(self, path_list):
        if len(path_list) == 0:
            return []

        size = imread(path_list[0]).shape
        result = []
        for path in path_list:
            cur_size = imread(path).shape
            if cur_size == size:
                result.append(path)

        return result

    def load(self, folder_filter: str):
        folders = [os.path.join(self.__root_path, f) for f in os.listdir(self.__root_path) if
                   os.path.isdir(os.path.join(self.__root_path, f)) and (
                               len(folder_filter) == 0 or f.startswith(folder_filter))]

        if len(folders) == 0:
            folders = [self.__root_path]

        logger.info(f"Folders matching query: {len(folders)}, path: {self.__root_path}")

        image_files = []

        for folder in folders:
            folder_images = [os.path.join(folder, img) for img in os.listdir(folder) if img.endswith(".jpg")]
            image_files.append(folder_images)

        image_files = self.__flatten(image_files)
        images_count = len(image_files)

        logger.info(f"Found {len(image_files)} images. Attempting to unify image sizes.")

        image_files = self.__filter_size(image_files)

        if images_count != len(image_files):
            logger.warn(f"Lost {images_count - len(image_files)} images after filtering.")

        image_files.sort()

        return image_files
