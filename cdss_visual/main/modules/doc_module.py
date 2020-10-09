import os, re, docx

'''
path = os.getcwd() + '/Patients_data'
names_of_documents = os.listdir(path)


patients_docx = []
for name_of_document in names_of_documents:
    full_path = path + '/' + name_of_document
    patients_docx.append(docx.Document(full_path))
'''


class DocFiles:
    def __init__(self):
        self.path = os.getcwd() + '/Patients_data'
        self.names_of_documents = os.listdir(self.path)

    def read_docs(self):
        """
        Выполняет чтение документов
        :return: список документов
        """
        self.docs = []
        for name_of_document in self.names_of_documents:
            self.docs.append(docx.Document(self.path + '/' + name_of_document))


def parse_doc_file_test():
    return {"first_name": 'Игорь', "last_name": 'Николаев'}


def parse_doc_file(doc):
    # выражение для поиска ФИО
    pattern = r"[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+"

    document = docx.Document(doc)

    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text + '\n'

    names = re.findall(pattern, text)[0].split()
    data = {"first_name": names[1],
            "last_name": names[0],
            "middle_name": names[2],
            }
    return data
