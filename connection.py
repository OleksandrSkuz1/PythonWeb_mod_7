from sqlalchemy import create_engine

USER = 'alex'
PASSWORD = 'alex'
HOST = 'localhost'
DATABASE = 'postgres-container'
PORT = 5432

URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(URL, echo=True)

#C:\Users\admin\Desktop\GoIT\Home Work WEB\MODUL_7