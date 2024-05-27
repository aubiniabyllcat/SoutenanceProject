# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata







class Salle(Base):
    __tablename__ = 'salle'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".salle_id_seq'::regclass)"))
    nom = Column(String(150), nullable=False)












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


t_utilisateur_role = Table(
    'utilisateur_role', metadata,
    Column('id_utilisateur', ForeignKey('public.utilisateur.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL')),
    Column('id_role', ForeignKey('public.role.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL')),
    schema='public'
)




class Jury(Base):
    __tablename__ = 'jury'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".jury_id_seq'::regclass)"))
    id_enseignant = Column(ForeignKey('public.enseignant.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    president = Column(String(150), nullable=False)
    examinateur = Column(String(150), nullable=False)
    rapporteur = Column(String(150), nullable=False)

    enseignant = relationship('Enseignant')


class MaitreMemoire(Base):
    __tablename__ = 'maitre_memoire'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".maitre_memoire_id_seq'::regclass)"))
    nbr_max_equipe = Column(Integer, nullable=False)
    id_filiere = Column(ForeignKey('public.filiere.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_enseignant = Column(ForeignKey('public.enseignant.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    enseignant = relationship('Enseignant')
    filiere = relationship('Filiere')


class Equipe(Base):
    __tablename__ = 'equipe'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".equipe_id_seq'::regclass)"))
    nom_equipe = Column(String(150))
    id_filiere = Column(ForeignKey('public.filiere.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_maitre_memoire = Column(ForeignKey('public.maitre_memoire.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    filiere = relationship('Filiere')
    maitre_memoire = relationship('MaitreMemoire')


class MembresEquipe(Base):
    __tablename__ = 'membres_equipe'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".membres_equipe_id_seq'::regclass)"))
    id_equipe = Column(ForeignKey('public.equipe.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_etudiant = Column(ForeignKey('public.etudiant.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))
    id_etudiant = Column(ForeignKey('public.etudiant.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'))

    equipe = relationship('Equipe')
    etudiant = relationship('Etudiant')


class Memoire(Base):
    __tablename__ = 'memoire'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".memoire_id_seq'::regclass)"))
    title = Column(String(255), nullable=False)
    document = Column(Text, nullable=False)
    statut = Column(String(50), nullable=False)
    id_equipe = Column(ForeignKey('public.equipe.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'), unique=True)

    equipe = relationship('Equipe', uselist=False)


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


class Stage(Base):
    __tablename__ = 'stage'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".stage_id_seq'::regclass)"))
    theme = Column(Text, nullable=False)
    lieu = Column(String(255), nullable=False)
    responsable = Column(String(150), nullable=False)
    statut = Column(String(50), nullable=False)
    id_equipe = Column(ForeignKey('public.equipe.id', ondelete='SET NULL', onupdate='CASCADE', match='FULL'), unique=True)
    cahier_de_charge = Column(Text, nullable=False)

    equipe = relationship('Equipe', uselist=False)


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
