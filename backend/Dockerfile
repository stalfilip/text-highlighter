# Start from a Python 3.10 base image that is compatible with Poetry
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock file and pyproject.toml file
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install poetry

# Avoid creating .venv directories inside project directory
RUN poetry config virtualenvs.create false

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the codebase into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application using Poetry
CMD ["poetry", "run", "python", "api/main.py"]
