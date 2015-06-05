from PIL import Image

class ImageTiler:
    """ Read an image, return a tile when given coordinates """
    def __init__(self, img_name):
    	self.img = Image.open(img_name)
        (width, height) = self.img.size
        self.tile_width = width/8
        self.tile_height = height/8
    	self.margin = 1

    def get_at_coords(self, tile_x, tile_y):
    	pos_x = (self.tile_width * tile_x) + (self.margin * (tile_x + 1))
    	pos_y = (self.tile_height * tile_y) + (self.margin * (tile_y + 1))
    	box = (pos_x, pos_y, pos_x + self.tile_width, pos_y + self.tile_height)
    	return self.img.crop(box)
