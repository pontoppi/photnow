webbcrawl is a a simple command-line tool to recursively list the contents of a JWST data directory, usually as downloaded from the Mikulski Archive for Space Telescopes (MAST)

This software is provided as-is, with no warranty.

  
INSTALLATION

using setup.py:
----------
python setup.py install

Using pip:
----------
To be uploaded to pypi

Basic command line usage:
------------------------
webbcrawl --options path 
   
example:

webbcrawl --include_path MAST_2022-02-08T0000 
# spew
