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

def pixel_array_to_divoom(pixels):
    '''Converts an array of 100 integers, each representing a pixel, to Divoom data'''
    result = []
    it = iter(pixels)
    for i in it:
        val = to_(i, next(it))
        result.append(val)

    return result
    return result