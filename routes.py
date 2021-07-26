def urls(api):
    from resources.Health import HealthResource
    from resources.UserResource import SingleUserResource
    from resources.PostResource import SinglePostResource
    api.add_resource(HealthResource, '/')
    api.add_resource(SingleUserResource, '/user/<int:id>', '/user')
    api.add_resource(SinglePostResource, '/post/<int:id>', '/post')
