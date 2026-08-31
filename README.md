# FastAPI Calculator

A simple REST API calculator built with FastAPI to learn backend development concepts and API design.

## Features

Currently, the API supports:

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling
- Invalid operation handling
- Input validation using Pydantic
- HTTP error responses using FastAPI's `HTTPException`

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

### Example Request

```python
{
  "a": 10,
  "b": 5,
  "operation": "+"
}
```

### Example Response

```python
{
  "result": 15
}
```

## What I Learnt 

Through building this project, I practiced:

- Creating API endpoints with FastAPI
- Understanding GET and POST requests
- Using Pydantic models for request validation
- Working with JSON data
- Returning API responses
- Handling errors using HTTPException
- Using HTTP status codes
- Setting up a local API server with Uvicorn

## Future Improvements 

This project is still in development. Planned improvements include:

- Adding more calculator operations
- Improving input validation
- Adding automated tests
- Organising the project into multiple files
- Improving API documentation
- Adding additional error handling
- Exploring more advanced FastAPI features
