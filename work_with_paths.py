import os

abspath = os.path.abspath('resource/hello')
print(abspath)
print(os.path.dirname(os.path.abspath('resource/hello')))

