import os, re, docx, datetime


def parse_doc_file(doc):
    data = dict()
    document = docx.Document(doc)

    data['text_data'] = get_text_data(document)

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
    text_data["date_of_birth"] = get_date_between_sections(r'Дата рождения:',
                                                           r'Дата поступления в стационар:',
                                                           text)

    text_data["receipt_date"] = get_date_between_sections(r'Дата поступления в стационар',
                                                          r'Дата выписки из стационара',
                                                          text)

    text_data["discharge_date"] = get_date_between_sections(r'Дата выписки из стационара',
                                                            r'Полный диагноз',
                                                            text)
    return text_data


def get_date_between_sections(beg_sec, end_sec, text):
    # ищем позиции тегов в тексте
    beg_point = re.search(beg_sec, text)
    end_point = re.search(end_sec, text)
    # 27.12.1985
    matches = re.findall(r'\d\d.\d\d.\d\d\d\d', text[beg_point.end():end_point.start()])
    if matches:
        return datetime.datetime.strptime(matches[0], '%d.%m.%Y').date()
    # 27.12.85
    matches = re.findall(r'\d\d.\d\d.\d\d', text[beg_point.end():end_point.start()])
    if matches:
        day_mon = matches[0][:-2]
        year = matches[0][-2:]
        if int(year) > 35:
            year = '19' + matches[0][-2:]
        else:
            year = '20' + matches[0][-2:]
        return datetime.datetime.strptime(day_mon + year, '%d.%m.%Y').date()
    # 1985
    matches = re.findall(r'\d\d\d\d', text[beg_point.end():end_point.start()])
    if matches:
        return datetime.datetime.strptime('01.01.' + matches[0], '%d.%m.%Y').date()
    # 85
    matches = re.findall(r'\d\d', text[beg_point.end():end_point.start()])
    if matches:
        year = matches[0]
        if int(year) > 35:
            year = '19' + matches[0]
        else:
            year = '20' + matches[0]
        return datetime.datetime.strptime('01.01.' + year, '%d.%m.%Y').date()

    return datetime.datetime.strptime("01.01.1900", '%d.%m.%Y').date()

