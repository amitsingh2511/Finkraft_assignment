# Finkraft_assignment

## API Documentation (Swagger UI)

FastAPI provides an interactive API documentation through Swagger UI. You can access it by navigating to the following URL in your browser:

- [Swagger UI](http://127.0.0.1:8001/docs)

## Project run command

    1. Navigate to the project directory:
    `bash
        cd /path/to/your/project
        `

    2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    3. Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload --port 8001
    ```

    The application will now be accessible at `http://127.0.0.1:8001`.

## Technologies Used

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL

## Project Structure

```plaintext
my_project/
  ├── app/
      ├── __init__.py
      ├── main.py
      ├── models.py
      ├── schemas.py
      ├── crud.py
      ├── db.py
  ├── requirements.txt
  ├── Dockerfile
  ├── README.md
```

### Alternative Documentation (ReDoc):

FastAPI also provides an alternative documentation interface called ReDoc. You can access it at:

- [ReDoc Documentation](http://127.0.0.1:8001/redoc)

ReDoc provides a different style of documentation and might be preferable for some users.
