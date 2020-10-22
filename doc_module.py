import os, docx, datetime
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


path = "C:\\Users\\Arthur\\Bronchopulmonary_system\\raw_data_doc\\patient_6.docx"

#path = "/Users/needmoredata/Documents/Programming/Repositories/pycharm_prj/BP_CDSS/Patients_data/patient_18.docx"

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

#print(doc)

text = ''
for paragraph in doc.paragraphs:
    text += paragraph.text + '\n'

print(text)
import re


def find_date_between_sections(re_sec1, re_sec2, text):
    # ищем позиции тегов в тексте
    beg_point = re.search(re_sec1, text)
    end_point = re.search(re_sec2, text)

    matches = re.findall(r'\d\d.\d\d.\d\d\d\d', text[beg_point.end():end_point.start()])
    if matches:
        return datetime.datetime.strptime(matches[0], '%d.%m.%Y').date()

    matches = re.findall(r'\d\d.\d\d.\d\d', text[beg_point.end():end_point.start()])
    if matches:
        day_mon = matches[0][:-2]
        year = matches[0][-2:]
        if int(year) > 35:
            year = '19' + matches[0][-2:]
        else:
            year = '20' + matches[0][-2:]
        return datetime.datetime.strptime(day_mon + year, '%d.%m.%Y').date()

    matches = re.findall(r'\d\d\d\d', text[beg_point.end():end_point.start()])
    if matches:
        return datetime.datetime.strptime('01.01.' + matches[0], '%d.%m.%Y').date()

    matches = re.findall(r'\d\d', text[beg_point.end():end_point.start()])
    if matches:
        year = matches[0]
        if int(year) > 35:
            year = '19' + matches[0]
        else:
            year = '20' + matches[0]
        return datetime.datetime.strptime('01.01.' + year, '%d.%m.%Y').date()

    return datetime.datetime.strptime("01.01.1900", '%d.%m.%Y').date()







def get_diagnosis(diag, text):
    diag_sec = {'base':
                [[r'Основной:', r'Осложнение:'],
                 [r'Основной:', r'Осложнения:'],
                 [r'Основной:', r'Сопутствующий:'],
                 [r'Основной:', r'Сопутствующие:'],
                 [r'Основной:', r'Госпитализирован'],
                 [r'Основной:', r'Диагностические'],],
                'complication':
                [[r'Осложнение:', r'Сопутствующий:'],
                 [r'Осложнение:', r'Сопутствующие:'],
                 [r'Осложнения:', r'Сопутствующий:'],
                 [r'Осложнения:', r'Сопутствующие:'],
                 [r'Осложнение:', r'Госпитализирован'],
                 [r'Осложнение:', r'Диагностические'],],
                'accompanying':
                [[r'Сопутствующий:', r'Госпитализирован'],
                 [r'Сопутствующий:', r'Диагностические'],],
                }
    for point in diag_sec[diag]:
        diagnosis_text = find_text_between_sections(point[0], point[1], text)
        if diagnosis_text:
            return diagnosis_text
    return 'Нет'


def find_text_between_sections(re_sec1, re_sec2, text):
    beg_point = re.search(re_sec1, text)
    end_point = re.search(re_sec2, text)
    if beg_point and end_point:
        return text[beg_point.end():end_point.start()]
    else:
        return None


#print(find_date_between_sections(r'Дата рождения:', r'Дата поступления в стационар:', text))
#print(find_date_between_sections(r'Дата поступления в стационар', r'Дата выписки из стационара', text))
#print(find_date_between_sections(r'Дата выписки из стационара', r'Полный диагноз', text))

print(get_diagnosis('base', text))
print(get_diagnosis('complication', text))
print(get_diagnosis('accompanying', text))
'''
dict1 = {"first": 'f', "second": 's'}
dict2 = {"third": 't', "fourth": 'fs'}
dict1.update(dict2)
print(dict1)
'''

