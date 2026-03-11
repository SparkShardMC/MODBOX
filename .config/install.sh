#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing Python 3 and pip..."
sudo apt install -y python3 python3-pip python3-venv

echo "Installing MySQL client and server..."
sudo apt install -y mysql-client mysql-server

echo "Creating Python virtual environment..."
python3 -m venv modbox_env
source modbox_env/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "MODBOX environment setup complete!"
