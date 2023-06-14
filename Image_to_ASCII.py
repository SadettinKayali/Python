import pywhatkit

import os 
ImageFile = os.path.join(os.path.dirname(__file__), 'Papatya.jfif')
assert os.path.exists(ImageFile)

ImageTxt = os.path.join(os.path.dirname(__file__), 'Papatya.txt')
assert os.path.exists(ImageTxt)

pywhatkit.image_to_ascii_art(ImageFile,ImageTxt)


