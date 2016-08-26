from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
items = Table('items', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('projectid', INTEGER),
    Column('description', VARCHAR(length=500), nullable=False),
    Column('label', VARCHAR(length=50)),
    Column('project', VARCHAR(length=50)),
    Column('priority', VARCHAR(length=50)),
    Column('state', VARCHAR(length=10), nullable=False),
    Column('opened_at', VARCHAR(length=200), nullable=False),
    Column('resolved_at', VARCHAR(length=200)),
    Column('uid', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['items'].columns['project'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['items'].columns['project'].create()
