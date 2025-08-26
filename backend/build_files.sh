# Update pip
echo "Updating pip..."
python3 -m pip install -U pip

# Install project dependencies
echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt
python3 -m pip install psycopg2-binary # PostgreSQL
python3 -m pip install djangorestframework
python3 -m pip install django-cors-headers

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed!"