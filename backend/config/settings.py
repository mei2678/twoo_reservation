import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'g8oapcr9_25*b-7q5**od-6w0+l(8_+6e4!*1v8q4bif*tb-k)'
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'auth_management.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.line.LineOAuth2', # LINE認証用
    'django.contrib.auth.backends.ModelBackend'
]

LOGIN_REDIRECT_URL = "/account_management/complete/line"
LOGOUT_REDIRECT_URL = "/account_management/complete/line"
SOCIAL_AUTH_LINE_KEY = os.environ.get('SOCIAL_AUTH_LINE_KEY')
SOCIAL_AUTH_LINE_SECRET = os.environ.get('SOCIAL_AUTH_LINE_SECRET')

SOCIAL_AUTH_PIPELINE = (
  "social_core.pipeline.social_auth.social_details",
  "social_core.pipeline.social_auth.social_uid",
  "social_core.pipeline.social_auth.social_user",
  "social_core.pipeline.user.get_username",
  "social_core.pipeline.social_auth.associate_by_email",
  "social_core.pipeline.user.create_user",
  "social_core.pipeline.social_auth.associate_user",
  "social_core.pipeline.social_auth.load_extra_data",
  "social_core.pipeline.user.user_details",
  "auth_management.pipeline.set_user_data",
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'menu_management',
    'auth_management',
    'booking_management',
    'slot_management',
    'social_django',
    'account_management',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_ROOT_USER'),
        'PASSWORD': os.environ.get('MYSQL_ROOT_PASSWORD'),
        'HOST': 'db',
        'PORT': '3306'
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
