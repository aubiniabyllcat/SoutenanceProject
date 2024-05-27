from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, func, Boolean, Time, text
from sqlalchemy.orm import relationship
from database import Base

class Enseignant(Base):
    __tablename__ = 'enseignants'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    matricule = Column(String(length=200), nullable=False, unique=True)
    slug = Column(String)
    grade = Column(String(length=200), nullable=False)
    specialite = Column(String(length=200), nullable=False)
    user_id = Column(Integer, ForeignKey('utilisateur.id', ondelete='CASCADE'))
    filiere_id = Column(Integer, ForeignKey('filiere.id', ondelete='CASCADE'))
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'))

    filiere_rel = relationship('Filiere', backref='enseignants')
    annee_rel = relationship('Annee', backref='enseignants')
    created = Column(DateTime, server_default=func.now())
    

    def __repr__(self) -> str:
        return f'Enseignant: {self.slug}'
    
