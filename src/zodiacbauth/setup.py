import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',  
    'pyramid_chameleon',  
    'pyramid_mako', 
    'pyramid_debugtoolbar',
    'waitress',
    ]

setup(name='zodiacbauth',
      version='0.0',
      description='zodiacbauth',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="zodiacbauth",
      entry_points="""\
      [paste.app_factory]
      main = zodiacbauth:main
      """,
      )
