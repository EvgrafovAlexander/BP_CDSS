import os, docx
import pandas as pd

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


path = "C:\\Users\\Arthur\\Bronchopulmonary_system\\raw_data_doc\\patient_18.docx"

path = "/Users/needmoredata/Documents/Programming/Repositories/pycharm_prj/BP_CDSS/Patients_data/patient_18.docx"

doc = docx.Document(path)


columns_CBC = ['cbc_date', 'rbc', 'hb', 'wbc', 'mchc',
               'esr', 'eos', 'stab', 'segm', 'lym',
               'mon', 'bas', 'rpr', 'young']
columns_CUT = ['cut_date', 'col', 'ph', 'sg', 'transp',
               'pro', 'epith', 'wbc', 'rbc', 'salt',
               'bact']
columns_BBA = ['bba_date', 'total_pro', 'creatin', 'urea', 'total_bil',
               'cholest', 'alt', 'ast', 'crp', 'potassium',
               'natr', 'not_data']
columns_BCT = ['bct_date', 'apt_time', 'ina', 'prot_index', 'fibrin', 'not_data']

columns_ACE = ['ace_date', 'color', 'nature', 'consistency', 'wbc',
               'rbc', 'epith', 'alveolar', 'bacteria', 'bk']


def word_preprocessing(text):
    if text == '':
        return 'NaN'
    return text.replace(',', '.')


def astype_df(df):
    for col in df.columns:
            if 'date' in col:
                df[col] = pd.to_datetime(df[col], format='%d.%m.%y', errors='ignore')
            df[col] = df[col].astype('float', errors='ignore')
    return df


def get_dict_tables_from_doc(doc):
    dict_tables = dict()
    for table in doc.tables:
        tab = []
        for row in table.rows:
            tab_row = []
            for cell in row.cells:
                tab_row.append(word_preprocessing(cell.text))
            tab.append(tab_row)

        for col in tab[0]:
            if   'ОАК' in col:
                dict_tables['CBC'] = astype_df(pd.DataFrame(tab[1:], columns = columns_CBC))
            elif 'ОАМ' in col:
                dict_tables['CUT'] = astype_df(pd.DataFrame(tab[1:], columns = columns_CUT))
            elif 'Б/Х' in col:
                dict_tables['BBA'] = astype_df(pd.DataFrame(tab[1:], columns = columns_BBA))
            elif 'Коагулограмма' in col:
                dict_tables['BCT'] = astype_df(pd.DataFrame(tab[1:], columns = columns_BCT))
            elif 'Мокрота' in col:
                dict_tables['ACE'] = astype_df(pd.DataFrame(tab[1:], columns = columns_ACE))
    return dict_tables

#print(get_dict_tables_from_doc(doc)['BCT'])

print(doc)

text = ''
for paragraph in doc.paragraphs:
    text += paragraph.text + '\n'

print(text)
import re


def find_date_between_sections(re_sec1, re_sec2, text):
    re_list = [
        '\d\d.\d\d.\d\d\d\d',
        '\d\d.\d\d.\d\d',
        '\d\d\d\d',
        '\d\d'
    ]
    sec1 = re.search(re_sec1, text)
    sec2 = re.search(re_sec2, text)

    matches = []
    for reg_exp in re_list:
        matches += re.findall(reg_exp, text[sec1.end():sec2.start()])

    return list(map(int, matches[0].split('.')))


print(find_date_between_sections(r'Дата рождения:', r'Дата поступления в стационар:', text))
#print(find_date_between_sections(r'Дата поступления в стационар', r'Дата выписки из стационара', text))
#print(find_date_between_sections(r'Дата выписки из стационара', r'Полный диагноз', text))
