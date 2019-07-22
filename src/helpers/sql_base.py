"""Base for DB connections"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ENGINE = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
SESSION = sessionmaker(bind=ENGINE)

BASE = declarative_base()
