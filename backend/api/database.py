import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user =os.getenv("DB_USER")
db_password =os.getenv("DB_PASSWORD")
db_host =os.getenv("DB_HOST")
db_name  =os.getenv("DB_NAME")


SQL_ALCHEMY_DATABASE = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}?charset=utf8mb4"

engine = create_engine(SQL_ALCHEMY_DATABASE, pool_recycle=3600)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# session = Session()

Base = declarative_base()