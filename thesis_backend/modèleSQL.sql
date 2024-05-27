-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
CREATE DATABASE new_database;
-- ddl-end --


-- object: education | type: SCHEMA --
-- DROP SCHEMA IF EXISTS education CASCADE;
CREATE SCHEMA education;
-- ddl-end --
ALTER SCHEMA education OWNER TO postgres;
-- ddl-end --

-- object: projets | type: SCHEMA --
-- DROP SCHEMA IF EXISTS projets CASCADE;
CREATE SCHEMA projets;
-- ddl-end --
ALTER SCHEMA projets OWNER TO postgres;
-- ddl-end --

-- object: projet | type: SCHEMA --
-- DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;
-- ddl-end --
ALTER SCHEMA projet OWNER TO postgres;
-- ddl-end --

-- object: soutenances | type: SCHEMA --
-- DROP SCHEMA IF EXISTS soutenances CASCADE;
CREATE SCHEMA soutenances;
-- ddl-end --
ALTER SCHEMA soutenances OWNER TO postgres;
-- ddl-end --

-- object: notification | type: SCHEMA --
-- DROP SCHEMA IF EXISTS notification CASCADE;
CREATE SCHEMA notification;
-- ddl-end --
ALTER SCHEMA notification OWNER TO postgres;
-- ddl-end --

SET search_path TO pg_catalog,public,education,projets,projet,soutenances,notification;
-- ddl-end --

-- object: public.utilisateur | type: TABLE --
-- DROP TABLE IF EXISTS public.utilisateur CASCADE;
CREATE TABLE public.utilisateur (
	id serial NOT NULL,
	nom varchar(150) NOT NULL,
	prenom varchar(150) NOT NULL DEFAULT false,
	email varchar(150) NOT NULL,
	date_naissance date,
	mot_de_passe varchar(255) NOT NULL,
	sexe varchar(50),
	"isAdmin" boolean NOT NULL,
	CONSTRAINT utilisateur_pk PRIMARY KEY (id),
	CONSTRAINT unicity_mail UNIQUE (email)
);
-- ddl-end --
ALTER TABLE public.utilisateur OWNER TO postgres;
-- ddl-end --

-- object: public.role | type: TABLE --
-- DROP TABLE IF EXISTS public.role CASCADE;
CREATE TABLE public.role (
	id serial NOT NULL,
	nom_role varchar(100) NOT NULL,
	CONSTRAINT role_pk PRIMARY KEY (id),
	CONSTRAINT unicity UNIQUE (nom_role)
);
-- ddl-end --
ALTER TABLE public.role OWNER TO postgres;
-- ddl-end --

