from google.cloud import firestore

# Add a new document
db = firestore.Client.from_service_account_json("onetrustkey.json")
col_ref = db.collection(u'onetrust')
