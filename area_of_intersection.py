import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Point
from shapely.affinity import scale, rotate
import math
import scipy.integrate as integrate

_ellipse_co_vertex = float(input('Enter the value of the distance from workpiece to electrode tip for pulsed in mm: '))
b = float(input('Enter the vale of the distance from workpiece(base metal+pulsed) to electrode tip for CMT in mm: '))
d = float(input('Enter the value of the wire diameter in mm: '))
f1 = float(input('Enter the value of the feed rate in m/min: '))
f = (f1*1000)/60
v = float(input('Enter the value of the welding speed in mm/sec: '))
_circle_radius = (d/2)*(math.sqrt(f/v))
m = _ellipse_co_vertex+b-2*_circle_radius
_circle_centerY = _ellipse_co_vertex+b-_circle_radius
_ellipse_vertex = (d*d*f)/(2*v*_ellipse_co_vertex)
w = (_circle_centerY**2)+(_ellipse_vertex**2)-(_circle_radius**2)
s = (1-(_ellipse_vertex/_ellipse_co_vertex)**2)
dis = (-2*_circle_centerY)**2 -(4*s*w)
if dis>0:
    root1 = ((2*_circle_centerY) + math.sqrt(dis))/(2*s)
    root2 = ((2*_circle_centerY) - math.sqrt(dis))/(2*s)
elif dis==0:
    root1=root2= -((2*_circle_centerY)/(2*s))
elif dis<0:
    print('Points are imagiary, so no result can be obtained.')
if root1>0:
    p = root1
elif root2>0:
    p = root2
I1, error1 = integrate.quad(lambda y: 2*(math.sqrt(_circle_radius**2-(y-_circle_centerY)**2)),m,p)
I2, error2 = integrate.quad(lambda y: 2*((_ellipse_vertex*(math.sqrt(1-(y/_ellipse_co_vertex)**2)))),p,_ellipse_co_vertex)
A_p = I1+I2
print('The area of the penetration in mm2 due to pulsed and CMT is=', A_p)
A_t = (math.pi)*(_circle_radius**2)
j = (A_p/A_t)
percentage = f"{j:.2%}"
print('The penetration percentage is',percentage)


# this fucntion returns generated ellipse. Circle is also type of Ellipse.
def ellipse_generator(center, axes, inclination):
    _ellipse = scale(Point(*center).buffer(1), *axes)
    _ellipse = rotate(_ellipse, inclination)
    return _ellipse

# Constants
_circle_centerX = 0
_ellipse_centerX = 0
_ellipse_centerY = 0

# the following fucntions will generate the ellipses for you.
CIRCLE = ellipse_generator((_circle_centerX, _circle_centerY), (_circle_radius, _circle_radius), 0) # circle equation = (x - xc)**2 + (y - yc)**2 - _circle_radius**2
ELLIPSE = ellipse_generator((_ellipse_centerX, _ellipse_centerY), (_ellipse_vertex, _ellipse_co_vertex), 0) 


# Patch the polygons and inner intersection
_e1 = PolygonPatch(CIRCLE, facecolor='white', edgecolor='#001a00', linewidth=1)
_e2 = PolygonPatch(ELLIPSE, facecolor='white', edgecolor='#e60000', linewidth=1)
_polys = [_e1, _e2]
if CIRCLE.intersects(ELLIPSE):
    _intersect = CIRCLE.intersection(ELLIPSE)
    inter = PolygonPatch(_intersect, facecolor='#99e6ff',edgecolor='black', linewidth=1)
    _polys.append(inter)

# Plotting
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 8,
        }
_ax=plt.gca()
[_ax.add_artist(item) for item in _polys]
_ax.set_xlim(-10, 10)
_ax.set_ylim(0, 15)
_ax.set_aspect('equal', adjustable='box')
plt.title('Graphical Representation of Elliptical Pulsed Bead with Circular CMT Bead', fontsize=10, fontstyle='italic')
# plt.text(-6.8, 9.5, 'Area = '+str(A_p) + ' $\mathregular{mm^2}$', fontdict=font)
# plt.text(-6.8, 9, 'Percentage = '+str(percentage), fontdict=font)
plt.show()
