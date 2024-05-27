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
    user_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'))
    filiere_id = Column(Integer, ForeignKey('filiere.id', ondelete='CASCADE'))
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'))

    filiere_rel = relationship('Filiere', backref='enseignant')
    annee_rel = relationship('Annee', backref='enseignant')
    created = Column(DateTime, server_default=func.now())
    

    def __repr__(self) -> str:
        return f'Enseignant: {self.slug}'
    


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
