#!/usr/bin/python3
''' module for BaseModel class '''
from datetime import datetime
import uuid
import models


class BaseModel:
    ''' BaseModel class '''
    def __init__(self, *args, **kwargs):
        '''
        initation of basemodel

        Args:
        *args: arguments passed in
        **kwargs: arguments with key values

        Return:
        None
        '''
        if len(kwargs):
            for key in kwargs:
                value = kwargs[key]
                if key != "__class__":
                    self.__setattr__(key, value)
                if key in ["created_at", "updated_at"]:
                    self.__setattr__(key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        Return:
        string represntation fo object
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' updates date for updated_at attribute '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' returns dictonary with all key values of instance '''
        mydict = {**self.__dict__}
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = datetime.isoformat(self.created_at)
        mydict['updated_at'] = datetime.isoformat(self.updated_at)

        return mydict
