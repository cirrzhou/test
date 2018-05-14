# Author:zhouxy


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationships

engine = create_engine("mysql+pymysql://dev_hx_rmps:dev_hx_rmps123@10.10.200.61:3306/rmpsdb",encoding='utf-8',echo=True)
Base = declarative_base()

#讲师与班级对应关系表
teacher_m2m_class= Table('teacher_m2m_class',Base.metadata,
                         Column('teacher_id',Integer,ForeignKey('teacher.id')),
                         Column('class_id',Integer,ForeignKey('class.id')),
                         )

#学生与班级对应关系表
student_m2m_class= Table('student_m2m_class',Base.metadata,
                         Column('student_id',Integer,ForeignKey('student.id')),
                         Column('class_id', Integer, ForeignKey('class.id')),
                         )

class class_m2m_lesson(Base):
    '''班级与课程对应关系表'''
    __tablename__= 'class_m2m_course'
    id = Column(Integer,primary_key=True,autoincrement=1)
    class_id =(Integer,ForeignKey('class.id'))
    lesson_id = (Integer,ForeignKey('lesson.id'))
    classes = relationships('Class',backref='class_m2m_lesson')
    lessons = relationships('Lesson',backref='class_m2m_lesson')

    def __repr__(self):
        return self.id,self.class_id,self.lesson_id

class StudyRecord(Base):
    '''上课记录表'''
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True, autoincrement=1)
    student_id = Column(Integer,ForeignKey('student.id'))
    class_m2m_lesson_id = Column(Integer,ForeignKey('class_m2m_lesson.id'))
    status = Column(String(16))
    score = Column(Integer)

    class_id_lessons = relationships('Class_m2m_lesson',backref = 'my_study_record')
    student = relationships('Studeng',backref = 'my_study_record')

    def __repr__(self):
        return self.class_m2m_lessons,self.student,self.status,self.score


class Teacher(Base):
    '''讲师表'''
    __tablename__='teacher'
    id = Column(Integer,primary_key=True,autoincrement=1)
    teacher_name = Column(String(64))
    class_name = relationships('Class',secondary = teacher_m2m_class,backref='teacher')

    def __repr__(self):
        return self.teacher_name

class Class(Base):
    '''班级表'''
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=1)
    class_name = Column(String(64))

    def __repr__(self):
        return self.teacher_name

class Student(Base):
    '''学生表'''
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=1)
    student_name = Column(String(64))
    qq = Column(Integer(16))

    def __repr__(self):
        return self.student_name

class Lesson(Base):
    '''课程表'''
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True, autoincrement=1)
    lesson_name = Column(String(64))

    def __repr__(self):
        return self.lesson_name

Base.metadata.create.all(engine)