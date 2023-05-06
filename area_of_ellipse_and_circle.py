import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Point
from shapely.affinity import scale, rotate


# this fucntion returns generated ellipse. Circle is also type of Ellipse.
def ellipse_generator(center, axes, inclination):
    _ellipse = scale(Point(*center).buffer(1), *axes)
    _ellipse = rotate(_ellipse, inclination)
    return _ellipse

# variables
_radius_r = 2.8; _vertex_a = 3.78; _covertex_b = 2; _xcenter_h = 0; _ycenter_k = 2.22

# the following fucntions will generate the ellipses for you.
CIRCLE = ellipse_generator((_xcenter_h, _ycenter_k), (_radius_r, _radius_r), 0) # circle equation = (x - xc)**2 + (y - yc)**2 - r**2
ELLIPSE = ellipse_generator((0, 0), (_vertex_a, _covertex_b), 0) 

"""
IMPORTANT

actual ellipse equation = ((x-h)/a)**2 + ((y-k)/b)**2 - 1

In that case modify the line '18' to ELLIPSE = ellipse_generator((h, k), (_vertex_a, _covertex_b), 0) 

If you want to rotate the ellipse to any direction then modify the same to ELLIPSE = ellipse_generator((h, k), (_vertex_a, _covertex_b), <input_value>) 

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
plt.figure()
_ax = plt.gca()
[_ax.add_artist(item) for item in _polys]
_ax.set_xlim(-7, 7)
_ax.set_ylim(0, 10)
plt.show()

