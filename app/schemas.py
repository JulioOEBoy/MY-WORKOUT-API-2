from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class WorkoutBase(BaseModel):
    title: str
    description: str

class WorkoutCreate(WorkoutBase):
    user_id: int

class Workout(WorkoutBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
