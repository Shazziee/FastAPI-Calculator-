from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal  # literal is a typehint used to restrict values to specific, allowed values. Pydantic enforces type hints.
# python and the API client both need to know something went wrong. HTTPException handles both

app = FastAPI() # creates fastAPI application

# PYDANTIC MODEL 
class Calculation(BaseModel):  # BaseModel creates a Pydantic model called Calculation
    a: float
    b: float
    operation:Literal["+", "-", "*", "/"]  # validation will now happen before the function runs 

@app.post("/calculate")  # post is used when sending data to a server 
def calculate(calculation: Calculation): # calculation is the variable name, Calculation is a model within the Pydantic model
   
   if calculation.operation == "+":
       result = calculation.a + calculation.b

   elif calculation.operation == "-":
       result = calculation.a - calculation.b

   elif calculation.operation == "*":
       result = calculation.a * calculation.b

   elif calculation.operation == "/":
       if calculation.b == 0:
           raise HTTPException(  # raise stops a function immediately when something goes wrong
               status_code=400,   # tell the client this was a 400 Bad Request
               detail="Cannot divide by zero")
       result = calculation.a / calculation.b

   else:
       raise HTTPException(
           status_code=400,
           detail="Invalid operation")
       
   return {"result": result}

