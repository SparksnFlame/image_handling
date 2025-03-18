# Basic Image Handling and Processing
# Relevant Python libraries
# Python Image Library (PIL)

import os
import sys
from PIL import Image

test_image = Image.open("seabeach.jpg")

print(test_image.format, test_image.size, test_image.mode)
test_image.show()
convertim2 = test_image
convertim2 = Image.open("seabeach.jpg").convert("L")
convertim2.show()
