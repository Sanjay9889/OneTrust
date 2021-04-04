from fastapi import FastAPI

# FastAPI app
from models import Tag
from settings import col_ref

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to One Trust!!"}


@app.post("/increment_count/")
async def increment_count(tag: Tag):
    name = tag.name
    value = tag.value
    doc_ref = col_ref.document(name)
    doc = doc_ref.get()
    if doc.exists:
        existing_value = doc.to_dict()["value"]
        new_value = existing_value + value
        doc_ref.update({
            u'value': new_value})
    else:
        doc_ref.set({
            u'value': value})
    return {"message": f"{tag} has been created successfully!!"}


@app.get("/get_tags/")
async def get_tags():
    all_docs = col_ref.stream()
    tags = {}
    for doc in all_docs:
        print(doc.id)
        tags[doc.id] = doc.to_dict()["value"]
    return tags
