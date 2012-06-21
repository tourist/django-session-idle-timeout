from setuptools import setup, find_packages

setup(
    name = "django-session-idle-timeout",
    install_requires = [
        'django',
    ],
    packages = find_packages('.'),
    package_dir = {'':'.'},
    version = "1.0.1",
    description = "Timeout a logged user after a period of time",
    long_description=open('README.md').read(-1),
    author = "Tomas Zulberti",
    zip_safe = False,
    author_email = "tzulberti@gmail.com",
    url = "http://github.com/tzulberti/django-request-provider",
    keywords = [
        "django contrib",
        "session login expiration"
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Environment :: Web Environment',
        'Operating System :: OS Independent'
        ],
    license = 'License :: OSI Approved :: BSD License',
)
