import alembic.config


def migrate_up():
    alembicArgs = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)


def migrate_down():
    alembicArgs2 = [
        '--raiseerr',
        'downgrade', 'base',
    ]
    alembic.config.main(argv=alembicArgs2)
