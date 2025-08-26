# Update pip
echo "Updating pip..."
python3 -m pip install -U pip

# Install project dependencies
echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed!"