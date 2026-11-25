#import the function that creates connection to the database    
from sqlalchemy import create_engine, false
#imports the factory function that  generates sessions
from sqlalchemy.orm import sessionmaker
#imports the function that craetes databse mnodels that tables will inherit from
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db" 

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False})
 
sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()