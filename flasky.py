import os
import click
from app import create_app, db
from app.models import User, Role, Permission, Post, Follow, Comment
from flask_migrate import Migrate

# config
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role, Permission=Permission, Post=Post, Comment=Comment)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().discover(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
