from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, func, Boolean, Time, text
from sqlalchemy.orm import relationship
from database import Base

class Enseignant(Base):
    __tablename__ = 'enseignant'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    matricule = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    grade = Column(String(length=200), nullable=False)
    specialite = Column(String(length=200), nullable=False) 
    utilisateur_id = Column(Integer,  ForeignKey('utilisateur.id', ondelete='CASCADE'), unique=True)
    departement_id = Column(ForeignKey('departement.id', ondelete='CASCADE'))

    departement_rel = relationship('Departement', backref='enseignant')
    created = Column(DateTime, server_default=func.now())
    
    def __repr__(self) -> str:
        return f'Enseignant: {self.slug}'
    
class Departement(Base):
    __tablename__ = 'departement'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)
    ecole_id = Column(ForeignKey('ecole.id', ondelete='CASCADE'))

    ecole_rel = relationship('Ecole', backref='departement')
    
    def __repr__(self) -> str:
        return f'Departement: {self.nom}'
    
class Chefdepartement(Base):
    __tablename__ = 'chef_departement'

    id = Column(Integer, primary_key=True)
    enseignant_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'))
    departement_id = Column(Integer, ForeignKey('departement.id', ondelete='CASCADE'))
    
    enseignant_rel = relationship('Enseignant', backref='chef_departement')
    chef_departemnt_rel = relationship('Departement', backref='chef_departement')
    def __repr__(self) -> str:
        return f'Filiere : {self.id}'

class MaitreMemoire(Base):
    __tablename__ = 'maitre_memoire'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    nbr_max_equipe = Column(Integer, nullable=False)
    filiere_id = Column(ForeignKey('filiere.id', ondelete='CASCADE'))
    enseignant_id = Column(ForeignKey('enseignant.id', ondelete='CASCADE'))

    enseignant = relationship('Enseignant', backref='maitre_memoire')
    filiere = relationship('Filiere', backref='maitre_memoire')

    def __repr__(self) -> str:
        return f'MaitreMemoire: {self.id}'
