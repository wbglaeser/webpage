from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'pyramid_chameleon',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'psycopg2',
    'bcrypt',
]

setup(name='workpage',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = workpage:main
      [console_scripts]
      initialize_workpage_db = workpage.initialize_db:main
      """,
)
