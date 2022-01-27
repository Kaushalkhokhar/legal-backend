import pymongo

def add_query(userID,email,userName,firstName,lastName,middleName,loginProvider,bio,gender,birthDate,birthYear,userStatus,userRole,lastSessionStartTime,lastLoginAt,lastSessionEndTime,failedAttempts,signinCount,token,unlockToken,resetPasswordSentAt,resetPasswordToken,deviceId,deviceToken,ipv6,ipv4,deviceType,deviceOs,location,meta,createdAt,updatedAt,isDeleted,createdBy,updatedBy):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["application"]
    mycol = mydb["users"]

    user_info = {
        "userID": f"{userID}" ,
        "email": f"{email}",
        "userName": f"{userName}",
        "firstName": f"{firstName}",
        "lastName": f"{lastName}",
        "middleName": f"{middleName}",
        "loginProvider": f"{loginProvider}",
        "bio": f"{bio}",       
        "gender": f"{gender}",
        "birthDate": f"{birthDate}",
        "birthYear": f"{birthYear}",
        "userStatus": f"{userStatus}",
        "userRole": f"{userRole}",
        "lastSessionStartTime":f"{lastSessionStartTime}",
        "lastLoginAt":f"{lastLoginAt}",
        "lastSessionEndTime":f"{lastSessionEndTime}",
        "failedAttempts": f"{failedAttempts}",
        "signinCount": f"{signinCount}",
        "token": f"{token}",
        "unlockToken": f"{unlockToken}",
        "resetPasswordSentAt": f"{resetPasswordSentAt}",
        "resetPasswordToken": f"{resetPasswordToken}",
        "deviceId": f"{deviceId}",
        "deviceToken" : f"{deviceToken}",
        "ipv6": f"{ipv6}",
        "ipv4": f"{ipv4}",
        "deviceType": f"{deviceType}",
        "deviceOs": f"{deviceOs}",
        "location": f"{location}",
        "meta": f"{meta}",
        "createdAt": f"{createdAt}",
        "updatedAt": f"{updatedAt}",
        "isDeleted": f"{isDeleted}",
        "createdBy": f"{createdBy}",
        "updatedBy": f"{updatedBy}",
    }
    
    x = mycol.insert_one(user_info)
    
    return {"message" : "Succesfully created your account"}
    # x = mycol.insert_one(mydict)
    # y = mycol.insert_one(mydict2)

    # for one in mycol.find():
    #     print(one.get("_id"))

    # myquery = ({"name" : {"$regex" : "^a"}})
    # x = mycol.delete_many(myquery)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["application"]
# mycol = mydb["users"]
# mycol.create_index("user_index")
# import pdb
# pdb.set_trace()
# mycol.find( { $text: { $search: "cus" } } )