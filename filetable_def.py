from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///filetable.db', echo=True)
Base = declarative_base()


########################################################################
class FileSystemObject(Base):
    """"""
    __tablename__ = "file_system_objects"

    id = Column(Integer, primary_key=True)  # the unique id of the object
    name = Column(String)                   # the name of the object
    type = Column(String, nullable=False)   # the type of the object ("file" or "folder")
    path = Column(String, nullable=False)   # the path to the object

    def __init__(self, name, obj_type, path):
        """"""
        self.name = name
        self.type = obj_type
        self.path = path


class Child(Base):
    """"""
    __tablename__ = "children"

    # the id of the parent folder
    folder_id = Column(Integer, ForeignKey(FileSystemObject.id), nullable=False, primary_key=True)
    # the id of the child file/folder
    child_id = Column(Integer, ForeignKey(FileSystemObject.id), nullable=False, primary_key=True)

    def __init__(self, folder_id, child_id):
        """"""
        self.folder_id = folder_id
        self.child_id = child_id


# create tables
Base.metadata.create_all(engine)
