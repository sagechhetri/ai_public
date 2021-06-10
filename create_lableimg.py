print("labelImg will be cloned at the folder you provide. You can then start labeling images.")
print("\tA new window will pop open. Select dir to open all images ")
print("\tMake sure to close the window when done else script will continue to run")

import os
folder=input("folder name:")
LABELIMG_PATH = os.path.join(folder, 'labelimg')
!pip install --upgrade pyqt5 lxml
if not os.path.exists(LABELIMG_PATH):
    !mkdir {LABELIMG_PATH}
    !git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}

if os.name == 'posix':
    !make qt5py3
if os.name =='nt':
    !cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc

!cd {LABELIMG_PATH} && python labelImg.py
