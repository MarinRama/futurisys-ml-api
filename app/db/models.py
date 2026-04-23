from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base


class EmployeeDataset(Base):
    __tablename__ = "employees_dataset"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Float)
    genre = Column(String)
    revenu_mensuel = Column(Float)
    statut_marital = Column(String)
    departement = Column(String)
    poste = Column(String)
    nombre_experiences_precedentes = Column(Float)
    nombre_heures_travailless = Column(Float)
    annee_experience_totale = Column(Float)
    annees_dans_l_entreprise = Column(Float)
    annees_dans_le_poste_actuel = Column(Float)
    satisfaction_employee_environnement = Column(Float)
    note_evaluation_precedente = Column(Float)
    satisfaction_employee_nature_travail = Column(Float)
    satisfaction_employee_equipe = Column(Float)
    satisfaction_employee_equilibre_pro_perso = Column(Float)
    note_evaluation_actuelle = Column(Float)
    heure_supplementaires = Column(String)
    augementation_salaire_precedente = Column(String)
    nombre_participation_pee = Column(Float)
    nb_formations_suivies = Column(Float)
    nombre_employee_sous_responsabilite = Column(Float)
    distance_domicile_travail = Column(Float)
    niveau_education = Column(Float)
    domaine_etude = Column(String)
    ayant_enfants = Column(String)
    frequence_deplacement = Column(String)
    annees_depuis_la_derniere_promotion = Column(Float)
    annes_sous_responsable_actuel = Column(Float)


class PredictionRequestDB(Base):
    __tablename__ = "prediction_requests"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    age = Column(Float)
    genre = Column(String)
    revenu_mensuel = Column(Float)
    statut_marital = Column(String)
    departement = Column(String)
    poste = Column(String)
    nombre_experiences_precedentes = Column(Float)
    nombre_heures_travailless = Column(Float)
    annee_experience_totale = Column(Float)
    annees_dans_l_entreprise = Column(Float)
    annees_dans_le_poste_actuel = Column(Float)
    satisfaction_employee_environnement = Column(Float)
    note_evaluation_precedente = Column(Float)
    satisfaction_employee_nature_travail = Column(Float)
    satisfaction_employee_equipe = Column(Float)
    satisfaction_employee_equilibre_pro_perso = Column(Float)
    note_evaluation_actuelle = Column(Float)
    heure_supplementaires = Column(String)
    augementation_salaire_precedente = Column(String)
    nombre_participation_pee = Column(Float)
    nb_formations_suivies = Column(Float)
    nombre_employee_sous_responsabilite = Column(Float)
    distance_domicile_travail = Column(Float)
    niveau_education = Column(Float)
    domaine_etude = Column(String)
    ayant_enfants = Column(String)
    frequence_deplacement = Column(String)
    annees_depuis_la_derniere_promotion = Column(Float)
    annes_sous_responsable_actuel = Column(Float)

    result = relationship("PredictionResultDB", back_populates="request", uselist=False)


class PredictionResultDB(Base):
    __tablename__ = "prediction_results"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("prediction_requests.id"), nullable=False)
    prediction = Column(Integer, nullable=False)
    probability = Column(Float, nullable=False)
    interpretation = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    request = relationship("PredictionRequestDB", back_populates="result")