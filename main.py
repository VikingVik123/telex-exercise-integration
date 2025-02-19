import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router

api_key = "zuq/hiBZxcaGPHYblr30kw==klbwkoKYvSMnDUqi"
api_url = "https://api.api-ninjas.com/v1/exercises?muscle="
muscles = ["glutes", "abs", "chest", "arms", "leg", "triceps",
           "abdominals", "abductors", "adductors", "biceps",
           "calves", "forearms", "hamstrings", "lats",
           "lower_back", "middle_back", "neck", "quadriceps", "traps"]

muscle_index = 0

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

@app.get("/exe")
async def get_exercises():
    global muscle_index
    muscle = muscles[muscle_index]
    full_url = f"{api_url}{muscle}"
    
    response = requests.get(full_url, headers={"X-Api-Key": api_key})
    
    muscle_index = (muscle_index + 1) % len(muscles)
    
    if response.status_code == requests.codes.ok:
        return response.json()[0] if response.json() else {"message": "No data available"}
    else:
        return {"error": response.status_code, "message": response.text}
