# Text Highlighter

## Description

This project is a Flask web server that accepts POST requests to the "/ingest" endpoint. It processes the text in the request with the `run_highlighting` function and returns the the text with key sentences highlighted

## Setup

Follow these steps to set up the project:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run `poetry install` to install the project dependencies.
4. Copy the example environment file with `cp .env.example .env`.
5. Open the `.env` file and fill out the necessary environment variables.
6. Run the server with `poetry run python api/main.py`.

## Usage

Once the server is running, you can send POST requests to the "/ingest" endpoint with a JSON body containing a "text" field. The server will process the text and return the result.

## Linting 
To run `ruff`, use the command `poetry run ruff`. This command runs `ruff` in the virtual environment managed by Poetry, ensuring that it has access to the correct Python interpreter and dependencies.

## Type Checking

This project uses `pyright` for static type checking. `pyright` is a fast type checker meant for large Python source bases. It can run in a “watch” mode and performs fast incremental updates when files are modified.

'poetry run pyright' to chech typechecks


## Tests
To run the tests, use the command `poetry run pytest`. This command runs `pytest` in the virtual environment managed by Poetry, ensuring that it has access to the correct Python interpreter and dependencies.


