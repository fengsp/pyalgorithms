"""
PyAlgorithms
------------

Links
`````

* `documentation <https://github.com/fengsp/pyalgorithms>`_
* `development version
  <http://github.com/fengsp/pyalgorithms/zipball/master#egg=pyalgorithms-dev>`_

"""
from setuptools import setup


setup(
    name='pyalgorithms',
    version='0.1',
    url='https://github.com/fengsp/pyalgorithms',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='Algorithms in Python',
    long_description=__doc__,
    packages=['pyalgorithms'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
