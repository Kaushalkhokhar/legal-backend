import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Docs
docs_collection = database.get_collection("docs_collection")

def doc_helper(doc) -> dict:  
    return {
        "id": str(doc["_id"]),
        "title": doc["title"],
        "author": doc["author"],
        "edition": doc["edition"],
        "tribunal": doc["tribunal"],
        "act_no": doc["act_no"],
        "yop": doc["yop"],
        "type": doc["type"],
        "category": doc["category"],
        "source_url": doc["original_source"],
        "ref": doc["ref"],
        "user_id": doc["user_id"],
        "html_id": doc["html"],
        "view_count": doc["view_count"],
        "display": doc["to_display"],
        "create_at": doc["created_at"],
        "update_at": doc["updated_at"],
    }
    
# Retrieve all docs present in the database
async def retrieve_docs():
    docs = []
    async for doc in docs_collection.find():
        docs.append(doc_helper(doc))
    return docs


# Add a new docs into to the database
async def add_docs(doc_data: dict) -> dict:
    doc = await docs_collection.insert_one(doc_data)
    new_doc = await docs_collection.find_one({"_id": doc.inserted_id})
    return doc_helper(new_doc)


# Retrieve a docs with a matching ID
async def retrieve_doc(id: str) -> dict:
    doc = await docs_collection.find_one({"_id": ObjectId(id)})
    if doc:
        return doc_helper(doc)


# Update a docs with a matching ID
async def update_doc(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    doc = await docs_collection.find_one({"_id": ObjectId(id)})
    if doc:
        updated_doc = await docs_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_doc:
            return True
        return False


# Delete a docs from the database
async def delete_doc(id: str):
    doc = await docs_collection.find_one({"_id": ObjectId(id)})
    if doc:
        await docs_collection.delete_one({"_id": ObjectId(id)})
        return True