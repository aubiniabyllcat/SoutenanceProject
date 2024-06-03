# models.py
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Ecole(Base):
    __tablename__ = 'ecole'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    adresse = Column(String(length=200), nullable=False)
    directeur = Column(String(length=200), nullable=False)
    telephone = Column(String(length=200), nullable=False)
    email = Column(String(length=200), nullable=False)
    ville = Column(String(length=200), nullable=False)
    siteweb = Column(String(length=200), nullable=False)

    salles = relationship('Salle', back_populates='ecole_rel')

    def __repr__(self) -> str:
        return f'Ecole: {self.slug}'

class Salle(Base):
    __tablename__ = 'salle'

    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)
    capacite = Column(String(150), nullable=False)
    ecole_id = Column(Integer, ForeignKey('ecole.id'), nullable=False)  # Assurez-vous que c'est Integer

    ecole_rel = relationship('Ecole', back_populates='salles')

    def __repr__(self) -> str:
        return f'Salle : {self.nom}'
