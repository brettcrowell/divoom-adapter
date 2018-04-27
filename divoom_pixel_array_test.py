import unittest
from divoom_pixel_array import pixel_array_to_divoom, divoom_to_pixel_array

class TestDivoomAuraBoxPixelArray(unittest.TestCase):

    PIXEL_ARRAY = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
                   0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
                   0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
                   1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0,
                   1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1,
                   1, 0, 0, 0, 1, 1, 0]

    DIVOOM_ENCODED = [0, 0, 0, 0, 1, 0, 0, 0, 16, 1, 0, 0, 0, 16, 1, 0, 0, 0,
                      17, 1, 0, 0, 16, 17, 1, 0, 0, 17, 17, 1, 0, 0, 16, 17, 1,
                      0, 16, 0, 17, 1, 0, 17, 0, 17, 1, 16, 17, 0, 16, 1]

    def test_pixel_array_to_divoom(self):
        encoded_pixel_array = pixel_array_to_divoom(self.PIXEL_ARRAY)
        self.assertEqual(encoded_pixel_array, self.DIVOOM_ENCODED)

    def text_divoom_to_pixel_array(self):
        decoded_divoom_data = divoom_to_pixel_array(self.DIVOOM_ENCODED)
        self.assertEqual(decoded_divoom_data, self.PIXEL_ARRAY)