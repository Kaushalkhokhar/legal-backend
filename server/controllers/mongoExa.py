import pymongo

def add_query(title,author,edition,tribunal,act_no,yop,type,category,original_source,ref,user_id,html,view_count,to_display,created_at,updated_at):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["application"]
    mycol = mydb["docs"]

    docs_info = {
        "title": f"{title}",
        "author": f"{author}",
        "edition": f"{edition}",
        "tribunal": f"{tribunal}",
        "act_no":  f"{act_no}",
        "yop": f"{yop}",
        "type":  f"{type}",
        "category": f"{category}",
        "original_source": f"{original_source}",
        "ref": f"{ref}",
        "user_id": f"{user_id}",
        "html": f"{html}",
        "view_count": f"{view_count}",
        "to_display": f"{to_display}",
        "created_at": f"{created_at}",
        "updated_at": f"{updated_at}",


    }
    
    x = mycol.insert_one(docs_info)
    
    return {"message" : "Succesfully created your account"}
    # x = mycol.insert_one(mydict)
    # y = mycol.insert_one(mydict2)

    # for one in mycol.find():
    #     print(one.get("_id"))

    # myquery = ({"name" : {"$regex" : "^a"}})
    # x = mycol.delete_many(myquery)
