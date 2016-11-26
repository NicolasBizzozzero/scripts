from PIL import ImageFilter, ImageFile, Image
from os import listdir, remove
from os.path import isfile

images_extensions = ["jpg", "png", "jpeg"]


def get_blurred_image(image_name: str, intensity: int) -> Image:
    original_image = Image.open(image_name)
    return original_image.filter(ImageFilter.GaussianBlur(radius=intensity))


def save_image(image_name: str, pil_image: Image):
    pil_image.save(image_name)


def show_image(pil_image: Image):
    pil_image.show()


def get_all_images_from_current_directory() -> set:
    all_images = set()
    # List all stuff inside the current directory
    for file in listdir('.'):
        # Ignore directories
        if isfile(file):
            # Ignore non-image files
            if is_image(file):
                all_images.add(file)
    return all_images


def add_blurred_before_extension(image_name: str) -> str:
    image_name_without_extension, extension = image_name.split(".")
    return "{}_blurred.{}".format(image_name_without_extension, extension)


def is_image(filename: str) -> bool:
    filename_end = filename[-4:].lower()
    for extension in images_extensions:
        if filename_end.endswith(extension):
            return True
    return False


def main() -> int:
    number_of_images_blurred = 0
    all_images_from_current_directory = get_all_images_from_current_directory()
    for image in all_images_from_current_directory:
        save_image("bg" + str(number_of_images_blurred) + ".jpg",
                   get_blurred_image(image, intensity=2))
        remove(image)
        number_of_images_blurred += 1
    return number_of_images_blurred


if __name__ == '__main__':
    number_of_images_blurred = main()
    print("Blurred {} images.".format(number_of_images_blurred))
