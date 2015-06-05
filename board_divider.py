from unittest import TestCase
import os
import shutil

def board_divider(filename_of_board_image):
    """ Takes a board and divides it into 64 images, stores in files,
    each created image named after its coordinates, like b4 and e7. """
    dir_name = filename_of_board_image.split(".")[0].replace("img", "tmp")
    os.mkdir(dir_name)

def create_or_clear_tmp_dir():
    # create temp directory if doesn't exist
    if os.path.exists("tmp/"):
        shutil.rmtree("tmp/")
    os.mkdir("tmp/")

class BoardDividerTest(TestCase):
    def test_board_divider_files_created(self):
        """ Tests that the 64 files are created, from a1 all
        the way to h8 """

        create_or_clear_tmp_dir()
        assert os.path.exists("tmp/000/") == False

        board_divider("img/000.png")
        # Chess boards are 8x8, so there are 64 positions
        assert len(os.listdir("tmp/000/")) == 0
