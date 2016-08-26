from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('firstname', VARCHAR(length=100)),
    Column('lastname', VARCHAR(length=100)),
    Column('email', VARCHAR(length=120)),
    Column('pwdhash', VARCHAR(length=54)),
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

links = Table('links', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('uid', INTEGER),
    Column('project_id', INTEGER),
)

projects = Table('projects', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('uid', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].drop()
    pre_meta.tables['toDo'].columns['uid'].drop()
    pre_meta.tables['links'].columns['uid'].drop()
    pre_meta.tables['projects'].columns['uid'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].create()
    pre_meta.tables['toDo'].columns['uid'].create()
    pre_meta.tables['links'].columns['uid'].create()
    pre_meta.tables['projects'].columns['uid'].create()
