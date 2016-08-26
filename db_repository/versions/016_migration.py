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

links = Table('links', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('pid', Integer),
    Column('url', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['links'].columns['name'].drop()
    pre_meta.tables['links'].columns['project_id'].drop()
    post_meta.tables['links'].columns['pid'].create()
    post_meta.tables['links'].columns['url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['links'].columns['name'].create()
    pre_meta.tables['links'].columns['project_id'].create()
    post_meta.tables['links'].columns['pid'].drop()
    post_meta.tables['links'].columns['url'].drop()
