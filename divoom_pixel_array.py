from divoom_image import to_

def pixel_array_to_divoom(pixels):
    '''Converts an array of 100 integers, each representing a pixel, to Divoom data'''
    result = []
    it = iter(pixels)
    for i in it:
        val = to_(i, next(it))
        result.append(val)

    return result