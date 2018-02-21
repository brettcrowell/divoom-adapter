import divoom_image
import time
from PIL import Image

class DivoomExamples:

    def show_files(self, protocol, device, filelist, delay=1):
        for f in filelist:
            bytes = divoom_image.image_to_divoom(f)
            pkg = protocol.create_image_package(bytes)
            device.send(pkg)
            time.sleep(delay)

    def blink(self, protocol, device, filename):
        for c in range(1, 20):
            f = ""
            if (c % 2 == 0):
                f = filename
            else:
                f = "images/black.bmp"
            bytes = divoom_image.image_to_divoom(f)
            pkg = protocol.create_image_package(bytes)
            device.send(pkg)
            time.sleep(0.5)

    def firework(self, protocol, device):
        basename = "images/firework"
        firework_files = []
        for n in range(1, 9):
            firework_files.append(basename + str(n) + ".bmp")
        firework_files.append("images/black.bmp")
        self.show_files(protocol, device, firework_files, 0.3)

    def firework_predefined(self, protocol, device):
        basename = "images/firework"
        firework_files = []
        for n in range(1, 9):
            firework_files.append(basename + str(n) + ".bmp")
        raw_data_packages = []
        for f in firework_files:
            bytes = divoom_image.image_to_divoom(f)
            raw_data_packages.append(bytes)
        pkgs = protocol.create_animation_packages(raw_data_packages, 0)
        for i in range(0, len(pkgs)):
            device.send(pkgs[i])

    def hello_world(self, protocol, device):
        img = divoom_image.draw_text_to_image(text="HELLO WORLD", color=divoom_image.BMP_YELLOW, size=(70, 10))
        sliced_images = divoom_image.horizontal_slices(img)
        # create divoom packages
        raw_data_packages = []
        for img in sliced_images:
            raw_data_packages.append(divoom_image.to_divoom_data(img))
        # create BT divoom packages
        pkgs = protocol.create_animation_packages(raw_data_packages, 1)
        for i in range(0, len(pkgs)):
            device.send(pkgs[i])

    # ways
    # 1 horizontal from left to right
    # 2 vertical from upper to lower
    # 3 horizontal from right to left
    # 4 vertical from lower to upper
    def old_to_new(self, protocol, device, old_img, new_img, way=1):

        sliced_images = divoom_image.scroll_between(old_img, new_img, way)
        pkgs = []
        # prepare the data before sending it
        for img in sliced_images:
            img_raw_bytes = divoom_image.to_divoom_data(img)
            img_bytes = protocol.create_image_package(img_raw_bytes)
            pkgs.append(img_bytes)
        # send single images to divoom
        for pkg in pkgs:
            device.send(pkg)
            time.sleep(0.1)

    def scroll_sequence(self, protocol, device):
        img_1 = Image.open("images/example7.bmp")
        img_2 = Image.open("images/example9.bmp")
        img_3 = Image.open("images/firework6.bmp")
        img_4 = Image.open("images/example3.bmp")
        img_5 = Image.open("images/example5.bmp")

        device.send(protocol.create_temp_package())
        time.sleep(1)
        first_img_raw_bytes = divoom_image.to_divoom_data(img_1)
        first_img_bytes = protocol.create_image_package(first_img_raw_bytes)
        device.send(first_img_bytes)
        time.sleep(4)

        self.old_to_new(protocol, device, img_1, img_2, 1)
        time.sleep(1)
        self.old_to_new(protocol, device, img_2, img_3, 2)
        time.sleep(1)
        self.old_to_new(protocol, device, img_3, img_4, 3)
        time.sleep(1)
        self.old_to_new(protocol, device, img_4, img_5, 4)