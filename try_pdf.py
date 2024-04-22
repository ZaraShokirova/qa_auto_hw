import pypdf

reader = pypdf.PdfReader('resource/zara123.pdf')
number_of_pages = len(reader.pages)
first_page = reader.pages[0]
text = first_page.extract_text()
print(number_of_pages)
print(first_page)
print(text)
count = 0
for image_file in first_page.images:
    with open(str(count) + image_file.name, 'wb') as fp:
        fp.write(image_file.data)
        count += 1
