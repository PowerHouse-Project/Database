import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("/Users/annerinjeri/Downloads/powerhouse-62f4d-firebase-adminsdk-fbsvc-9a2e946c98.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
data = {
'Energy Goal': '780kJ',
'Time Stamp': '11:03:45 Jan 13 2025',
'Goal Evaluation Date':'Jan 20 2025' } 


db.collection('Energy Saving Goals').document("Goal1").set(data)



def delete_collection(coll_ref, batch_size):
    if batch_size == 0:
        return

    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
    
delete_collection(db.collection("energySavingGoals"),2)
