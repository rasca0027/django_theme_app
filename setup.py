import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


REQUIREMENTS = [
    'Django==1.8.4',
    'Jinja2==2.7.3',
    'MarkupSafe==0.23',
    'Pillow==2.9.0',
    'Pygments==2.0.2',
    'Unipath==1.0',
    'django-appconf==1.0.1',
    'django-bootstrap3-sass==3.3.2.2',
    'django-braces==1.4.0',
    'django-classy-tags==0.6.2',
    'django-compressor==1.5',
    'django-crispy-forms==1.5.0',
    'django-direct-render==0.1.2',
    'django-gmapify==0.1',
    'django-kss-styleguide==0.5.9',
    'django-libsass==0.2',
    'django-responsive-viewer==0.1.1',
    'libsass==0.8.3',
    'logutils==0.3.3',
    'six==1.9.0',
    'sqlparse==0.1.14',
    'wsgiref==0.1.2',
    'fabric'
]

setup(
    name='django_theme',
    version='0.1',
    description='Django theme app',
    author='rasca0027',
    author_email='rasca0027@gmail.com',
    long_description=README,
    scripts=[],
    url='https://github.com/rasca027/django_theme_app',
    packages=find_packages(),
    license='MIT',
    platforms='Posix; MacOS X;',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
