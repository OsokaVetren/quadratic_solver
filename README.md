This is a quadratic equations solver written on python

Libraries used:

    FastAPI – web framework used to build the API and handle data validation.

    Uvicorn – ASGI server used to run the application.
    
    SQLAlchemy – An ORM library used to interact with the SQLite database and store calculation history.
    
    Pytest – A testing framework used to verify the mathematical logic and API endpoints.
    
    HTTPX – An HTTP client used to perform integration tests on the service.

Download and launch:

1. clone the repository

```git clone https://github.com/OsokaVetren/quadratic_solver ```

2. set up virtual enviroment

``` python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

3. install dependencies

```pip install -r requirements.txt```

4. launch server

```uvicorn app.main:app --reload ```
