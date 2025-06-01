# Import Libraries
import database as _database

# Define Create Database Service
def create_database():
    """
    Create the database "database" and tables if they do not exist
    """
    _database.Base.metadata.create_all(bind=_database.engine)
    print("Database and tables created successfully.")