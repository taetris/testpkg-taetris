from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='testpkg-taetris',
   version='1.0',
   description='Test package for Python',
   license="MIT",
   long_description=long_description,
   author='Tripti S.',
   author_email='triptis1235@gmail.com',
   packages=['testpkg-taetris'],  #same as name
   install_requires=[], #external packages as dependencies
   scripts=[
            
           ]
)