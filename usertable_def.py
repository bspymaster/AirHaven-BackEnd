from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///usertable.db', echo=True)
Base = declarative_base()


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    root_folder_id = Column(Integer, nullable=False)

    # ----------------------------------------------------------------------
    def __init__(self, username, email, pass_hash, root_folder_id):
        """"""
        self.username = username
        self.email = email
        self.password_hash = pass_hash
        self.root_folder_id = root_folder_id


# create tables
Base.metadata.create_all(engine)
