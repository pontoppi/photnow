photnow is a simple command line tool to quickly obtain aperture photometry of a source in a fits image. It was developed to work with JWST data, but may work with other observatories. 

The tool will centroid on the source in a window limited by the aperture parameter, and then use photutils to generate a curve of growth out to the aperture. The background is subtracted from an annulus outside of aperture. 

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
photnow file x y [aperture] 
   
example:

photnow image.fits 100 200 12 

