from sqlmodel import SQLModel
from fastapi import FastAPI
import json


app:FastAPI = FastAPI()

class RequiredParameters(SQLModel):
    location: str


@app.post("/get_temperature")
def get_current_temperature (required_parameters : RequiredParameters):
    location = required_parameters.location
    if "karachi" in location.lower():
        return json.dumps({"location": "Karachi", "temperature": "10", "unit": "celsius"})
    elif "islamabad" in location.lower():
        return json.dumps({"location": "Islamabad", "temperature": "72", "unit": "fahrenheit"})
    elif "lahore" in location.lower():
        return json.dumps({"location": "Lahore", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})



