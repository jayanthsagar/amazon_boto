"""
setup.py
~~~~~~~~
:copyright: (c) 2014.
:license: MIT License.
"""
from setuptools import setup
requires = ['tornado',
	'requests',
	'pymongo',
	'netaddr',
	'sh'
]
setup(
	name='AMAZON VM installation',
	version='0.1',
	url='https://github.com/jayanthsagar/amazon_boto',
	license='MIT',
	author='VLEAD',
	author_email='engg@virtual-labs.ac.in',
	description='Automated instance creation on amazon cloud',
	long_description=__doc__,
#packages=['src', 'config', 'scripts'],
	packages=['src'],
	zip_safe=False,
	platforms='any',
	install_requires=requires,
	include_package_data=True,
	classifiers=[
		'Development Status :: 0.1 - Alpha',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet',
		'Topic :: WWW/HTTP :: Automated:: VMCreation :: Cloud :: Hosting',
		]
)