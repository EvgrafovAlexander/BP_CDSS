import os, re, docx, datetime


def parse_doc_file(doc):
    data = dict()
    document = docx.Document(doc)

    text_data = get_text_data(document)
    data['text_data'] = text_data

    return data


def get_text_data(document):
    text_data = dict()
    # выражение для поиска ФИО
    names_pattern = r"[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+"

    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text + '\n'

    names = re.findall(names_pattern, text)[0].split()

    text_data["last_name"] = names[0]
    text_data["first_name"] = names[1]
    text_data["middle_name"] = names[2]
    text_data["date_of_birth"] = datetime.datetime.strptime("21.11.1986", '%d.%m.%Y').date()

    return text_data
