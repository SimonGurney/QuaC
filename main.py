from PIL import Image, ImageDraw

# define the colors
b = (115, 156, 191)
n = (48, 53, 70)
y = (255, 168, 0)
w = (226, 224, 216)
r = (162, 0, 57)

# define the pattern
border_color = n
pattern = [
    [y, n, r, n, b], 
    [n, w, n, w, n], 
    [b, n, r, b, y],
    [n, w, n, w, n],
    [r, n, b, n, y],
    ]

# set the ratios
rectangle_ratio = 1.3
border_ratio = 0.2

# static rectangle_width to determine image size
rectangle_width = 300

# calculate dimensions based on ratios
border = int(border_ratio * rectangle_width)

max_cells_wide = max([len(i) for i in pattern])
pattern_width = max_cells_wide * rectangle_width
width = pattern_width + border * 2

rectangle_height = int(rectangle_width * rectangle_ratio)
pattern_height = len(pattern) * rectangle_height
height = pattern_height + border * 2

im = Image.new("RGB", (width, height), border_color)
draw = ImageDraw.Draw(im)


class rectangle:
    def __init__(self, tlx, tly, color=(100, 100, 200)):
        self.tlx = tlx
        self.tly = tly
        self.color = color

    def draw(self):
        draw.rectangle(
            (self.tlx, self.tly, self.brx, self.bry),
            fill=self.color,
            outline=self.color,
        )

    @property
    def brx(self):
        return self.tlx + rectangle_width

    @property
    def bry(self):
        return self.tly + (rectangle_width * rectangle_ratio)


# Draw pattern
starting_x = 0 + border
tly = 0 + border
for row in pattern:
    tlx = starting_x
    for cell in row:
        c = rectangle(tlx, tly, cell)
        c.draw()
        tlx = c.brx
    tly = c.bry

# Show computed quilt
im.show()
