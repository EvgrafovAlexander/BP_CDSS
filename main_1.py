from sql_module import Connection
from doc_module import DocFiles

database = Connection('postgres', '12345')

database.create_tables()

database.insert_into('Patients', (1, 'Alexander', 'Petrov', '12-12-1988'))
database.insert_into('Patients', (2, 'Alexey', 'Ivanov', '12-12-1988'))

database.select_from(table_name="Patients")

database.drop_tables()



files = DocFiles()
files.read_docs()

print(files.docs)

print(DocFiles.read_docs.__doc__)
