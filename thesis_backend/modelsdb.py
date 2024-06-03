# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = 'message'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".message_id_seq'::regclass)"))
    contenue = Column(Text, nullable=False)
    envoye_a = Column(DateTime(True), nullable=False)
    id_utilisateur = Column(ForeignKey('public.utilisateur.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    expediteur = Column(String(150), nullable=False)
    destinataire = Column(String(150), nullable=False)

    utilisateur = relationship('Utilisateur')


class Notification(Base):
    __tablename__ = 'notification'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".notification_id_seq'::regclass)"))
    contenu = Column(Text, nullable=False)
    cree_a = Column(DateTime(True))
    statut = Column(Boolean, nullable=False)
    id_utilisateur = Column(ForeignKey('public.utilisateur.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    utilisateur = relationship('Utilisateur')



class Jury(Base):
    __tablename__ = 'jury'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    president_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'))
    examinateur_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'))
    rapporteur_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE', nullable=True))

    president = relationship('Enseignant', foreign_keys=[president_id], backref='jury_president')
    examinateur = relationship('Enseignant', foreign_keys=[examinateur_id], backref='jury_examinateur')
    rapporteur = relationship('Enseignant', foreign_keys=[rapporteur_id], backref='jury_rapporteur')


    enseignant = relationship('Enseignant')



class Planning(Base):
    __tablename__ = 'planning'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".planning_id_seq'::regclass)"))
    date = Column(DateTime, nullable=False)
    satut = Column(String(50))
    id_jury = Column(ForeignKey('public.jury.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_equipe = Column(ForeignKey('public.equipe.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_salle = Column(ForeignKey('public.salle.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    equipe = relationship('Equipe')
    jury = relationship('Jury')
    salle = relationship('Salle')





class Evaluation(Base):
    __tablename__ = 'evaluation'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".evaluation_id_seq'::regclass)"))
    evaluation = Column(Text)
    note = Column(String(10))
    id_planning = Column(ForeignKey('public.planning.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    planning = relationship('Planning')


class ProcesVerbaux(Base):
    __tablename__ = 'proces_verbaux'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".proces_verbaux_id_seq'::regclass)"))
    doc_pv = Column(Text, nullable=False)
    id_planning = Column(ForeignKey('public.planning.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    planning = relationship('Planning')
