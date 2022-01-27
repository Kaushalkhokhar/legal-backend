from typing import Optional, List, Dict, Set
from pydantic import BaseModel, Field
from datetime import datetime

# from pydantic import BaseModel, EmailStr, Field


class DocsModel(BaseModel):
    title: str
    author: Optional[str]
    edition: Optional[str]
    tribunal: Optional[str]
    act_no:  Optional[str]
    yop: Optional[int]
    type:  Optional[str]
    category: Optional[List[str]] = [] 
    original_source: Optional[str] 
    ref: Optional[List[str]] = []
    user_id: Optional[str] = None
    html: Optional[str]
    view_count: int
    to_display: Optional[bool] = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)




class UpdateDocsModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    edition: Optional[str]
    tribunal: Optional[str]
    act_no:  Optional[str]
    yop: Optional[int]
    type:  Optional[str]
    category: Optional[List[str]] = [] 
    original_source: Optional[str] 
    ref: Optional[List[str]] = []
    user_id: Optional[str] = None
    html: Optional[str]
    view_count: Optional[int]
    to_display: Optional[bool] = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)



def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}













































































# class UserSchema(BaseModel):
#     fullname: str = Field(...)
#     email: EmailStr = Field(...)
#     course_of_study: str = Field(...)
#     year: int = Field(..., gt=0, lt=9)
#     gpa: float = Field(..., le=4.0)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "John Doe",
#                 "email": "jdoe@x.edu.ng",
#                 "course_of_study": "Water resources engineering",
#                 "year": 2,
#                 "gpa": "3.0",
#             }
#         }


# class UpdateUserModel(BaseModel):
#     fullname: Optional[str]
#     email: Optional[EmailStr]
#     course_of_study: Optional[str]
#     year: Optional[int]
#     gpa: Optional[float]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "John Doe",
#                 "email": "jdoe@x.edu.ng",
#                 "course_of_study": "Water resources and environmental engineering",
#                 "year": 4,
#                 "gpa": "4.0",
#             }
#         }


# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}