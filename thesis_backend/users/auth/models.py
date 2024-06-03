from sqlalchemy import func, Column, Integer, String, DateTime,text, Time, Boolean, \
    ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import UniqueConstraint


class Users(Base):
    __tablename__ = 'utilisateur'

    __mapper_args__ = {"eager_defaults": True}


    id = Column(Integer, primary_key=True)
    username = Column(String(length=200), unique=True)
    password = Column(String)
    nom = Column(String(length=200), nullable=False)
    prenoms = Column(String(length=200), nullable=False)
    bio = Column(String(length=255))
    role_id = Column(
        Integer,
        ForeignKey('role.id', ondelete='CASCADE')
    )
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, server_default=func.now())

    role_rel = relationship('Role', backref='utilisateur')
    images = relationship(
        'UserImage',
        backref='user',
        passive_deletes=True,
        lazy='joined'
    )

    __table_args__ = (
        UniqueConstraint('id', 'role_id', name='unique_user_role'),
    )
    
    def __repr__(self) -> str:
        return f'User: {self.username}'
    

class UserImage(Base):
    __tablename__ = 'utilisateur_image'

    id = Column(Integer, primary_key=True)
    photo = Column(String)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'))

    def __repr__(self) -> str:
        return f'User image: {self.photo} : {self.user_id}'

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(length=200), nullable=False)

    def __repr__(self) -> str:
        return f'Role : {self.libelle}'