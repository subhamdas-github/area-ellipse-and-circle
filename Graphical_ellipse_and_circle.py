import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Point
from shapely.affinity import scale, rotate
import numpy

# this fucntion returns generated ellipse. Circle is also type of Ellipse.
def ellipse_generator(center, axes, inclination):
    _ellipse = scale(Point(*center).buffer(1), *axes)
    _ellipse = rotate(_ellipse, inclination)
    return _ellipse

# variables
_circle_radius = 1.78; _ellipse_vertex = 3.19; _ellipse_co_vertex = 2; _circle_centerX = 0; _circle_centerY = 2.22; _ellipse_centerX =3; _ellipse_centerY = 2
_offset = 5

# the following fucntions will generate the ellipses for you.
CIRCLE = ellipse_generator((_circle_centerX, _circle_centerY), (_circle_radius, _circle_radius), 0) # circle equation = (x - xc)**2 + (y - yc)**2 - r**2
ELLIPSE = ellipse_generator((_ellipse_centerX, _ellipse_centerY), (_ellipse_vertex, _ellipse_co_vertex), 0) 

"""
IMPORTANT
==========
If you want to rotate the ellipse to any direction then modify line 19 to 
ELLIPSE = ellipse_generator((_ellipse_centerX, _ellipse_centerY), (_ellipse_vertex, _ellipse_co_vertex), <your-input>)
"""

# Patch the polygons and inner intersection
_e1 = PolygonPatch(CIRCLE, facecolor='#99ccff', edgecolor='black', linewidth=1)
_e2 = PolygonPatch(ELLIPSE, facecolor='#33cc33', edgecolor='black', linewidth=1)
_polys = [_e1, _e2]
if CIRCLE.intersects(ELLIPSE):
    _intersect = CIRCLE.intersection(ELLIPSE)
    inter = PolygonPatch(_intersect, facecolor='#cc0066',edgecolor='black', linewidth=1, hatch='///')
    _polys.append(inter)

# Plotting
_ax=plt.gca()
[_ax.add_artist(item) for item in _polys]
_max = numpy.max(numpy.array([_circle_radius, _circle_centerX, _circle_centerY, _ellipse_centerX, _ellipse_centerY, _ellipse_co_vertex, _ellipse_vertex]))
_ax.set_xlim(-_max, _max*2+_offset)
_ax.set_ylim(-_max, _max*2+_offset)
_ax.set_aspect('equal', adjustable='box')
plt.title('Your content here', fontsize=15, color='green', fontstyle='italic')
plt.show()
