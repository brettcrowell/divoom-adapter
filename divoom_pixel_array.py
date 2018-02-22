# divoom palette
# 0 = black
# 1 = red
# 2 = green
# 3 = yellow
# 4 = blue
# 5 = pink
# 6 = light blue
# 7 = white

def to_(a, b):
    '''Join every 2 (4 bit) pixels into one byte'''
    upper = b << 4
    lower = a
    return upper + lower

def from_(data):
    '''Decode Divoom data back to Pixel Array'''
    a = int(data % 8)
    b = int(data >> 4)
    return (a, b)

def pixel_array_to_divoom(pixels):
    '''Converts an array of 100 integers, each representing a pixel, to Divoom data'''
    result = []
    it = iter(pixels)
    for i in it:
        val = to_(i, next(it))
        result.append(val)

    return result

def divoom_to_pixel_array(data):
    '''Given divoom raw data returns pixel array'''
    result = []
    for d in data:
        a, b = from_(d)
        result.append(a)
        result.append(b)

    return result