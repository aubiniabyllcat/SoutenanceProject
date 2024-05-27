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


-- object: public.utilisateur | type: TABLE --
-- DROP TABLE IF EXISTS public.utilisateur CASCADE;
CREATE TABLE public.utilisateur (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	username varchar(255) NOT NULL,
	email varchar(200) NOT NULL,
	password varchar(255) NOT NULL,
	created_at timestamp NOT NULL DEFAULT now(),
	is_actif boolean NOT NULL DEFAULT true,
	id_role integer,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.utilisateur OWNER TO postgres;
-- ddl-end --

-- object: public.etudiant | type: TABLE --
-- DROP TABLE IF EXISTS public.etudiant CASCADE;
CREATE TABLE public.etudiant (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	matricule varchar(20) NOT NULL,
	id_utilisateur varchar(12),
	nom varchar(50) NOT NULL,
	date_naissance date,
	genre varchar(20),
	id_filiere varchar(12),
	annee integer NOT NULL,
	CONSTRAINT etudiant_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.etudiant OWNER TO postgres;
-- ddl-end --

-- object: public.departement | type: TABLE --
-- DROP TABLE IF EXISTS public.departement CASCADE;
CREATE TABLE public.departement (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	libelle varchar(255) NOT NULL,
	id_chef varchar NOT NULL,
	CONSTRAINT departement_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.departement OWNER TO postgres;
-- ddl-end --

-- object: public.enseignant | type: TABLE --
-- DROP TABLE IF EXISTS public.enseignant CASCADE;
CREATE TABLE public.enseignant (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	grade varchar(255) NOT NULL,
	specialite varchar(255) NOT NULL,
	nom varchar(50) NOT NULL,
	prenoms varchar(150) NOT NULL,
	id_utilisateur varchar(12),
	CONSTRAINT enseignant_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.enseignant OWNER TO postgres;
-- ddl-end --

-- object: public.memoire | type: TABLE --
-- DROP TABLE IF EXISTS public.memoire CASCADE;
CREATE TABLE public.memoire (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	theme varchar(255) NOT NULL,
	lieu_stage varchar(200),
	adresse_stage varchar(100),
	contact_stage varchar(100),
	is_theme_valide boolean NOT NULL DEFAULT true,
	is_pret_pour_soutenir boolean NOT NULL DEFAULT false,
	id_maitre_memoire varchar(12),
	id_soutenance varchar(12),
	id_memorant varchar(12),
	CONSTRAINT memoire_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.memoire OWNER TO postgres;
-- ddl-end --

-- object: public.jury | type: TABLE --
-- DROP TABLE IF EXISTS public.jury CASCADE;
CREATE TABLE public.jury (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	role varchar NOT NULL DEFAULT 'Président',
	id_enseignant varchar(12),
	id_soutenance varchar(12),
	CONSTRAINT jury_pk PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON COLUMN public.jury.role IS E'Président, Rapporteur, Examinateur';
-- ddl-end --
ALTER TABLE public.jury OWNER TO postgres;
-- ddl-end --

-- object: public.soutenance | type: TABLE --
-- DROP TABLE IF EXISTS public.soutenance CASCADE;
CREATE TABLE public.soutenance (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	date date,
	heure time,
	decision_du_jury varchar,
	id_salle varchar(12),
	id_memorant varchar(12) NOT NULL,
	CONSTRAINT soutenance_pk PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON COLUMN public.soutenance.decision_du_jury IS E'Accepté, Refusé';
-- ddl-end --
ALTER TABLE public.soutenance OWNER TO postgres;
-- ddl-end --

-- object: public.salle | type: TABLE --
-- DROP TABLE IF EXISTS public.salle CASCADE;
CREATE TABLE public.salle (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	intitule varchar(150) NOT NULL,
	CONSTRAINT salle_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.salle OWNER TO postgres;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE public.etudiant DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE public.etudiant ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: etudiant_uq | type: CONSTRAINT --
-- ALTER TABLE public.etudiant DROP CONSTRAINT IF EXISTS etudiant_uq CASCADE;
ALTER TABLE public.etudiant ADD CONSTRAINT etudiant_uq UNIQUE (id_utilisateur);
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE public.enseignant DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE public.enseignant ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: enseignant_uq | type: CONSTRAINT --
-- ALTER TABLE public.enseignant DROP CONSTRAINT IF EXISTS enseignant_uq CASCADE;
ALTER TABLE public.enseignant ADD CONSTRAINT enseignant_uq UNIQUE (id_utilisateur);
-- ddl-end --

-- object: public.filiere | type: TABLE --
-- DROP TABLE IF EXISTS public.filiere CASCADE;
CREATE TABLE public.filiere (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	nom varchar(255) NOT NULL,
	id_departement varchar(12),
	CONSTRAINT filiere_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.filiere OWNER TO postgres;
-- ddl-end --

-- object: salle_fk | type: CONSTRAINT --
-- ALTER TABLE public.soutenance DROP CONSTRAINT IF EXISTS salle_fk CASCADE;
ALTER TABLE public.soutenance ADD CONSTRAINT salle_fk FOREIGN KEY (id_salle)
REFERENCES public.salle (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: soutenance_fk | type: CONSTRAINT --
-- ALTER TABLE public.memoire DROP CONSTRAINT IF EXISTS soutenance_fk CASCADE;
ALTER TABLE public.memoire ADD CONSTRAINT soutenance_fk FOREIGN KEY (id_soutenance)
REFERENCES public.soutenance (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: memoire_uq | type: CONSTRAINT --
-- ALTER TABLE public.memoire DROP CONSTRAINT IF EXISTS memoire_uq CASCADE;
ALTER TABLE public.memoire ADD CONSTRAINT memoire_uq UNIQUE (id_soutenance);
-- ddl-end --

-- object: enseignant_fk | type: CONSTRAINT --
-- ALTER TABLE public.jury DROP CONSTRAINT IF EXISTS enseignant_fk CASCADE;
ALTER TABLE public.jury ADD CONSTRAINT enseignant_fk FOREIGN KEY (id_enseignant)
REFERENCES public.enseignant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: soutenance_fk | type: CONSTRAINT --
-- ALTER TABLE public.jury DROP CONSTRAINT IF EXISTS soutenance_fk CASCADE;
ALTER TABLE public.jury ADD CONSTRAINT soutenance_fk FOREIGN KEY (id_soutenance)
REFERENCES public.soutenance (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: filiere_fk | type: CONSTRAINT --
-- ALTER TABLE public.etudiant DROP CONSTRAINT IF EXISTS filiere_fk CASCADE;
ALTER TABLE public.etudiant ADD CONSTRAINT filiere_fk FOREIGN KEY (id_filiere)
REFERENCES public.filiere (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.stage | type: TABLE --
-- DROP TABLE IF EXISTS public.stage CASCADE;
CREATE TABLE public.stage (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	theme varchar(255) NOT NULL,
	id_memorant varchar(12),
	CONSTRAINT stage_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.stage OWNER TO postgres;
-- ddl-end --

-- object: public.memorant | type: TABLE --
-- DROP TABLE IF EXISTS public.memorant CASCADE;
CREATE TABLE public.memorant (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	etu1 varchar(12) NOT NULL,
	etu2 varchar(12) NOT NULL,
	type varchar(255) NOT NULL,
	CONSTRAINT memorant_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.memorant OWNER TO postgres;
-- ddl-end --

-- object: public.maitre_memoire | type: TABLE --
-- DROP TABLE IF EXISTS public.maitre_memoire CASCADE;
CREATE TABLE public.maitre_memoire (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	id_maitre varchar NOT NULL,
	CONSTRAINT maitre_memoire_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.maitre_memoire OWNER TO postgres;
-- ddl-end --

-- object: memorant_fk | type: CONSTRAINT --
-- ALTER TABLE public.stage DROP CONSTRAINT IF EXISTS memorant_fk CASCADE;
ALTER TABLE public.stage ADD CONSTRAINT memorant_fk FOREIGN KEY (id_memorant)
REFERENCES public.memorant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: memorant_fk | type: CONSTRAINT --
-- ALTER TABLE public.memoire DROP CONSTRAINT IF EXISTS memorant_fk CASCADE;
ALTER TABLE public.memoire ADD CONSTRAINT memorant_fk FOREIGN KEY (id_memorant)
REFERENCES public.memorant (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: departement_fk | type: CONSTRAINT --
-- ALTER TABLE public.filiere DROP CONSTRAINT IF EXISTS departement_fk CASCADE;
ALTER TABLE public.filiere ADD CONSTRAINT departement_fk FOREIGN KEY (id_departement)
REFERENCES public.departement (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.administrateur | type: TABLE --
-- DROP TABLE IF EXISTS public.administrateur CASCADE;
CREATE TABLE public.administrateur (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	id_utilisateur varchar(12)

);
-- ddl-end --
ALTER TABLE public.administrateur OWNER TO postgres;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE public.administrateur DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE public.administrateur ADD CONSTRAINT utilisateur_fk FOREIGN KEY (id_utilisateur)
REFERENCES public.utilisateur (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: administrateur_uq | type: CONSTRAINT --
-- ALTER TABLE public.administrateur DROP CONSTRAINT IF EXISTS administrateur_uq CASCADE;
ALTER TABLE public.administrateur ADD CONSTRAINT administrateur_uq UNIQUE (id_utilisateur);
-- ddl-end --

-- object: public.role | type: TABLE --
-- DROP TABLE IF EXISTS public.role CASCADE;
CREATE TABLE public.role (
	id serial NOT NULL,
	libelle smallint NOT NULL,
	CONSTRAINT role_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.role OWNER TO postgres;
-- ddl-end --

-- object: role_fk | type: CONSTRAINT --
-- ALTER TABLE public.utilisateur DROP CONSTRAINT IF EXISTS role_fk CASCADE;
ALTER TABLE public.utilisateur ADD CONSTRAINT role_fk FOREIGN KEY (id_role)
REFERENCES public.role (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.enseigner | type: TABLE --
-- DROP TABLE IF EXISTS public.enseigner CASCADE;
CREATE TABLE public.enseigner (
	id varchar(12) NOT NULL DEFAULT encode(gen_random_bytes(6), 'hex'),
	enseignant_id varchar NOT NULL,
	filiere_id varchar NOT NULL,
	CONSTRAINT enseigner_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.enseigner OWNER TO postgres;
-- ddl-end --

-- object: fk_dep | type: CONSTRAINT --
-- ALTER TABLE public.departement DROP CONSTRAINT IF EXISTS fk_dep CASCADE;
ALTER TABLE public.departement ADD CONSTRAINT fk_dep FOREIGN KEY (id_chef)
REFERENCES public.enseignant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_memorant | type: CONSTRAINT --
-- ALTER TABLE public.soutenance DROP CONSTRAINT IF EXISTS fk_memorant CASCADE;
ALTER TABLE public.soutenance ADD CONSTRAINT fk_memorant FOREIGN KEY (id_memorant)
REFERENCES public.memorant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_etu1 | type: CONSTRAINT --
-- ALTER TABLE public.memorant DROP CONSTRAINT IF EXISTS fk_etu1 CASCADE;
ALTER TABLE public.memorant ADD CONSTRAINT fk_etu1 FOREIGN KEY (etu1)
REFERENCES public.etudiant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_etu2 | type: CONSTRAINT --
-- ALTER TABLE public.memorant DROP CONSTRAINT IF EXISTS fk_etu2 CASCADE;
ALTER TABLE public.memorant ADD CONSTRAINT fk_etu2 FOREIGN KEY (etu2)
REFERENCES public.etudiant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_maitre | type: CONSTRAINT --
-- ALTER TABLE public.maitre_memoire DROP CONSTRAINT IF EXISTS fk_maitre CASCADE;
ALTER TABLE public.maitre_memoire ADD CONSTRAINT fk_maitre FOREIGN KEY (id_maitre)
REFERENCES public.enseignant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_enseignant | type: CONSTRAINT --
-- ALTER TABLE public.enseigner DROP CONSTRAINT IF EXISTS fk_enseignant CASCADE;
ALTER TABLE public.enseigner ADD CONSTRAINT fk_enseignant FOREIGN KEY (enseignant_id)
REFERENCES public.enseignant (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: fk_filiere | type: CONSTRAINT --
-- ALTER TABLE public.enseigner DROP CONSTRAINT IF EXISTS fk_filiere CASCADE;
ALTER TABLE public.enseigner ADD CONSTRAINT fk_filiere FOREIGN KEY (filiere_id)
REFERENCES public.filiere (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --


