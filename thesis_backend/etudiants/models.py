from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, func, Boolean, Time, text
from sqlalchemy.orm import relationship
from database import Base

class Etudiant(Base):
    __tablename__ = 'etudiants'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    matricule = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    user_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'))
    filiere_id = Column(Integer, ForeignKey('filiere.id', ondelete='CASCADE'))
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'))

    filiere_rel = relationship('Filiere', backref='etudiants')
    annee_rel = relationship('Annee', backref='etudiants')
    created = Column(DateTime, server_default=func.now())
    

    def __repr__(self) -> str:
        return f'Etudiant: {self.slug}'
    
class Filiere(Base):
    __tablename__ = 'filiere'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(length=200), nullable=False)

    def __repr__(self) -> str:
        return f'Filiere : {self.libelle}'
    
class Annee(Base):
    __tablename__ = 'annee'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(length=200), nullable=False)

    def __repr__(self) -> str:
        return f'Annee : {self.libelle}'
