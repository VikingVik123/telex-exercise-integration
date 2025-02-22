import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router
from dotenv import load_dotenv
from integration import int_json
import os

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API Key is missing. Set the 'API_KEY' environment variable.")

telex_webhook_url = os.getenv("TELEX_WEBHOOK_URL")
if not telex_webhook_url:
    raise ValueError("Telex Webhook URL is missing. Set 'TELEX_WEBHOOK_URL' in environment variables.")

api_url = "https://api.api-ninjas.com/v1/exercises?muscle="
muscles = [
    "glutes", "chest", "arms", "leg", "triceps",
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

            if not data:
                return {"error": "No exercises found for this muscle group."}

            first_exercise = data[0]

            telex_payload = {
                "event_name": "exercise_update",
                "username": "FitnessBot",
                "status": "success",
                "message": f"New exercise retrieved: {first_exercise.get('name', 'Unknown'),
                                                      first_exercise.get('type', 'unknown'),
                                                      first_exercise.get('muscle', 'unknown'),
                                                      first_exercise.get('equipment', 'unknown'),
                                                      first_exercise.get('difficulty', 'unknown'),
                                                      first_exercise.get('instructions', 'unknown')}",
            }

            webhook_response = requests.post(telex_webhook_url, json=telex_payload)

            if webhook_response.status_code == 200:
                return {
                    "exercise": first_exercise,
                    "webhook_status": "Successfully sent to Telex",
                }
            else:
                return {
                    "exercise": first_exercise,
                    "webhook_status": f"Failed to send to Telex: {webhook_response.status_code}",
                    "webhook_response": webhook_response.text,
                }
        else:
            return {
                "error": response.status_code,
                "message": response.json().get("error", "Unknown error occurred"),
            }
            
    except requests.RequestException as e:
        return {"error": "Request failed", "message": str(e)}

@app.get("/integration.json")
async def get_integration():
    return int_json
