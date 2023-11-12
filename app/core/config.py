import os
import dotenv


dotenv.load_dotenv(".env")
conn_dict = {
    "host": os.environ.get("MYSQL_HOST"),
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "port": int(os.environ.get("MYSQL_PORT")),
    "database": os.environ.get("MYSQL_DATABASE"),
}
