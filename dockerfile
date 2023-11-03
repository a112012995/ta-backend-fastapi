# Use the official Python image as the base image
FROM python:3.11

# Set the working directory within the container
WORKDIR /app

# Copy the Poetry dependencies file and install the application dependencies
COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the FastAPI application code into the container
COPY . /app/

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Install Alembic and create an Alembic configuration file
RUN pip install --no-cache-dir alembic
COPY alembic.ini /app/alembic.ini

# Run Alembic migrations
RUN alembic upgrade heads

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
