from datetime import datetime
from base.config import database, marshmallow


class Application(database.Model):
    __tablename__ = 'application'
    application_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    api_key = database.Column(database.String(255), unique=True, nullable=False)
    entered_stamp = database.Column(database.DateTime, default=datetime.utcnow, nullable=False)


class ApplicationSchema(marshmallow.ModelSchema):
    class Meta:
        model = Application
        sqla_session = database.session

########################################################


class Users(database.Model):
    __tablename__ = 'users'
    user_id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(31), unique=True, nullable=False)
    email = database.Column(database.String(255), nullable=False)
    password = database.Column(database.String(255), nullable=False)


class UsersSchema(marshmallow.ModelSchema):
    class Meta:
        model = Users
        sqla_session = database.session

########################################################


class FileSystem(database.Model):
    __tablename__ = 'filesystem'
    filesystem_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    type = database.Column(database.Integer, nullable=False)
    path = database.Column(database.String(260), nullable=False)
    owner_id = database.Column(database.Integer, database.ForeignKey(Users.user_id), nullable=False)
    entered_stamp = database.Column(database.DateTime, default=datetime.utcnow, nullable=False)
    updated_stamp = database.Column(database.DateTime, default=datetime.utcnow,
                                    onupdate=datetime.utcnow, nullable=False)
    __table_args__ = (
        database.CheckConstraint(type in (0, 1), name='check_type_valid'),
        {}
    )


class FileSystemSchema(marshmallow.ModelSchema):
    class Meta:
        model = FileSystem
        sqla_session = database.session

########################################################


class FileSystemChildren(database.Model):
    __tablename__ = 'filesystem_children'
    filesystem_child_id = database.Column(database.Integer, primary_key=True)
    folder_id = database.Column(database.Integer, database.ForeignKey(FileSystem.filesystem_id), nullable=False)
    child_id = database.Column(database.Integer, database.ForeignKey(FileSystem.filesystem_id), nullable=False)


class FileSystemChildrenSchema(marshmallow.ModelSchema):
    class Meta:
        model = FileSystemChildren
        sqla_session = database.session

########################################################


class UserRoot(database.Model):
    __tablename__ = 'user_root'
    user_root_id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey(Users.user_id), nullable=False)
    root_folder_id = database.Column(database.Integer, database.ForeignKey(FileSystem.filesystem_id), nullable=False)


class UserRootSchema(marshmallow.ModelSchema):
    class Meta:
        model = UserRoot
        sqla_session = database.session
