from pydantic import BaseModel 

class HealthResponse(BaseModel):
    """
    Response model for the health endpoint 
    """
    status: str 
    debug: bool 



# what we have done is this we have created a class thet escribe the health end point 
# using pydantic we can define the schema and the data validation 
