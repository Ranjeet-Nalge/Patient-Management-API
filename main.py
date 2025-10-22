from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import json
from fastapi import FastAPI, HTTPException, Query, Path


app = FastAPI(title="Patient Management API")


class Patient(BaseModel):

    patient_id: int = Field(...,
                            gt=1,
                            description="ID of the patient",
                            json_schema_extra={"example":10})
    name: str = Field(...,
                      description="Name of the patient",
                      json_schema_extra={"example":"Your Name"})
    age: int = Field(...,
                     description="Age of the patient",
                     ge=1,
                     le=120,
                     json_schema_extra={"example":30})
    weight: float = Field(...,
                          description="Weight of the patient",
                          json_schema_extra={"example": 50.50})
    symptoms: List[str] = Field(...,
                                description="symptoms of the patients",
                                min_length=1,
                                max_length=5,
                                json_schema_extra={"example":["fever", "cough"]})
    contact : Dict[str, str] = Field(...,
                                     max_length=3,
                                     json_schema_extra={"example": {"phone": "+91-9876543210",
        "address": "123 MG Road, Mumbai, Maharashtra"}})


def load_patient_data():

    with open("patient_data_json.json", mode="r") as f:
        data = json.load(f)

    return data

patient_data = load_patient_data()


@app.get("/")
def homepage():

    return {"message":"this is the patient management api homepage".title()}

@app.get("/view")
def view_patients():
    data = patient_data
    if not data:
        raise HTTPException(status_code=404, detail="no data found!".title())
    return data

@app.get("/patient/{patient_id}")
def get_patient_by_id(patient_id: int = Path(...,
                                              ge=1,
                                              title="Enter patient id: ",
                                              description="enter patient id ".title(),
                                              json_schema_extra={"example": 1})):
    patients = patient_data["patients"]

    for patient in patients:
        if patient["patient_id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail=f"given id {patient_id} doesnt exit.!")

@app.post("/add")
def add_patient(new_patient: Patient):

    data = patient_data
    if "patients" not in data:
        data["patients"] = []

    # check for duplicates ids

    for patient in data["patients"]:
        if patient["patient_id"] == new_patient.patient_id:
            raise HTTPException(status_code=400, detail=f"patient id of {new_patient.patient_id} already exist.")

    # add new patient
    data["patients"].append(new_patient.model_dump())

    # write to json file to persist changes
    with open("patient_data_json.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"message":"new patient has been added/created.".title(), "new patient".title():new_patient}