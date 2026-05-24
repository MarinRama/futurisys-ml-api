from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    age: float = Field(..., json_schema_extra={"example": 26})
    genre: str = Field(..., json_schema_extra={"example": "M"})
    revenu_mensuel: float = Field(..., json_schema_extra={"example": 2000})
    statut_marital: str = Field(..., json_schema_extra={"example": "Célibataire"})
    departement: str = Field(..., json_schema_extra={"example": "Consulting"})
    poste: str = Field(..., json_schema_extra={"example": "Consultant"})
    nombre_experiences_precedentes: float = Field(..., json_schema_extra={"example": 2})
    annee_experience_totale: float = Field(..., json_schema_extra={"example": 2})
    annees_dans_l_entreprise: float = Field(..., json_schema_extra={"example": 1})
    annees_dans_le_poste_actuel: float = Field(..., json_schema_extra={"example": 1})
    satisfaction_employee_environnement: float = Field(..., json_schema_extra={"example": 4})
    note_evaluation_precedente: float = Field(..., json_schema_extra={"example": 4})
    satisfaction_employee_nature_travail: float = Field(..., json_schema_extra={"example": 3})
    satisfaction_employee_equipe: float = Field(..., json_schema_extra={"example": 4})
    satisfaction_employee_equilibre_pro_perso: float = Field(..., json_schema_extra={"example": 3})
    note_evaluation_actuelle: float = Field(..., json_schema_extra={"example": 4})
    heure_supplementaires: str = Field(..., json_schema_extra={"example": "Oui"})
    augementation_salaire_precedente: str = Field(..., json_schema_extra={"example": "11 %"})
    nombre_participation_pee: float = Field(..., json_schema_extra={"example": 1})
    nb_formations_suivies: float = Field(..., json_schema_extra={"example": 3})
    distance_domicile_travail: float = Field(..., json_schema_extra={"example": 12})
    niveau_education: float = Field(..., json_schema_extra={"example": 3})
    domaine_etude: str = Field(..., json_schema_extra={"example": "Informatique"})
    frequence_deplacement: str = Field(..., json_schema_extra={"example": "Rarement"})
    annees_depuis_la_derniere_promotion: float = Field(..., json_schema_extra={"example": 1})
    annes_sous_responsable_actuel: float = Field(..., json_schema_extra={"example": 2})



class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    interpretation: str