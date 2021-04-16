import time

from django.contrib.auth.hashers import make_password
from django_dynamic_fixture.fixture_algorithms import RandomDataFixture
from faker import Faker

fake = Faker()


class SmartFixture(RandomDataFixture):
    def charfield_config(self, field, key):
        result = self.charfield_custom(field, key)
        if result:
            return result

        field_name = field.name
        if "password" in field_name:
            return make_password("123456")

        if "username" in field_name:
            return f"{int(time.time())}-{fake.user_name()}"

        if "phone" in field_name:
            return fake.phone_number()

        if "address" in field_name:
            return fake.address()

        if "name" in field_name:
            return fake.name()
        
        if "url" in field_name:
            return fake.url()

        if "description" in field_name:
            return fake.text().replace("\n", "")

        return " ".join(fake.words(3))
    
    def charfield_custom(self, field, key):
        pass

    def imagefield_config(self, field, key):
        return fake.image_url(400, 400)
