# Django Smart Fixture

- Download
```sh
curl -s https://raw.githubusercontent.com/cuongnb14/django-smart-fixture/master/download.sh | bash -s 
```

- requirements
```
django-dynamic-fixture==3.1.1
faker==8.1.0
```

- Setting

```
DDF_DEFAULT_DATA_FIXTURE = 'smart_fixture.fixtures.CustomFixture'
```

- Update fixure in init_test_data command

- Load test data

```sh
python3 manage.py init_test_data
```