# Mini-Data-Query-Simulation-Engine
This project simulates a simplified data query system using a mock in-memory database. It provides a REST API(POSTMAN) to interact with the data using natural language queries.You can query the data easily using RESTAPI and can be used only with authorization.
.
## Project Structure

* 'data.py': Contains the mock in-memory database and data access functions accesible for the users.
* 'query_engine.py': It handles natural language query translation, processing, validation, and pseudo-SQL conversion.
* 'test.py': We are implementing the Flask REST API with authentication to test the mock database.

## Setup Instructions

1.  **Clone the Repository (if applicable):**

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2.  **Install Dependencies:**
   
    Setup your environment if required.
    ---
    Install Flask:

    for bash
    pip install Flask

4.  **Run the Flask Application:**

    Save the provided code as same name as'data.py', 'query_engine.py' and 'test.py' in the same directory.Then run:

    ---bash
    python test.py

    The Flask development server will start, and it will provide you the link like this 'http://127.0.0.1:5000/',
    copy this link into your postman and paste the link and set the type to "POST",

## API Documentation

### Endpoints

**'/query' (POST):** It Simulates AI-powered data query processing with proper output.
**'/explain' (POST):** Returns a simulated query which breakdowns to explain the query.
**'/validate' (POST):** Checks query whether it is feasible to run or not.

## Render Documenation

-Make an account on render.
Create a new Web Service and add this Github Repo:
<tarun02-git/Mini-Data-Query-Simulation-Engine>

Language : <Programming Langauge with version>

Branch : main/master.

Region: <Your region>

Build:
<pip install -r requirements.txt>

Start Command:
<gunicorn test:app>

Deploy Your Web Service.

Copy the link after your Service is ready,
Link:<https://mini-data-query-simulation-engine-2.onrender.com>
and use it accordingly (via POSTMAN) to simulate the query.

### Request Format (JSON)

All endpoints accept a JSON payload with a `query` field containing the natural language query.

---json
{
    "query": "Your natural language query here"
}
---example query
{
    "query": "What is the price of laptops?"
}

### Request Format For Render (JSON)

All endpoints accept a JSON payload with a `query` field containing the natural language query.

---json
{
    "query": "Your natural language query here"
}
---example query
{
    "query": "What is the price of laptops?"
}
