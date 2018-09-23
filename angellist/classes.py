class Resource(object):
    """ An AngelList API Resource """
    def __init__(self, **kwargs):
        self.json = kwargs

        for key, value in kwargs.items():
            if isinstance(value, list):
                setattr(self, key, [i for i in value])
            else:
                setattr(self, key, value)

    def __repr__(self):
        return '<{class_name} {resource_id}>'.format(
            class_name=self.__class__.name,
            resource_id=self.id
        )


class Accreditation(Resource):
    pass


class Comment(Resource):
    pass


class Follow(Resource):
    pass


class Intro(Resource):
    pass


class Job(Resource):
    pass


class Like(Resource):
    pass


class Message(Resource):
    pass


class Path(Resource):
    pass


class Press(Resource):
    pass


class Review(Resource):
    pass


class Search(Resource):
    pass


class Startup(Resource):
    def __init__(self, **kwargs):
        self._comments = []
        return super(Startup, self).__init__(**kwargs)

    @property
    def comments(self):
        if self._comments == []:
            return self.get_comments()
        return self._comments


class StartupRole(Resource):
    pass


class StatusUpdate(Resource):
    pass


class Tag(Resource):
    TYPES = (
        ('LocationTag', 'LocationTag'),
        ('RoleTag', 'RoleTag'),
        ('SkillTag', 'SkillTag'),
        ('MarketTag', 'MarketTag'),
    )

    def __init__(self, **kwargs):
        self.tag_type = self.TYPES[kwargs.pop('tag_type')]
        return super(Startup, self).__init__(**kwargs)


class User(Resource):
    pass
