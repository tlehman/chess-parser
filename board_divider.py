from unittest import TestCase
import os
import shutil
from image_tiler import ImageTiler

def board_divider(filename_of_board_image):
    """ Takes a board and divides it into 64 images, stores in files,
    each created image named after its coordinates, like b4 and e7. """
    dir_name = filename_of_board_image.split(".")[0].replace("img", "tmp")
    os.mkdir(dir_name)
    tiler = ImageTiler(filename_of_board_image)
    for i in range(8):
        for j in range(8):
            filename_of_tile = os.path.join(dir_name, "%d%d.jpg" % (i,j))
            tiler.get_at_coords(i,j).save(filename_of_tile)



def create_or_clear_tmp_dir():
    # create temp directory if doesn't exist
    if os.path.exists("tmp/"):
        shutil.rmtree("tmp/")
    os.mkdir("tmp/")

class BoardDividerTest(TestCase):
    def board_divider_files_created(self, board_name):
        """ Tests that the 64 files are created, from a1 all
        the way to h8 """

        board_tile_dir = "tmp/%s/" % board_name
        board_img_name = "img/%s.jpg" % board_name

        board_divider(board_img_name)
        # Chess boards are 8x8, so there are 64 positions
        assert len(os.listdir(board_tile_dir)) == 64

    def test_several_board_divisions(self):
        create_or_clear_tmp_dir()
        for i in range(47):
            board_name = str(i).rjust(3,'0')
            self.board_divider_files_created(board_name)
