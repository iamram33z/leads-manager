# Import Libraries
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "sqlite:///./database.db"

# Create a SQLAlchemy engine
engine = _sql.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = _declarative.declarative_base()