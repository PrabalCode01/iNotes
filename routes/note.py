from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity , notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter() 
templates = Jinja2Templates(directory="templates")




@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  # Convert ObjectId to string
            "notes": doc.get("notes", "No Content")  # Safeguard against missing "notes"
        })
    
    # Print newDocs to the console for debugging
    print(newDocs)
    
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
