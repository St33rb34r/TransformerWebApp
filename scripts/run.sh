#!/bin/zsh

echo "Starting web application locally. "
uvicorn app.main:app --port 8000 --reload
