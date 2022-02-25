from setuptools import setup

setup(name='photnow',
      version=1.0,
      description='Quick photometry from the command line',
      author='Klaus Pontoppidan (STScI)',
      author_email='pontoppi@stsci.edu',
      url='http://jwst.stsci.edu/',
      download_url = '',
      packages=['photnow'],
      install_requires=['docopt>=0.6.2','astropy>=3.0.0','photutils>=1.0.0'],
      entry_points = {'console_scripts': ['photnow=photnow.cli:main']}
      )
