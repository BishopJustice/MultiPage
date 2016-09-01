from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
roles = Table('roles', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('description', String),
)

roles_users = Table('roles_users', post_meta,
    Column('user_id', Integer),
    Column('role_id', Integer),
)

users = Table('users', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('firstname', VARCHAR(length=100)),
    Column('lastname', VARCHAR(length=100)),
    Column('email', VARCHAR(length=120)),
    Column('pwdhash', VARCHAR(length=100)),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String),
    Column('name', String(length=100)),
    Column('password', String),
    Column('active', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['roles'].create()
    post_meta.tables['roles_users'].create()
    pre_meta.tables['users'].columns['firstname'].drop()
    pre_meta.tables['users'].columns['lastname'].drop()
    pre_meta.tables['users'].columns['pwdhash'].drop()
    pre_meta.tables['users'].columns['uid'].drop()
    post_meta.tables['users'].columns['active'].create()
    post_meta.tables['users'].columns['id'].create()
    post_meta.tables['users'].columns['name'].create()
    post_meta.tables['users'].columns['password'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['roles'].drop()
    post_meta.tables['roles_users'].drop()
    pre_meta.tables['users'].columns['firstname'].create()
    pre_meta.tables['users'].columns['lastname'].create()
    pre_meta.tables['users'].columns['pwdhash'].create()
    pre_meta.tables['users'].columns['uid'].create()
    post_meta.tables['users'].columns['active'].drop()
    post_meta.tables['users'].columns['id'].drop()
    post_meta.tables['users'].columns['name'].drop()
    post_meta.tables['users'].columns['password'].drop()
