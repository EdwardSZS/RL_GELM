#!/bin/bash

# Exit on error
set -e

# Check and install pip version 22.3 if not already installed
pip_version=$(pip --version | awk '{print $2}' | cut -d '.' -f 1-2)
if [[ "$pip_version" != "22.3" ]]; then
    echo "Upgrading pip to version 22.3..."
    pip install --upgrade pip==22.3
else
    echo "pip is already at version 22.3."
fi

# Install Python dependencies
pip install -r requirements.txt

# Other setup commands can go here, e.g.:
# python -m spacy download en_core_web_sm

# Any environment variable setup
# export SOME_ENV_VAR=value

echo "Setup complete!"
