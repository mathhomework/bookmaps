# You need to use a requirements.txt and .gitignore file, lots of files that shouldn't be checked in to your repo (.pyc files)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookmaps',
        'USER': 'postgres',
        'PASSWORD': 'hotdog'
    }
}
