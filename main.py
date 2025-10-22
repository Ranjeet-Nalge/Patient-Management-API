from pydantic import BaseModel, Field
from typing import List, Dict, Optional


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


