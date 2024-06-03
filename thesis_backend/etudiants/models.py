from typing import Text
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, func, Boolean, Time, Text
from sqlalchemy.orm import relationship
from database import Base

class Etudiant(Base):
    __tablename__ = 'etudiant'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    matricule = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'), unique=True)
    filiere_id = Column(Integer, ForeignKey('filiere.id', ondelete='CASCADE'))
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'))

    
    filiere_rel = relationship('Filiere', backref='etudiant')
    annee_rel = relationship('Annee', backref='etudiant')
    created = Column(DateTime, server_default=func.now())
    

    def __repr__(self) -> str:
        return f'Etudiant: {self.slug}'
    

    
class Filiere(Base):
    __tablename__ = 'filiere'

    id = Column(Integer, primary_key=True)
    nom = Column(String(length=200), nullable=False)
    departement_id = Column(Integer, ForeignKey('departement.id', ondelete='CASCADE'))
    
    chef_departemnt_rel = relationship('Departement', backref='filiere')
    def __repr__(self) -> str:
        return f'Filiere : {self.nom}'
    




class Annee(Base):
    __tablename__ = 'annee'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(length=200), nullable=False)

    def __repr__(self) -> str:
        return f'Annee : {self.libelle}'
    
class Equipe(Base):
    __tablename__ = 'equipe'
   
    id = Column(Integer, primary_key=True)
    nom = Column(String(150))
    filiere_id = Column(ForeignKey('filiere.id', ondelete='CASCADE'))
    maitre_memoire_id = Column(ForeignKey('maitre_memoire.id', ondelete='CASCADE'))

    filiere = relationship('Filiere', backref='equipe')
    maitre_memoire = relationship('MaitreMemoire', backref='equipe')

    def __repr__(self) -> str:
        return f'Equipe: {self.nom}'


class MembresEquipe(Base):
    __tablename__ = 'membre_equipe'
    
    id = Column(Integer, primary_key=True)
    equipe_id = Column(ForeignKey('equipe.id', ondelete='CASCADE'))
    etudiant1_id = Column(ForeignKey('etudiant.id', ondelete='CASCADE'))
    etudiant2_id = Column(ForeignKey('etudiant.id', ondelete='CASCADE'), nullable=True)
    
    equipe = relationship('Equipe', backref='membre_equipe')
    etudiant1 = relationship('Etudiant', foreign_keys=[etudiant1_id], backref='membre_equipe1')
    etudiant2 = relationship('Etudiant', foreign_keys=[etudiant2_id], backref='membre_equipe2')

    def __repr__(self) -> str:
        return f'MembresEquipe: {self.id}'

class Memoire(Base):
    __tablename__ = 'memoire'

    id = Column(Integer, primary_key=True)
    theme = Column(String(255), nullable=False)
    document = Column(Text, nullable=False)
    valide = Column(Boolean, default=False)
    equipe_id = Column(ForeignKey('equipe.id', ondelete='CASCADE'), unique=True)

    equipe = relationship('Equipe', backref='memoire')

    def __repr__(self) -> str:
        return f'Memoire: {self.theme}'


class Stage(Base):
    __tablename__ = 'stage'


    id = Column(Integer, primary_key=True)
    theme = Column(Text, nullable=False)
    lieu = Column(String(255), nullable=False)
    responsable = Column(String(150), nullable=False)
    valide = Column(Boolean, default=True)
    equipe_id = Column(ForeignKey('equipe.id', ondelete='CASCADE'), unique=True)
    cahier_de_charge = Column(Text, nullable=False)

    equipe = relationship('Equipe', backref='stage')

    def __repr__(self) -> str:
        return f'Stage: {self.theme}'