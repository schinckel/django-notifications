from distutils.core import setup
from notifications import __version__

setup(name='django-notifications',
      version=__version__,
      description='Generic notifications  app for Django.',
      long_description=open('README.rst').read(),
      author='Matthew Schinckel',
      author_email='matt@schinckel.net',
      url='http://github.com/schinckel/django-notifications',
      install_requires=[
          'django',
          'django-model-utils>=1.1.0',
          'pytz',
          'django-jsonfield>=0.9.3',
      ],
      packages=['notifications',
                'notifications.templatetags'],
      package_data={'notifications': [
                                 'templates/notifications/*.html']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
