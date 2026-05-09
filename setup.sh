#!/usr/bin/env bash
set -e

PYTHON=${PYTHON:-python3}

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON -m venv .venv
fi

echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip -q
.venv/bin/pip install -r requirements.txt

echo ""
echo "Done. Activate with:    source .venv/bin/activate"
echo "Run tests with:         .venv/bin/python -m unittest discover -s test -p '*_test.py' -v"
echo "Launch notebook with:   .venv/bin/jupyter notebook python_learning_py3.ipynb"
