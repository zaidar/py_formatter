import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'\\src'

SECRET_KEY = 'y&$dgfs3eiz#w@3-)sd3lp_2ao^'

DEBUG = False

ALLOWED_HOSTS = ['django-env.eba-wmzdu4xz.us-west-2.elasticbeanstalk.com']



INSTALLED_APPS = [
    'rest_framework',
    'src.apps.profiler',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
REST_FRAMEWORK = {
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework_xml.parsers.XMLParser',
    # ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework_xml.renderers.XMLRenderer',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['src/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'static/db.sqlite3'),
    }
}
# DATABASES = {
# 		'default': {
# 			'ENGINE': 'django.db.backends.mysql',
# 			'NAME': 'test_py_formatter',
# 			'USER': 'root',
# 			'PASSWORD': 'aa18aa01',
# 			'HOST': '127.0.0.1',
# 			'PORT': '3606'
# 		}
# 	}
#


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR,"static/static_cdn")
MEDIA_ROOT = os.path.join(BASE_DIR,"static/media_cdn")
LOGIN_REDIRECT_URL = '/'
