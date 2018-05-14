# Author:zhouxy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:alex3714@localhost/testdb",encoding='utf-8', echo=True) #echo=True打印信息
Base = declarative_base()  #生成orm基类


