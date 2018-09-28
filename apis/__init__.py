from flask_restplus import Api

from .push import api as push

api = Api(
    title='My GitHub Spoky',
    version='1.0',
    description='Catch GitHub event and do something',
    # All API metadatas
)

api.add_namespace(push)