from mongoengine import Document, StringField, IntField, connect
from config import Settings

settings = Settings()

# Connexion à MongoDB
connect(
    db=settings.MONGODB_DATABASE,
    host=settings.MONGODB_CONNECTION_STRING
)

class Passage(Document):
    _id = IntField(primary_key=True)
    passage = StringField()

    def create_passage(self, passage_data):
        passage = Passage(**passage_data)
        passage.save()
        return {"message": "Passage created"}

    def update_passage(self, passage_data):
        passage = Passage.objects(_id=passage_data["_id"]).first()
        if passage:
            passage.passage = passage_data["passage"]
            passage.save()
            return {"message": "Passage updated"}
        else:
            return {"error": "Passage not found"}

    def delete_passage(self, passage_id):
        passage = Passage.objects(_id=passage_id).first()
        if passage:
            passage.delete()
            return {"message": "Passage deleted"}
        else:
            return {"error": "Passage not found"}
