from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-19",
      "updated_at": "2025-02-19"
    },
    "descriptions": {
      "app_description": "sends notifications to slack",
      "app_logo": "URL to the application logo.",
      "app_name": "Exercise Tracker",
      "app_url": "100.25.191.235",
      "background_color": "#HEXCODE"
    },
    "integration_category": "Communication & Collaboration",
    "integration_type": "output",
    "is_active": True,
    "output": [
      {
        "label": "output_channel_1",
        "value": True
      },
    ],
    "key_features": [
      "Feature description 1.",
      "Feature description 2.",
      "Feature description 3.",
      "Feature description 4."
    ],
    "permissions": {
      "monitoring_user": {
        "always_online": True,
        "display_name": "Performance Monitor"
      }
    },
    "settings": [
      {
        "label": "interval",
        "type": "text",
        "required": True,
        "default": "* * * * *"
      },
      {
        "label": "Key",
        "type": "text",
        "required": True,
        "default": "1234567890"
      },
      {
        "label": "Do you want to continue",
        "type": "checkbox",
        "required": True,
        "default": "Yes"
      },
      {
        "label": "Provide Speed",
        "type": "number",
        "required": True,
        "default": "1000"
      },
      {
        "label": "Sensitivity Level",
        "type": "dropdown",
        "required": True,
        "default": "Low",
        "options": ["High", "Low"]
      },
      {
        "label": "Alert Admin",
        "type": "multi-checkbox",
        "required": True,
        "default": "Super-Admin",
        "options": ["Super-Admin", "Admin", "Manager", "Developer"]
      }
    ],
    "tick_url": "URL for subscribing to Telex's clock.",
    "target_url": os.getenv("SLACK_WEBHOOK_URL"),
  }
}

@router.get("/integration-json")
async def get_integration_json():
    return JSONResponse(content=integration_json)