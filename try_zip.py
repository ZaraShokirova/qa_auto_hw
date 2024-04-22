import zipfile

zip_file = zipfile.ZipFile('resource/Hello.zip')
print(zip_file.namelist())
text = zip_file.read('Hello.txt')
print(text)
zip_file.close()

with zipfile.ZipFile('resource/Hello.zip') as hellozip:
    hellozip.extract('Hello.txt')
