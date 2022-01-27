from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_docs,
    add_docs,
    retrieve_doc,
    update_doc,
    delete_doc,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    DocsModel,
    UpdateDocsModel,
)

router = APIRouter()

# For create
@router.post("/", response_description="doc data added into the database")
async def add_doc_data(user: DocsModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_docs(user)
    return ResponseModel(new_user, "doc added successfully.")


# For read
@router.get("/", response_description="docs retrieved")
async def get_docs():
    users = await retrieve_docs()
    if users:
        return ResponseModel(users, "docs data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="user data retrieved")
async def get_doc_data(id):
    user = await retrieve_doc(id)
    if user:
        return ResponseModel(user, "doc data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "doc doesn't exist.")


# For update
@router.put("/{id}")
async def update_docs_data(id: str, req: UpdateDocsModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_doc(id, req)
    if updated_user:
        return ResponseModel(
            "doc with ID: {} update is successful".format(id),
            "docs updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the doc data.",
    )
    

# For delete
@router.delete("/{id}", response_description="doc data deleted from the database")
async def delete_docs_data(id: str):
    deleted_user = await delete_doc(id)
    if deleted_user:
        return ResponseModel(
            "doc with ID: {} removed".format(id), "doc deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "doc with id {0} doesn't exist".format(id)
    )