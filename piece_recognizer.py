from phash import image_digest, cross_correlation
from os import path, listdir

def generate_ref_images():
    """ canonical piece images used for reference (hence the name) """
    piece_colors = ['W','B']
    piece_names = ['K','Q','N','B','R','P']
    bg_colors = ['L','D']
    ref_names = ['_L', '_D'] + map(lambda t: ''.join(t), [(c,p,b) for c in piece_colors for p in piece_names for b in bg_colors])
    ref_filenames = map(lambda rn: "ref/%s.jpg" % rn, ref_names)
    return ref_filenames

ref_images = map(lambda filename: (filename, image_digest(filename)), generate_ref_images())

def piece_recognizer(filename):
    """ take filename of piece, compare with ref table,
    find one of maximum correlation, return ref name """
    # piece digest (pd)
    pd = image_digest(filename)
    # compute cross correlations
    ccs = map(lambda ref_im: (ref_im[0], cross_correlation(pd, ref_im[1])), ref_images)
    return max(ccs, key=lambda item: item[1])


test_inputs = map(lambda s: "tmp/001/%s" % s, listdir("tmp/001"))
for test_input in test_inputs:
    name, value = piece_recognizer(test_input)
    print "%s = %s  (%f match)" % (test_input, name, value)

