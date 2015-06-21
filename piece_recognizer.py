from phash import image_digest, cross_correlation
from os import path

def piece_recognizer(filename):
    """ take filename of piece, compare with ref table,
    find one of maximum correlation, return ref name """
    ref_images = map(image_digest, ref_images())
    # piece digest (pd)
    pd = image_digest(filename)
    # compute cross correlations
    ccs = map(lambda ref_im: (ref_im, cross_correlation(pd, ref_im)), ref_images)
    print(ccs)
    return max(ccs, key=lambda item: item[1])



def ref_images():
    """ canonical piece images used for reference (hence the name) """
    piece_colors = ['W','B']
    piece_names = ['K','Q','N','B','R','P']
    bg_colors = ['L','D']
    ref_names = map(lambda t: ''.join(t), [(c,p,b) for c in piece_colors for p in piece_names for b in bg_colors])
    ref_filenames = map(lambda rn: "ref/%s.jpg" % rn, ref_names)
    return ref_filenames

