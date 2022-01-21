import psycopg2
import os

connection = None
try:
    connection = psycopg2.connect(
        "user='{}' host='{}' password='{}' port='5432'".format(
            os.environ.get("POSTGRES_USER"),
            os.environ.get("POSTGRES_DB"),
            os.environ.get("POSTGRES_PASSWORD"),
        )
    )
    print(
        "Connecting to postgres database to check if postal codes table already exists."
    )

except:
    print("Couldn't connect to postgres. Something went wrong.")

if connection is not None:
    connection.autocommit = True

    cur = connection.cursor()
    table_name = "django_postalcodes_mexico_postalcode"
    # Check if database already exist
    cur.execute(
        "SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='" + table_name + "')"
    )
    # This return (True,) or (False,)
    database_exist = cur.fetchone()[0]
    # The database doesn't exist, therefore we should run migrations and obtain postal codes
    if not database_exist:
        print("Postal codes database don't exist, running migrations.")
        os.system("python manage.py migrate")
        os.system("python manage.py importpostalcodesmx")
    connection.close()
    print("Verification ended. Closing postgres connection.")
    print("Initializing server...")
    os.system("python manage.py runserver 0.0.0.0:8000")
