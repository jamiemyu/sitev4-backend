# Update pip
echo "Updating pip..."
python3 -m pip install -U pip

# Install project dependencies
echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed!"