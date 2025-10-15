from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from models import Passage

app = FastAPI()

class PassageModel(BaseModel):
    id: int = Field(..., alias="_id")
    passage: str

class DeleteModel(BaseModel):
    _id: str

@app.post("/passage", status_code=201)
async def create_passage(passage: PassageModel):
    try:
        passage_obj = Passage(_id=passage.id, passage=passage.passage)  # Explicitly set _id
        passage_obj.save()
        return {"message": "Passage created"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/passage")
async def update_passage(passage: PassageModel):
    try:
        passage_obj = Passage.objects(_id=passage._id).first()
        if passage_obj:
            passage_obj.passage = passage.passage
            passage_obj.save()
            return {"message": "Passage updated"}
        else:
            raise HTTPException(status_code=404, detail="Passage not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/passage")
async def delete_passage(delete_data: DeleteModel):
    try:
        passage_obj = Passage.objects(_id=delete_data._id).first()
        if passage_obj:
            passage_obj.delete()
            return {"message": "Passage deleted"}
        else:
            raise HTTPException(status_code=404, detail="Passage not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/passage/{passage_id}")
async def get_passage(passage_id: int):
    try:
        passage_obj = Passage.objects(_id=passage_id).first()
        if passage_obj:
            return {
                "_id": passage_obj._id,
                "passage": passage_obj.passage
            }
        else:
            raise HTTPException(status_code=404, detail="Passage not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

