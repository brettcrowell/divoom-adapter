from divoom_adapter import DivoomAdapter
import divoom_image
import divoom_bits
import time
from PIL import Image

class ExampleCommands(DivoomAdapter):

    def show_bytes(self, bytes):
        pkg = self.protocol.create_image_package(bytes)
        self.device.send(pkg)

    def show_file(self, filename):
        bytes = divoom_image.image_to_divoom(filename)
        self.show_bytes(bytes)

    def show_files(self, filelist, delay=1):
        for f in filelist:
            self.show_file(f)
            time.sleep(delay)

    def show_bits(self, bits):
        bytes = divoom_bits.bits_to_divoom(bits)
        self.show_bytes(bytes)

    def blink(self, filename):
        for c in range(1, 20):
            f = ""
            if (c % 2 == 0):
                f = filename
            else:
                f = "images/black.bmp"
            bytes = divoom_image.image_to_divoom(f)
            pkg = self.protocol.create_image_package(bytes)
            self.device.send(pkg)
            time.sleep(0.5)

    def firework(self):
        basename = "images/firework"
        firework_files = []
        for n in range(1, 9):
            firework_files.append(basename + str(n) + ".bmp")
        firework_files.append("images/black.bmp")
        self.show_files(firework_files, 0.3)

    def firework_predefined(self):
        basename = "images/firework"
        firework_files = []
        for n in range(1, 9):
            firework_files.append(basename + str(n) + ".bmp")
        raw_data_packages = []
        for f in firework_files:
            bytes = divoom_image.image_to_divoom(f)
            raw_data_packages.append(bytes)
        pkgs = self.protocol.create_animation_packages(raw_data_packages, 0)
        for i in range(0, len(pkgs)):
            self.device.send(pkgs[i])

    def hello_world(self):
        img = divoom_image.draw_text_to_image(text="HELLO WORLD", color=divoom_image.BMP_YELLOW, size=(70, 10))
        sliced_images = divoom_image.horizontal_slices(img)
        # create divoom packages
        raw_data_packages = []
        for img in sliced_images:
            raw_data_packages.append(divoom_image.to_divoom_data(img))
        # create BT divoom packages
        pkgs = self.protocol.create_animation_packages(raw_data_packages, 1)
        for i in range(0, len(pkgs)):
            self.device.send(pkgs[i])

    # ways
    # 1 horizontal from left to right
    # 2 vertical from upper to lower
    # 3 horizontal from right to left
    # 4 vertical from lower to upper
    def old_to_new(self, old_img, new_img, way=1):

        sliced_images = divoom_image.scroll_between(old_img, new_img, way)
        pkgs = []
        # prepare the data before sending it
        for img in sliced_images:
            img_raw_bytes = divoom_image.to_divoom_data(img)
            img_bytes = self.protocol.create_image_package(img_raw_bytes)
            pkgs.append(img_bytes)
        # send single images to divoom
        for pkg in pkgs:
            self.device.send(pkg)
            time.sleep(0.1)

    def scroll_sequence(self):
        img_1 = Image.open("images/example7.bmp")
        img_2 = Image.open("images/example9.bmp")
        img_3 = Image.open("images/firework6.bmp")
        img_4 = Image.open("images/example3.bmp")
        img_5 = Image.open("images/example5.bmp")

        self.device.send(self.protocol.create_temp_package())
        time.sleep(1)
        first_img_raw_bytes = divoom_image.to_divoom_data(img_1)
        first_img_bytes = self.protocol.create_image_package(first_img_raw_bytes)
        self.device.send(first_img_bytes)
        time.sleep(4)

        self.old_to_new(img_1, img_2, 1)
        time.sleep(1)
        self.old_to_new(img_2, img_3, 2)
        time.sleep(1)
        self.old_to_new(img_3, img_4, 3)
        time.sleep(1)
        self.old_to_new(img_4, img_5, 4)

    def show_time(self):
        self.device.send(self.protocol.create_time_package())

    def show_temperature(self):
        self.device.send(self.protocol.create_temp_package())