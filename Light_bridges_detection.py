#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import sunpy.map as smap
from skimage import measure

image_ = smap.Map("/home/bryan_alfonso/light_bridges/FITS/hmi.ic_45s.2010.12.07_12-00-00_TAI.continuum.fits")
image = image_.rotate()
image.plot()
plt.show()

hdu = fits.open("/home/bryan_alfonso/light_bridges/FITS/hmi.ic_45s.2010.12.07_12-00-00_TAI.continuum.fits", ckecksum = True)
data = hdu[0].data
hdr = hdu[0].header
data[np.isnan(data)] = 0
angle_rot = hdr["crota2"]
print angle_rot

img = scipy.ndimage.interpolation.rotate(data, angle_rot, mode="nearest", order=2, prefilter=False)
plt.imshow(data,origin="lower",cmap="gray")
plt.colorbar()
plt.show()

plt.imshow(img,origin="lower",cmap="gray")
plt.colorbar()
plt.show()

zoom = data[980:1110,2270:2410]
plt.imshow(zoom, origin="lower", cmap="gray")
plt.colorbar()
plt.show()

#contours = measure.find_contours(zoom, 49500)
#plt.imshow(zoom,origin="lower",cmap="gray")
#for n, contour in enumerate(contours):
#    plt.plot(contour[:, 1]*(0.504), contour[:, 0]*(0.504),"k", linewidth=1,linestyle="-",scaley = False,scalex=False)
#plt.show()

cs = plt.contour(zoom,levels=[49500],ls = "solid")
plt.imshow(zoom, origin="lower", cmap="gray")
plt.colorbar()
plt.show()

cs1 = cs.collections
print (cs1[0])
p = cs.collections[0].get_paths()[0]
v = p.vertices
print (v)

def PolyArea(x,y):
	return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

x = v[:,0]
y = v[:,1]

a = PolyArea(y,x)
print (a)



