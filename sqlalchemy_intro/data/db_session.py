import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase

factory = None

def global_init():
    global factory

    if factory:
        return

    conn_str = 'postgresql+psycopg2://postgres:root@localhost:54321/sqlalchemy'

    engine = sa.create_engine(conn_str, echo=False)
    factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import sqlalchemy_intro.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)