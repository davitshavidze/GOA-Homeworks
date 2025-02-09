
# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

# Example(Input1, Input2 --> Output):

def area_or_perimeter(l , w):
    if l * w == l * l:
        return l * l
    else:
        return (l + w) * 2