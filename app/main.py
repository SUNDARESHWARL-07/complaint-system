from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.init_db import init_db
from app.routes.complaint_routes import router as complaint_router
from app.routes.defect_routes import router as defect_router

app = FastAPI()

# ✅ ADD CORS HERE (EARLY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/")
def home():
    return {"message": "System Running"}

app.include_router(complaint_router)
app.include_router(defect_router)