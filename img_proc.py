from PIL import Image
# Red = L(eft), Yellow = D(own), Green = B(ack), White = U(p), Pink = R(ight), Blue = F(ront)
TARGET_COLORS = {"L": (169, 42, 16), "D": (204, 211, 71), "B": (85, 205, 41), "U": (244, 237, 225), "R": (251,79,108), "F": (36, 110, 174)}

def list_colors(image_file):
    image = Image.open(image_file)

    width, height = image.size
    
    image = image.load()
    x1 = int(width/10)
    x2 = int(width/3+width/10)
    x3 = int((2*width)/3+width/10)
    y1 = int(height/10)
    y2 = int(height/3+height/10)
    y3 = int((2*height)/3+height/10)
    sq = int(width/6)

    return (get_average_color(x1, y1, sq, image) + 
            get_average_color(x2, y1, sq, image) +
            get_average_color(x3, y1, sq, image) +
            get_average_color(x1, y2, sq, image) +
            get_average_color(x2, y2, sq, image) +
            get_average_color(x3, y2, sq, image) +
            get_average_color(x1, y3, sq, image) +
            get_average_color(x2, y3, sq, image) +
            get_average_color(x3, y3, sq, image))


def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

def get_average_color(x,y, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
 
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x+n+1):
        for t in range(y, y+n+1):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    
    my_color = ((r/count), (g/count), (b/count))
    differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
    differences.sort()  # sorted by the first element of inner lists
    return differences[0][1]