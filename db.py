import os

import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/complaint_system"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
