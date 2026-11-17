# NASA Asteroids API - Python ☄️

## Overview
This project uses Python to connect to NASA's Near-Earth Object Web Service (NeoWs) API and retrieve information about asteroids approaching Earth.

The retrieved JSON data is processed and organized using a custom Python class, then displayed in a formatted summary.

## Features
- Connects to NASA's public REST API using HTTP GET requests.
- Retrieves asteroid data for the current date.
- Parses the JSON response.
- Uses a custom `Asteroid` class to organize asteroid information.
- Displays the following details for each asteroid:
  - Asteroid Name
  - Estimated Maximum Diameter (km)
  - Close Approach Date
  - Potentially Hazardous Status
- Checks the HTTP response status code.

## Technologies Used
- Python
- Requests
- Python-dotenv
- NASA NeoWs API

## Project Structure
```text
nasa-asteroids-api-python/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/IsraaXx/nasa-asteroids-api-python.git
cd nasa-asteroids-api-python
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

Create a `.env` file in the project directory and add your NASA API key:

```env
NASA_API_KEY=your_api_key_here
```

You can obtain a free API key from the [NASA API Portal](https://api.nasa.gov/).

### 6. Run the Project
```bash
python main.py
```

## Example Output
```text
Request sent successfully!

Name: (2019 HW3)
Diameter (km): 0.123
Close Approach Date: 2026-11-17
Potentially Hazardous: False
----------------------------------------
```

*Note: The actual output depends on the asteroid data returned by NASA's API.*

## API Reference
**NASA NeoWs Feed API**

Endpoint:
`https://api.nasa.gov/neo/rest/v1/feed`

Official Documentation: https://api.nasa.gov/