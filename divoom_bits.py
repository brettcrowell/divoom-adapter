from divoom_image import to_

def bits_to_divoom(bits):
    '''Converts an array of 100 integers, each representing a pixel, to Divoom data'''
    result = []
    it = iter(bits)
    for i in it:
        val = to_(i, next(it))
        result.append(val)

    return result