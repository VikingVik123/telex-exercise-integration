# Exercise Retrieval API

## Overview

This FastAPI-based API retrieves exercise information based on different muscle groups using the API Ninjas Exercise API. It rotates through a predefined list of muscle groups and sends the retrieved exercise data to a Telex webhook.

## Features

1. Fetches exercise details for different muscle groups.

2. Uses API Ninjas for exercise data.

3. Sends retrieved exercise information to a Telex webhook.

4. Supports CORS for cross-origin requests.

5. Provides an integration JSON endpoint.

## Requirements

1. Python 3.8+

2. requests

3. fastapi

4. uvicorn

5. python-dotenv

## Installation

Clone the repository:

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Environment Variables

Create a .env file in the root directory and add the following variables:

API_KEY=your_api_ninjas_key
TELEX_WEBHOOK_URL=your_telex_webhook_url

### Running the API

Start the FastAPI server with:

uvicorn main:app --reload

### API Endpoints

#### GET /exe

Retrieves an exercise for the current muscle group and moves to the next in rotation.

Sends the exercise details to Telex webhook.

Returns:

{
  "exercise": { ...exercise data... },
  "webhook_status": "Successfully sent to Telex"
}

#### GET /integration.json

Returns the integration JSON file.

### Error Handling

If the API key is missing, an error is raised.

If the Telex webhook URL is missing, an error is raised.

If the API call fails, appropriate error messages are returned.