from unittest import TestCase
from phash import image_digest, cross_correlation

class RookTestCase(TestCase):
    black_rooks = ["/Users/tlehman/src/chess-parser/tmp/001/21.jpg", "/Users/tlehman/src/chess-parser/tmp/007/35.jpg", "/Users/tlehman/src/chess-parser/tmp/008/13.jpg", "/Users/tlehman/src/chess-parser/tmp/019/30.jpg"]
    white_rook = "/Users/tlehman/src/chess-parser/tmp/008/47.jpg"

    def test_all_phash_values(self):
      black_rook_pairs = filter(lambda p: p[0]!=p[1], [(x,y) for x in black_knights for y in black_knights])
      # cross-correlation falues for all pairs of black rooks
      map(lambda p: cross_correlation(image_digest(p[0]), image_digest(p[1])), black_rook_pairs)

      # cross_correlation 
