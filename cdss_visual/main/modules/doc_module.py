import os, docx

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


def parseDocFile():
    return {"first_name": 'Антон', "last_name": 'Семенов'}