-- object: public.utilisateur_role | type: TABLE --
-- DROP TABLE IF EXISTS public.utilisateur_role CASCADE;
CREATE TABLE public.utilisateur_role (
	id_utilisateur integer,
	id_role integer

);
-- ddl-end --
ALTER TABLE public.utilisateur_role OWNER TO postgres;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE public.utilisateur_role DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE public.utilisateur_role ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: role_fk | type: CONSTRAINT --
-- ALTER TABLE public.utilisateur_role DROP CONSTRAINT IF EXISTS role_fk CASCADE;
ALTER TABLE public.utilisateur_role ADD CONSTRAINT role_fk FOREIGN KEY (id_role)
REFERENCES public.role (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: education.departement | type: TABLE --
-- DROP TABLE IF EXISTS education.departement CASCADE;
CREATE TABLE education.departement (
	id serial NOT NULL,
	nom_departement varchar(150) NOT NULL,
	CONSTRAINT departement_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE education.departement OWNER TO postgres;
-- ddl-end --

-- object: education.filiere | type: TABLE --
-- DROP TABLE IF EXISTS education.filiere CASCADE;
CREATE TABLE education.filiere (
	id serial NOT NULL,
	nom_filiere varchar(255) NOT NULL,
	id_departement integer,
	CONSTRAINT filiere_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE education.filiere OWNER TO postgres;
-- ddl-end --

-- object: education.etudiant | type: TABLE --
-- DROP TABLE IF EXISTS education.etudiant CASCADE;
CREATE TABLE education.etudiant (
	id serial NOT NULL,
	id_utilisateur integer,
	id_filiere integer,
	CONSTRAINT etudiant_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE education.etudiant OWNER TO postgres;
-- ddl-end --

-- object: education.enseignant | type: TABLE --
-- DROP TABLE IF EXISTS education.enseignant CASCADE;
CREATE TABLE education.enseignant (
	id serial NOT NULL,
	id_utilisateur integer,
	id_departement integer,
	CONSTRAINT enseignant_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE education.enseignant OWNER TO postgres;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE education.enseignant DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE education.enseignant ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: departement_fk | type: CONSTRAINT --
-- ALTER TABLE education.enseignant DROP CONSTRAINT IF EXISTS departement_fk CASCADE;
ALTER TABLE education.enseignant ADD CONSTRAINT departement_fk FOREIGN KEY (id_departement)
REFERENCES education.departement (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE education.etudiant DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE education.etudiant ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: filiere_fk | type: CONSTRAINT --
-- ALTER TABLE education.etudiant DROP CONSTRAINT IF EXISTS filiere_fk CASCADE;
ALTER TABLE education.etudiant ADD CONSTRAINT filiere_fk FOREIGN KEY (id_filiere)
REFERENCES education.filiere (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: departement_fk | type: CONSTRAINT --
-- ALTER TABLE education.filiere DROP CONSTRAINT IF EXISTS departement_fk CASCADE;
ALTER TABLE education.filiere ADD CONSTRAINT departement_fk FOREIGN KEY (id_departement)
REFERENCES education.departement (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: projets.maitre_memoire | type: TABLE --
-- DROP TABLE IF EXISTS projets.maitre_memoire CASCADE;
CREATE TABLE projets.maitre_memoire (
	id serial NOT NULL,
	nbr_max_equipe integer NOT NULL,
	id_filiere integer,
	id_enseignant integer,
	CONSTRAINT projets_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE projets.maitre_memoire OWNER TO postgres;
-- ddl-end --

-- object: projets.equipe | type: TABLE --
-- DROP TABLE IF EXISTS projets.equipe CASCADE;
CREATE TABLE projets.equipe (
	id serial NOT NULL,
	nom_equipe varchar(150),
	id_filiere integer,
	id_maitre_memoire integer,
	CONSTRAINT equipe_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE projets.equipe OWNER TO postgres;
-- ddl-end --

-- object: projets.membres_equipe | type: TABLE --
-- DROP TABLE IF EXISTS projets.membres_equipe CASCADE;
CREATE TABLE projets.membres_equipe (
	id serial NOT NULL,
	id_equipe integer,
	id_etudiant integer,
	CONSTRAINT membres_equipe_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE projets.membres_equipe OWNER TO postgres;
-- ddl-end --

-- object: projets.stage | type: TABLE --
-- DROP TABLE IF EXISTS projets.stage CASCADE;
CREATE TABLE projets.stage (
	id serial NOT NULL,
	theme text NOT NULL,
	lieu varchar(255) NOT NULL,
	responsable varchar(150) NOT NULL,
	statut varchar(50) NOT NULL,
	id_equipe integer,
	cahier_de_charge text NOT NULL,
	CONSTRAINT stage_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE projets.stage OWNER TO postgres;
-- ddl-end --

-- object: projets.memoire | type: TABLE --
-- DROP TABLE IF EXISTS projets.memoire CASCADE;
CREATE TABLE projets.memoire (
	id serial NOT NULL,
	title varchar(255) NOT NULL,
	document text NOT NULL,
	statut varchar(50) NOT NULL,
	id_equipe integer,
	CONSTRAINT memoire_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE projets.memoire OWNER TO postgres;
-- ddl-end --

-- object: equipe_fk | type: CONSTRAINT --
-- ALTER TABLE projets.memoire DROP CONSTRAINT IF EXISTS equipe_fk CASCADE;
ALTER TABLE projets.memoire ADD CONSTRAINT equipe_fk FOREIGN KEY (id_equipe)
REFERENCES projets.equipe (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: memoire_uq | type: CONSTRAINT --
-- ALTER TABLE projets.memoire DROP CONSTRAINT IF EXISTS memoire_uq CASCADE;
ALTER TABLE projets.memoire ADD CONSTRAINT memoire_uq UNIQUE (id_equipe);
-- ddl-end --

-- object: equipe_fk | type: CONSTRAINT --
-- ALTER TABLE projets.stage DROP CONSTRAINT IF EXISTS equipe_fk CASCADE;
ALTER TABLE projets.stage ADD CONSTRAINT equipe_fk FOREIGN KEY (id_equipe)
REFERENCES projets.equipe (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: stage_uq | type: CONSTRAINT --
-- ALTER TABLE projets.stage DROP CONSTRAINT IF EXISTS stage_uq CASCADE;
ALTER TABLE projets.stage ADD CONSTRAINT stage_uq UNIQUE (id_equipe);
-- ddl-end --

-- object: equipe_fk | type: CONSTRAINT --
-- ALTER TABLE projets.membres_equipe DROP CONSTRAINT IF EXISTS equipe_fk CASCADE;
ALTER TABLE projets.membres_equipe ADD CONSTRAINT equipe_fk FOREIGN KEY (id_equipe)
REFERENCES projets.equipe (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: etudiant_fk | type: CONSTRAINT --
-- ALTER TABLE projets.membres_equipe DROP CONSTRAINT IF EXISTS etudiant_fk CASCADE;
ALTER TABLE projets.membres_equipe ADD CONSTRAINT etudiant_fk FOREIGN KEY (id_etudiant)
REFERENCES education.etudiant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: filiere_fk | type: CONSTRAINT --
-- ALTER TABLE projets.equipe DROP CONSTRAINT IF EXISTS filiere_fk CASCADE;
ALTER TABLE projets.equipe ADD CONSTRAINT filiere_fk FOREIGN KEY (id_filiere)
REFERENCES education.filiere (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: maitre_memoire_fk | type: CONSTRAINT --
-- ALTER TABLE projets.equipe DROP CONSTRAINT IF EXISTS maitre_memoire_fk CASCADE;
ALTER TABLE projets.equipe ADD CONSTRAINT maitre_memoire_fk FOREIGN KEY (id_maitre_memoire)
REFERENCES projets.maitre_memoire (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: filiere_fk | type: CONSTRAINT --
-- ALTER TABLE projets.maitre_memoire DROP CONSTRAINT IF EXISTS filiere_fk CASCADE;
ALTER TABLE projets.maitre_memoire ADD CONSTRAINT filiere_fk FOREIGN KEY (id_filiere)
REFERENCES education.filiere (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: enseignant_fk | type: CONSTRAINT --
-- ALTER TABLE projets.maitre_memoire DROP CONSTRAINT IF EXISTS enseignant_fk CASCADE;
ALTER TABLE projets.maitre_memoire ADD CONSTRAINT enseignant_fk FOREIGN KEY (id_enseignant)
REFERENCES education.enseignant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: soutenances.jury | type: TABLE --
-- DROP TABLE IF EXISTS soutenances.jury CASCADE;
CREATE TABLE soutenances.jury (
	id serial NOT NULL,
	id_enseignant integer,
	president varchar(150) NOT NULL,
	examinateur varchar(150) NOT NULL,
	rapporteur varchar(150) NOT NULL,
	CONSTRAINT jury_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE soutenances.jury OWNER TO postgres;
-- ddl-end --

-- object: soutenances.planning | type: TABLE --
-- DROP TABLE IF EXISTS soutenances.planning CASCADE;
CREATE TABLE soutenances.planning (
	id serial NOT NULL,
	date timestamp NOT NULL,
	satut varchar(50),
	id_jury integer,
	id_equipe integer,
	id_salle integer,
	CONSTRAINT planning_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE soutenances.planning OWNER TO postgres;
-- ddl-end --

-- object: soutenances.evaluation | type: TABLE --
-- DROP TABLE IF EXISTS soutenances.evaluation CASCADE;
CREATE TABLE soutenances.evaluation (
	id serial NOT NULL,
	evaluation text,
	note varchar(10),
	id_planning integer,
	CONSTRAINT evaluation_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE soutenances.evaluation OWNER TO postgres;
-- ddl-end --

-- object: soutenances.proces_verbaux | type: TABLE --
-- DROP TABLE IF EXISTS soutenances.proces_verbaux CASCADE;
CREATE TABLE soutenances.proces_verbaux (
	id serial NOT NULL,
	doc_pv text NOT NULL,
	id_planning integer,
	CONSTRAINT pv_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE soutenances.proces_verbaux OWNER TO postgres;
-- ddl-end --

-- object: planning_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.evaluation DROP CONSTRAINT IF EXISTS planning_fk CASCADE;
ALTER TABLE soutenances.evaluation ADD CONSTRAINT planning_fk FOREIGN KEY (id_planning)
REFERENCES soutenances.planning (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: planning_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.proces_verbaux DROP CONSTRAINT IF EXISTS planning_fk CASCADE;
ALTER TABLE soutenances.proces_verbaux ADD CONSTRAINT planning_fk FOREIGN KEY (id_planning)
REFERENCES soutenances.planning (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: jury_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.planning DROP CONSTRAINT IF EXISTS jury_fk CASCADE;
ALTER TABLE soutenances.planning ADD CONSTRAINT jury_fk FOREIGN KEY (id_jury)
REFERENCES soutenances.jury (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: equipe_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.planning DROP CONSTRAINT IF EXISTS equipe_fk CASCADE;
ALTER TABLE soutenances.planning ADD CONSTRAINT equipe_fk FOREIGN KEY (id_equipe)
REFERENCES projets.equipe (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: enseignant_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.jury DROP CONSTRAINT IF EXISTS enseignant_fk CASCADE;
ALTER TABLE soutenances.jury ADD CONSTRAINT enseignant_fk FOREIGN KEY (id_enseignant)
REFERENCES education.enseignant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: notification.message | type: TABLE --
-- DROP TABLE IF EXISTS notification.message CASCADE;
CREATE TABLE notification.message (
	id serial NOT NULL,
	contenue text NOT NULL,
	envoye_a timestamp with time zone NOT NULL,
	id_utilisateur integer,
	expediteur varchar(150) NOT NULL,
	destinataire varchar(150) NOT NULL,
	CONSTRAINT message_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE notification.message OWNER TO postgres;
-- ddl-end --

-- object: notification.notification | type: TABLE --
-- DROP TABLE IF EXISTS notification.notification CASCADE;
CREATE TABLE notification.notification (
	id serial NOT NULL,
	contenu text NOT NULL,
	cree_a timestamp with time zone,
	statut boolean NOT NULL,
	id_utilisateur integer,
	CONSTRAINT notification_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE notification.notification OWNER TO postgres;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE notification.notification DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE notification.notification ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE notification.message DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE notification.message ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: soutenances.salle | type: TABLE --
-- DROP TABLE IF EXISTS soutenances.salle CASCADE;
CREATE TABLE soutenances.salle (
	id serial NOT NULL,
	nom varchar(150) NOT NULL,
	CONSTRAINT salles_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE soutenances.salle OWNER TO postgres;
-- ddl-end --

-- object: salle_fk | type: CONSTRAINT --
-- ALTER TABLE soutenances.planning DROP CONSTRAINT IF EXISTS salle_fk CASCADE;
ALTER TABLE soutenances.planning ADD CONSTRAINT salle_fk FOREIGN KEY (id_salle)
REFERENCES soutenances.salle (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


