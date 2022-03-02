photnow is a simple command line tool to quickly obtain aperture photometry of a source in a fits image. It was developed to work with JWST data, but may work with other observatories. 

The tool will centroid on the source in a window limited by the aperture radius parameter, and then use photutils to generate a curve of growth out to the aperture. The background is subtracted from an annulus outside of aperture. 

This software is provided as-is, with no warranty.

  
INSTALLATION

using setup.py:
---------------
python setup.py install

Using pip:
----------
To be uploaded to pypi

Basic command line usage:
------------------------
photnow file x y [--radius aperture] 
   
examples:
---------

photnow --help
photnow image.fits 100 200
photnow image.fits 100 200 --radius 10 

![Example output](https://user-images.githubusercontent.com/3697922/156459947-f69f36b0-89df-4ef0-a83c-62c80cdb3f77.png)
