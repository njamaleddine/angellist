
class APIObject(object):
    """ Instantiate an api object instance """
    def __init__(self, **kwargs):
        self.json = kwargs

        for key, value in kwargs.items():
            if isinstance(value, list):
                setattr(self, key, [i for i in value])
            else:
                setattr(self, key, value)


class Accreditation(APIObject):
    pass


class Comment(APIObject):
    pass


class Follow(APIObject):
    pass


class Intro(APIObject):
    pass


class Job(APIObject):
    pass


class Like(APIObject):
    pass


class Message(APIObject):
    pass


class Path(APIObject):
    pass


class Press(APIObject):
    pass


class Review(APIObject):
    pass


class Search(APIObject):
    pass


class Startup(APIObject):
    def __init__(self, **kwargs):
        self._comments = []
        return super(Startup, self).__init__(**kwargs)

    @property
    def comments(self):
        if self._comments == []:
            return self.get_comments()
        return self._comments


class StartupRole(APIObject):
    pass


class StatusUpdate(APIObject):
    pass


class Tag(APIObject):
    TYPES = (
        ('LocationTag', 'LocationTag')
        ('RoleTag', 'RoleTag')
        ('SkillTag', 'SkillTag')
        ('MarketTag', 'MarketTag')
    )

    def __init__(self, **kwargs):
        self.tag_type = self.TYPES[kwargs.pop('tag_type')]
        return super(Startup, self).__init__(**kwargs)


class User(APIObject):
    pass
