from pydantic import BaseModel 

class RootResponse(BaseModel):
    """
    Response model for the root endpoint 
    """
    application: str 
    version: str 
    status : str 


# what we have done in this
# 1. we have create a class that describe the response of the root endpoint 
# 2. using pydantic BaseModel we can define the schema of the response 
# 3. using pydantic BaseModel we can validate the response 