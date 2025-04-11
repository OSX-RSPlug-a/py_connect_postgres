# py_connect_postgres

Setup the stack.

# Script to create the SSL key:

        chmod +x ./setup_bash.sh

        ./setup_bash.sh

# Setup the env for python code

        python3 -m venv env

        source env/bin/activate

        pip3 install -m requirements.txt
        
        python3 app.py

# Access the bash docker Postgres image

        docker exec -it postgres sh

# Verify the data created in the DB

        \dt