users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
veri= list(filter(lambda x:x['verified']==True,users))
veri1= [user['email'] for user in veri]
print(list(veri1))