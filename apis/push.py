from flask_restplus import Namespace, Resource, fields

api = Namespace('push', description='Handle a push on github')

#cat = api.model('Cat', {
#    'id': fields.String(required=True, description='The cat identifier'),
#    'name': fields.String(required=True, description='The cat name'),
#})

#CATS = [
#    {'id': 'felix', 'name': 'Felix'},
#]


@api.route('/')
class Push(Resource):
    
    @api.doc('post_push')
    def post(self):
        """Fetch a push"""
        return {"message": "Everything is OK"}, 200