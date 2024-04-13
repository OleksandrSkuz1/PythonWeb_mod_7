from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


USER = 'alex'
PASSWORD = 'alex'
HOST = 'localhost'
DATABASE = 'postgres'
PORT = 5432

#URL: postgresql://username:password@host:port/database
URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(URL, echo=True, pool_size=5, max_overflow=0)

DBSession = sessionmaker(bind=engine)
session = DBSession()

print(URL)