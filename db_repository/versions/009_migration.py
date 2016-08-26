from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
links = Table('links', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('project_id', INTEGER),
)

toDo = Table('toDo', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('description', VARCHAR(length=500), nullable=False),
    Column('label', VARCHAR(length=50)),
    Column('project', VARCHAR(length=50)),
    Column('priority', VARCHAR(length=50)),
    Column('state', VARCHAR(length=10), nullable=False),
    Column('opened_at', VARCHAR(length=200), nullable=False),
    Column('resolved_at', VARCHAR(length=200)),
    Column('uid', INTEGER),
)

items = Table('items', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('projectid', Integer),
    Column('description', String(length=500), nullable=False),
    Column('label', String(length=50)),
    Column('project', String(length=50)),
    Column('priority', String(length=50)),
    Column('state', String(length=10), nullable=False),
    Column('opened_at', String(length=200), nullable=False),
    Column('resolved_at', String(length=200)),
    Column('uid', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['links'].drop()
    pre_meta.tables['toDo'].drop()
    post_meta.tables['items'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['links'].create()
    pre_meta.tables['toDo'].create()
    post_meta.tables['items'].drop()
