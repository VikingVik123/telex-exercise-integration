import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router
import os

api_key = "zuq/hiBZxcaGPHYblr30kw==klbwkoKYvSMnDUqi"
if not api_key:
    raise ValueError("API Key is missing. Set the 'api_key' environment variable.")

api_url = "https://api.api-ninjas.com/v1/exercises?muscle="
muscles = [
    "glutes", "abs", "chest", "arms", "leg", "triceps",
    "abdominals", "abductors", "adductors", "biceps",
    "calves", "forearms", "hamstrings", "lats",
    "lower_back", "middle_back", "neck", "quadriceps", "traps"
]

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

    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(full_url, headers=headers)
        muscle_index = (muscle_index + 1) % len(muscles)

        if response.status_code == 200:
            data = response.json()
            return data[0] if data else {"message": "No exercises found for this muscle group."}
        else:
            return {
                "error": response.status_code,
                "message": response.json().get("error", "Unknown error occurred"),
            }
    except requests.RequestException as e:
        return {"error": "Request failed", "message": str(e)}
