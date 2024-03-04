from pymongo.mongo_client import MongoClient

def add_user(user: str, password: str, email: str = None, name: str = None, 
                db_name: str = "systemy_rozproszone", collection_name: str="users",
                uri="mongodb+srv://spambartosz123:c0WDL8nciXDSAo1w@cluster0.ffekdag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    user_data = {
        "user": user,
        "email": email,
        "name": name,
        "password": password
    }

    insert_result = collection.insert_one(user_data)

    if insert_result.inserted_id:
        print("User inserted successfully")
    else:
        print("Failed to insert user")

def find_password_by_name(name: str, 
                            db_name: str = "systemy_rozproszone", collection_name: str="users",
                            uri="mongodb+srv://spambartosz123:c0WDL8nciXDSAo1w@cluster0.ffekdag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") -> str:

    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    user = collection.find_one({"name": name})

    if user:
        return user.get("password")
    else:
        return None
    
def find_username(username: str, 
                            db_name: str = "systemy_rozproszone", collection_name: str="users",
                            uri="mongodb+srv://spambartosz123:c0WDL8nciXDSAo1w@cluster0.ffekdag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") ->bool:
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    user = collection.find_one({"user": username})

    # Check if user exists
    if user:
        return True
    else:
        return False

def get_user_data_from_mongodb(self, 
                                db_name: str = "systemy_rozproszone", collection_name: str="users") -> dict:
    db = self.client[db_name]
    collection = db[collection_name]
    users = collection.find()

    credentials = {"usernames": {}}
    for user in users:
        username = user.get("user")
        name = user.get("name")
        password = user.get("password")
        user_dict = {"name": name, "password": password}
        credentials["usernames"].update({username: user_dict})
    return credentials


# data = Database()
# data.add_user("Bartek", "user@example.com", "Bartek", "Bartek")

# name_to_search = "Example User"
# password = data.find_password_by_name(name_to_search)
# if password:
#     print(f"Password for user '{name_to_search}': {password}")
# else:
#     print(f"User '{name_to_search}' not found")
