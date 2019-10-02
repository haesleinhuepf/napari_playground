
from skimage import data
import napari

# create Qt GUI context
with napari.gui_qt():
    # create a Viewer and add an image
    viewer = napari.view_image(data.astronaut(), rgb=True)

import vispy
print(vispy.sys_info())
