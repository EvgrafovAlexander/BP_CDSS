import os, docx


path = os.getcwd()

print(path)

file = docx.Document(path + '/' + 'patient_1.docx')

print(file)
print(type(file))

print(type(file) == "class")

print(file.paragraphs[0].text)