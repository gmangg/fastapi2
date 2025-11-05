from fastapi import APIRouter, HTTPException
from db.models import User

router = APIRouter()

@router.get("/")
def get_all_users():
    #Add code to return all users
    return {"Message": "Success!"}

#Create route for GET USER
@router.get("/{user_id}")
def get_user(user_id:int):
    #Add code to get user from DB
    user = None
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", status_code=204)
def create_new_user(user: User):
    #Add code to create the user
    new_user = user
    return new_user
