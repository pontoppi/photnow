import os
import numpy as np
import matplotlib.pylab as plt
from matplotlib.patches import Circle

from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils import aperture as ap
from photutils import centroids

class photnow():

    '''
    Do simple aperture photometry of a single source, with a curve of growth.
    Documentation of the inputs in the cli.py command line interface definition.
    '''    
    def __init__(self,arguments):
            
        ffpath = arguments['<file>']
        xx = int(arguments['<x>'])
        yy = int(arguments['<y>'])
        nr = int(arguments['--radius'])
        aw = 2
        pos = (xx,yy)

        self.data = fits.getdata(ffpath)
        self.hdr = fits.getheader(ffpath,1)
        
        try:
            self.unit = self.hdr['BUNIT']
            cdelt1 = self.hdr['CDELT1']
            cdelt2 = self.hdr['CDELT2']
            self.px_area = cdelt1*cdelt2 * 3.0461741978670859934e-4 #square degree --> steradian
        except:
            print('Failed reading header, units are undefined')
            self.unit = 'Unknown unit'
            
        #If we have units of intensity, need to convert to integral over solid angle, and to Jy (if MJy/sr)
        if self.unit=='MJy/sr':
            breakpoint()
            self.scale_factor = 1e6 * self.px_area
            self.unit = 'Jy'
        else:
            self.scale_factor = 1.0
            
        radii, phot_vals = self.apphot(pos,nr,aw)
        self.plotphot(radii, phot_vals, nr, aw)
        
    def apphot(self,pos,nr,aw):
        
        phot_vals = np.zeros(nr)
        radii = np.linspace(1,nr,nr)

        self.cutout = self.data[pos[1]-2*nr:pos[1]+2*nr,pos[0]-2*nr:pos[0]+2*nr]
        mini_cut = self.cutout[nr:3*nr,nr:3*nr]
        self.vmax = np.max(mini_cut)
        self.vmin = np.min(self.cutout)

        self.cen = centroids.centroid_com(mini_cut)+np.array([nr,nr])

        annulus = ap.CircularAnnulus(self.cen, r_in=nr, r_out=nr+aw)
        annulus_mask = annulus.to_mask(method='center')
        annulus_data = annulus_mask.multiply(self.cutout)
        mask = annulus_mask.data    
        annulus_data_1d = annulus_data[mask > 0]
        mean, median, stddev = sigma_clipped_stats(annulus_data_1d)
 
        for ii,radius in enumerate(radii):
            aperture = ap.CircularAperture(self.cen,r=radii[ii])
            phot_table = ap.aperture_photometry(self.cutout, [aperture,annulus])   
            phot_val = phot_table['aperture_sum_0'][0] - phot_table['aperture_sum_1'][0]*aperture.area/annulus.area
            phot_vals[ii] = phot_val

        error = stddev*np.sqrt(aperture.area)    

        print('%9.3f +/- %9.3f' % (phot_vals[-1], error))
        
        return radii, phot_vals

    def plotphot(self, radii, phot_vals, nr, aw):

        fig = plt.figure(figsize=(6,3))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        ax1.imshow(self.cutout,cmap='cividis',extent=[-2*nr,2*nr,-2*nr,2*nr],vmin=self.vmin,vmax=self.vmax)
        ax1.set_xlabel('Pixels')
        ax1.set_ylabel('Pixels')

        ap_patch = Circle(self.cen-2*nr,nr, fill=False, color='white')
        an_patch = Circle(self.cen-2*nr,nr+aw, fill=False, color='yellow')
        ax1.add_patch(ap_patch)
        ax1.add_patch(an_patch)

        ax2.step(radii, phot_vals * self.scale_factor)
        ax2.set_xlabel('Pixels')
        ax2.set_ylabel(self.unit)

        plt.tight_layout()
        plt.show()
