from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
toDo = Table('toDo', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String(length=500), nullable=False),
    Column('label', String(length=50)),
    Column('project', String(length=50)),
    Column('priority', String(length=50)),
    Column('state', String(length=10), nullable=False),
    Column('opened_at', String(length=200), nullable=False),
    Column('resolved_at', String(length=200)),
    Column('uid', Integer),
)

projects = Table('projects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('uid', Integer),
    Column('name', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['toDo'].columns['uid'].create()
    post_meta.tables['projects'].columns['uid'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['toDo'].columns['uid'].drop()
    post_meta.tables['projects'].columns['uid'].drop()
