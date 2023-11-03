#! /usr/bin/env bash

# Let the DB start
python3 /app/pre_start.py

# Run migrations
alembic upgrade heads

# Create initial data in DB
python3 /app/initial_data.py