import psycopg2

tables = ['Patients',
          'Clinical_blood_test',
          'Clinical_urine_test',
          'Biochemical_blood_test',
          'Coagulation_test',
          'Sputum_test']

tables_create_queries = {'Patients': '''CREATE TABLE IF NOT EXISTS "Patients"
                                (   Id SERIAL PRIMARY KEY,
                                    FirstName VARCHAR(20) NOT NULL,
                                    LastName VARCHAR(25) NOT NULL,
                                    DateOfBirthday DATE
                                );''',
                         'Clinical_blood_test': '''CREATE TABLE IF NOT EXISTS "Clinical_blood_test"
                                (   Id SERIAL PRIMARY KEY,
                                    PatientId INTEGER,
                                    cbc_date DATE,
                                    rbc REAL,
                                    FOREIGN KEY (PatientId) REFERENCES "Patients" (Id)
                                );''',
                         'Clinical_urine_test': '''CREATE TABLE IF NOT EXISTS "Clinical_urine_test"
                                (   Id SERIAL PRIMARY KEY,
                                    PatientId INTEGER,
                                    cut_date DATE,
                                    FOREIGN KEY (PatientId) REFERENCES "Patients" (Id)
                                );''',
                         'Biochemical_blood_test': '''CREATE TABLE IF NOT EXISTS "Biochemical_blood_test"
                                (   Id SERIAL PRIMARY KEY,
                                    PatientId INTEGER,
                                    bba_date DATE,
                                    FOREIGN KEY (PatientId) REFERENCES "Patients" (Id)
                                );''',
                         'Coagulation_test': '''CREATE TABLE IF NOT EXISTS "Coagulation_test"
                                (   Id SERIAL PRIMARY KEY,
                                    PatientId INTEGER,
                                    bct_date DATE,
                                    FOREIGN KEY (PatientId) REFERENCES "Patients" (Id)
                                );''',
                         'Sputum_test': '''CREATE TABLE IF NOT EXISTS "Sputum_test"
                                (   Id SERIAL PRIMARY KEY,
                                    PatientId INTEGER,
                                    ace_date DATE,
                                    FOREIGN KEY (PatientId) REFERENCES "Patients" (Id)
                                );'''
                         }

tables_insert_queries = {'Patients': """ INSERT INTO "Patients" (Id, FirstName, LastName, DateOfBirthday)
                                                                    VALUES (%s,%s,%s,%s)""",
                         'Clinical_blood_test': """ INSERT INTO "Clinical_blood_test" (Id, PatientId, cbc_date, rbc) 
                                                                    VALUES (%s,%s,%s,%s)""",
                         'Clinical_urine_test': """ INSERT INTO "Clinical_urine_test" (Id, PatientId, cut_date) 
                                                                    VALUES (%s,%s,%s)""",
                         'Biochemical_blood_test': """ INSERT INTO "Biochemical_blood_test" (Id, PatientId, bba_date) 
                                                                    VALUES (%s,%s,%s)""",
                         'Coagulation_test': """ INSERT INTO "Coagulation_test" (Id, PatientId, bct_date) 
                                                                    VALUES (%s,%s,%s)""",
                         'Sputum_test': """ INSERT INTO "Sputum_test" (Id, PatientId, ace_date) 
                                                                    VALUES (%s,%s,%s)"""
                        }


class Connection:
    def __init__(self, user, password, dbname='bpd_system_db', host='localhost'):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        for name_table in tables:
            self.cursor.execute(tables_create_queries[name_table])
            self.conn.commit()

    def drop_tables(self):
        self.cursor.execute('''DROP TABLE "Clinical_blood_test";''')
        self.conn.commit()
        self.cursor.execute('''DROP TABLE "Clinical_urine_test";''')
        self.conn.commit()
        self.cursor.execute('''DROP TABLE "Biochemical_blood_test";''')
        self.conn.commit()
        self.cursor.execute('''DROP TABLE "Coagulation_test";''')
        self.conn.commit()
        self.cursor.execute('''DROP TABLE "Sputum_test";''')
        self.conn.commit()
        self.cursor.execute('''DROP TABLE "Patients";''')
        self.conn.commit()

    def insert_into(self, table_name, record_to_insert):
        postgres_insert_query = tables_insert_queries[table_name]
        self.cursor.execute(postgres_insert_query, record_to_insert)
        self.conn.commit()

    def select_from(self, table_name):
        self.cursor.execute('''SELECT * FROM "%s"''' % table_name)
        self.conn.commit()
        for row in self.cursor:
            print(row)
