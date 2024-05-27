from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, func, Boolean, Time, text
from sqlalchemy.orm import relationship
from database import Base

class Etudiant(Base):
    __tablename__ = 'etudiant'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    matricule = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    user_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'))
    filiere_id = Column(Integer, ForeignKey('filiere.id', ondelete='CASCADE'))
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'))

    filiere_rel = relationship('Filiere', backref='etudiant')
    annee_rel = relationship('Annee', backref='etudiant')
    created = Column(DateTime, server_default=func.now())
    

    def __repr__(self) -> str:
        return f'Etudiant: {self.slug}'
    
class Departement(Base):
    __tablename__ = 'departement'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)

    def __repr__(self) -> str:
        return f'Departement: {self.nom}'
    
class Filiere(Base):
    __tablename__ = 'filiere'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(length=200), nullable=False)
    departement_id = Column(ForeignKey('departement.id', ondelete='CASCADE'))

    departement_rel = relationship('Departement', backref='filiere')

    def __repr__(self) -> str:
        return f'Filiere : {self.libelle}'
    
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
    id_filiere = Column(ForeignKey('filiere.id', ondelete='CASCADE'))
    id_maitre_memoire = Column(ForeignKey('maitre_memoire.id', ondelete='CASCADE'))

    filiere = relationship('Filiere', backref='equipe')
    maitre_memoire = relationship('MaitreMemoire', backref='equipe')

    def __repr__(self) -> str:
        return f'Equipe: {self.nom}'


class MembresEquipe(Base):
    __tablename__ = 'membre_equipe'
    
    id = Column(Integer, primary_key=True)
    id_equipe = Column(ForeignKey('equipe.id', ondelete='CASCADE'))
    id_etudiant = Column(ForeignKey('etudiant.id', ondelete='CASCADE'))
    
    
    equipe = relationship('Equipe', backref='membre_equipe')
    etudiant = relationship('Etudiant', backref='membre_equipe')

    def __repr__(self) -> str:
        return f'MembresEquipe: {self.id}'
