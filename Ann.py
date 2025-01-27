import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("/Users/annerinjeri/Downloads/powerhouse-62f4d-firebase-adminsdk-fbsvc-9a2e946c98.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
goals = [{'Energy Goal': '780kJ',
'Time Stamp': '11:03:45 Jan 13 2025',
'Goal Evaluation Date':'Jan 20 2025'} ,
{'Energy Goal': '720kJ','Time Stamp': '01:03:45 Jan 22 2025','Goal Evaluation Date':'Jan 29 2025'}, {'Energy Goal': '820kJ','Time Stamp': '01:03:45 Jan 2 2025','Goal Evaluation Date':'Jan 7 2025' }]
devices = [{'Name': 'Thermostat','Room': 'Living Room', 'Information': {'Model': 'T1000', 'IPAddress': '192.168.1.1', 'ConnectionType': 'WiFi'} },
{'Name': "AC",'Room': 'Living Room', 'Information': {'Model': 'T2000', 'IPAddress': '192.008.1.1', 'ConnectionType': 'WiFi'} }]

def set_doc_data(coll_ref,data):
    for i in range(len(data)):
        
        coll_ref.document().set(data[i])

def delete_collection(coll_ref, coll_size):
    if coll_size == 0:
        return

    docs = coll_ref.list_documents(page_size=coll_size)
    deleted = 0

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()
        deleted = deleted + 1

    if deleted >= coll_size:
        return delete_collection(coll_ref, coll_size)
    
delete_collection(db.collection("Devices"),2) #find way to find count 
delete_collection(db.collection("Energy Saving Goals"),2)
set_doc_data(db.collection("Energy Saving Goals"),goals)
set_doc_data(db.collection("Devices"),devices)

