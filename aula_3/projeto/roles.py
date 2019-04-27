
import schema
import db

class Role(schema.Schema):

    def __init__(self, name):
        self.name