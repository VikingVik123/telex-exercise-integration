int_json = {
  "data": {
    "date": {
      "created_at": "2025-02-21",
      "updated_at": "2025-02-21"
    },
    "descriptions": {
      "app_name": "Daily WorkOut",
      "app_description": "Fetches workout data from an exercise API and sends it to Slack via Telex.",
      "app_logo": "https://images.app.goo.gl/XTLJhuQC53HMV6HY8",
      "app_url": "https://telex-integration-evq8.onrender.com/",
      "background_color": "#000000"
    },
    "is_active": True,
    "integration_category": "Communication & Collaboration",
    "integration_type": "output",
    "key_features": [
      "Fetches workout data from an exercise API."
    ],
    "website": "https://telex-integration-evq8.onrender.com/exe",
    "author": "Victor",
    "settings": [
      {
        "label": "slack-channel",
        "type": "text",
        "required": True,
        "default": "#ExerciseAlert"
      },
      {
        "label": "time interval",
        "type": "dropdown",
        "required": True,
        "default": "* * * * *",
        "options": ["15", "30", "45", "60", "120"]
      }
    ],
    "target_url": "https://hooks.slack.com/services/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"
  }
}
