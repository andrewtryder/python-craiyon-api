from setuptools import setup

setup(
    name='craiyonapi',
    version='0.1.1',
    description='Python wrapper for the Craiyon API',
    author='Andrew Ryder',
    author_email='andrewtryder@gmail.com',
    url='https://github.com/andrewtryder/python-craiyon-api',
    packages=['craiyonapi'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
