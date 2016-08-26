from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
links = Table('links', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('uid', Integer),
    Column('project_id', Integer),
)

projects = Table('projects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('uid', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['links'].create()
    post_meta.tables['projects'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['links'].drop()
    post_meta.tables['projects'].drop()
