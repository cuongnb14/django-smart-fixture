from .algorithms.smart import SmartFixture
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomFixture(SmartFixture):

    def charfield_custom(self, field, key):
        if field.model == User:
            if field.name == "company":
                return fake.company()
        
        return None