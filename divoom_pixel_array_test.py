import unittest
import divoom_pixel_array

class TestDivoomAuraBoxPixelArray(unittest.TestCase):

    TEST_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 0,
                 0, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12,
                 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 0, 12, 12, 12,
                 12, 12, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 12, 0, 0,
                 12, 12, 12, 0, 0, 0, 12, 12, 0, 0, 12, 12, 12, 0, 0, 12, 12,
                 12, 0, 0, 0, 12, 12, 0]

    TEST_DIVOOM = [0, 0, 0, 0, 4, 0, 0, 0, 64, 4, 0, 0, 0, 64, 4, 0, 0, 0, 68,
                   4, 0, 0, 64, 68, 4, 0, 0, 68, 68, 4, 0, 0, 64, 68, 4, 0, 64,
                   0, 68, 4, 0, 68, 0, 68, 4, 64, 68, 0, 64, 4]

    def test_pixel_array_to_divoom(self):
        divoom_data = divoom_pixel_array.pixel_array_to_divoom(self.TEST_BITS)
        self.assertEquals(divoom_data, self.TEST_DIVOOM)