# Import Libraries
import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database

# Class for User Model
class User(_database.Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    username = _sql.Column(_sql.String, unique=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    leads = _orm.relationship("Lead", back_populates="owner")

    def verify_password(self, password: str) -> bool:
        return _hash.bcrypt.verify(password, self.hashed_password)

# Class for Lead Model
class Lead(_database.Base):
    __tablename__ = "leads"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True)
    company = _sql.Column(_sql.String, index=True, default="")
    note= _sql.Column(_sql.String, default="")
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="leads")