import sys
import gmsh
import math

'''
EXTERNAL DOMAIN:

^ y
|

4-------L---------3  !!  This line is the symmetric axes !!
|  *              |
H  *              |
|  *              |
1-----------------2  --> x


REFERENCE POSITION OF THE BODY POINTS:

8---7
|   |
5---6 

Configurations to be tested (coarse, medium, fine):
- 4
- 6
- 6 6 6
- 6 4 6 

Test wake with longer channel 

Boundary layer estimation:
https://www.fluidmechanics101.com/pages/tools.html
'''

# refinement and type of config definition
refinement = "supercoarse"
config     = "base"
########################## DO NOT DELETE THOSE 2 LINES ##############################################
##CONFIG
##REFINEMENT

# VARIABLES DEFINITIONS
SCALES = {
    'supercoarse': 2.0,   # ~40k  nodes  (Reference with the base case)
    'coarse'     : 1.5,   # ~60k  nodes  (Reference with the base case)
    'medium'     : 1,     # ~140k nodes
    'fine'       : 0.75,  # ~240k nodes
    'superfine'  : 0.5    # ~545k nodes
}

CONFIGS = {
    'base'   : [4], 
    'adv'    : [6],
    '666'    : [6, 6, 6],
    '646'    : [6, 4, 6]
}

l = 5.5e-3              # internal body length
h = 1e-3                # internal body height
L = 20*l  #about 100mm  # external domain length
H = 14*h  #14e-3        # external domain height
x_0 = 4*l #22e-3        # distance from inlet to first body
x_dist = 0.6*l  # 3.5e-3 # distance between bodies along the x diection
COLS = CONFIGS[config]   # array containing the number of bodies for each column

MESH_SIZE = l*SCALES[refinement] / 15 # mesh size of external mesh

MESH_SIZE_BODIES = MESH_SIZE / 15   # mesh size for bodies
MESH_SIZE_CORNERS = MESH_SIZE / 50  # mesh size for body corners

# define boundary layer properties
BL_OPTIONS = {
    'Quads': 1,
    'Ratio': max(1.0, 1.1 - 0.1 * (2 - SCALES[refinement])), # growth ratio
    'Size': min(1e-5, MESH_SIZE_CORNERS), # First layer
    'Thickness': 1.5e-4 # delta99
}

WALL_BL_NODES = 10 # number of bl nodes (only for lower wall)

BODY_RADIUS = l / 50 # radius for body corners
FAN_SIZE = math.ceil(math.pi * BODY_RADIUS / 2 / MESH_SIZE_CORNERS) # for boundary layer at corners

N_NODES_l = math.ceil(l / MESH_SIZE_BODIES)         # number of nodes along body length
N_NODES_h = math.ceil(h / MESH_SIZE_BODIES * 1.5)   # number of nodes along body height

BUMP_COEF_l = 0.25  # bump coefficient along body lenght
BUMP_COEF_h = 0.5   # bump coefficient along body height

# define refinement box properties
REFBOX_OPTIONS = {
    'VIn': MESH_SIZE / 5,   # smaller element size inside the box
    'VOut': MESH_SIZE,      # larger element size outside the box
    'XMin': x_0 * 0.9,      # start of the box in X
    'XMax': x_0 + (x_dist + l)*len(COLS) + 4*l, # end of the box in X
    'YMin': 0,              # start of the box in Y
    'YMax': H,              # end of the box in Y
    'Thickness': 3*l        # thickness to create smooth transition
}


class Rectangle:
    def __init__(self, pos_x: float, pos_y: float, dx: float, dy: float, create_lines: bool=True) -> None:
        '''
        Create a rectangle. \\
        By default, also lines, curve loop and surface are created.
        '''
        # create points
        p1 = gmsh.model.geo.add_point(pos_x,    pos_y,    0)
        p2 = gmsh.model.geo.add_point(pos_x+dx, pos_y,    0)
        p3 = gmsh.model.geo.add_point(pos_x+dx, pos_y+dy, 0)
        p4 = gmsh.model.geo.add_point(pos_x,    pos_y+dy, 0)

        self.points = [p1, p2, p3, p4]

        # return if no line must be created
        if not create_lines:
            return

        # create lines
        l1 = gmsh.model.geo.add_line(p1, p2)
        l2 = gmsh.model.geo.add_line(p2, p3)
        l3 = gmsh.model.geo.add_line(p3, p4)
        l4 = gmsh.model.geo.add_line(p4, p1)

        self.lines = [l1, l2, l3, l4]

        # create curve loop
        self.curve_loop = gmsh.model.geo.add_curve_loop(self.lines)
        self.surface = None # surface will be generated later


class BoundaryLayer:
    def __init__(self, points: list, lines: list) -> None:
        '''
        Points and lines must already exists. \\
        A new curve loop and a new surface will be created. \\
        Transfinite lines and surface are created.
        '''
        self.points = points
        self.lines = lines
        # create curve loop
        self.curve_loop = gmsh.model.geo.add_curve_loop(lines)
        self.surface = gmsh.model.geo.add_plane_surface([self.curve_loop])

        # Make transifinite lines (usual counterclockwise order starting from lower line)
        bl_ratio = BL_OPTIONS['Ratio']

        gmsh.model.geo.mesh.set_transfinite_curve(lines[1],
                                                  WALL_BL_NODES,
                                                  meshType='Prog',
                                                  coef=bl_ratio)
        
        gmsh.model.geo.mesh.set_transfinite_curve(lines[3],
                                                  WALL_BL_NODES,
                                                  meshType='Prog',
                                                  coef=1/bl_ratio)
        
        gmsh.model.geo.mesh.set_transfinite_surface(self.surface)
        gmsh.model.geo.mesh.set_recombine(2, self.surface) # make bl mesh structured


class Body:
    def __init__(self, pos_x, pos_y, dx, dy) -> None:
        '''
        Create a rectangle with round corners. \\
        Also lines, curve loop and surface are created.
        '''
        r = BODY_RADIUS
        
        # create points
        p1 = gmsh.model.geo.add_point(pos_x+r,      pos_y,      0)
        p2 = gmsh.model.geo.add_point(pos_x+dx-r,   pos_y,      0)
        p3 = gmsh.model.geo.add_point(pos_x+dx,     pos_y+r,    0)
        p4 = gmsh.model.geo.add_point(pos_x+dx,     pos_y+dy-r, 0)
        p5 = gmsh.model.geo.add_point(pos_x+dx-r,   pos_y+dy,   0)
        p6 = gmsh.model.geo.add_point(pos_x+r,      pos_y+dy,   0)
        p7 = gmsh.model.geo.add_point(pos_x,        pos_y+dy-r, 0)
        p8 = gmsh.model.geo.add_point(pos_x,        pos_y+r,    0)

        self.points = [p1, p2, p3, p4, p5, p6, p7, p8]

        # get circle centers
        c1 = gmsh.model.geo.add_point(pos_x+dx-r,   pos_y+r,    0)
        c2 = gmsh.model.geo.add_point(pos_x+dx-r,   pos_y+dy-r, 0)
        c3 = gmsh.model.geo.add_point(pos_x+r,      pos_y+dy-r, 0)        
        c4 = gmsh.model.geo.add_point(pos_x+r,      pos_y+r,    0)

        centers = iter([c1, c2, c3, c4])

        # create lines
        self.straight_lines = []
        self.corners = []
        self.lines = []
        is_straight = True

        for p1, p2 in zip(self.points[0:], [*self.points[1:], self.points[0]]):
            if is_straight:
                # create straight lines
                new_line = gmsh.model.geo.add_line(p1, p2)
                self.straight_lines.append(new_line)
            else:
                # create round corners
                center = next(centers)
                new_line = gmsh.model.geo.add_circle_arc(p1, center, p2)
                self.corners.append(new_line)

            # append new line to list
            self.lines.append(new_line)
            is_straight = not is_straight

        # set straight lines as transfinite lines
        for line in [self.straight_lines[0], self.straight_lines[2]]:
            gmsh.model.geo.mesh.set_transfinite_curve(line,
                                                      N_NODES_l,
                                                      meshType='Bump',
                                                      coef=BUMP_COEF_l)
        
        for line in [self.straight_lines[1], self.straight_lines[3]]:
            gmsh.model.geo.mesh.set_transfinite_curve(line,
                                                      N_NODES_h,
                                                      meshType='Bump',
                                                      coef=BUMP_COEF_h)

        # set corners as transfinite lines
        for corner in self.corners:
            gmsh.model.geo.mesh.set_transfinite_curve(corner, FAN_SIZE)

        # create curve loop
        self.curve_loop = gmsh.model.geo.add_curve_loop(self.lines)
        self.surface = None # surface will be generated later


def domain_initialization(pos_x: float, pos_y: float, dx: float, dy: float) -> tuple[Rectangle, BoundaryLayer]:
    """
    This function aims to create the domain we want to use for our simulation. \\
    We do have 2 distinct regions connected by a transfinite line, \\
    the lower region aims to produce a stuctured grid for the BL subdomain, \\
    the upper region instead aims to produce our domain of intrest \\
    (i.e. where we do put the bodies). \\
    Only half the domain will be generated. \\
    The functions also provides the rename of the boundaries (inlet, outlet, ...), \\
    except for the internal volume.
    """
    bl_thick = BL_OPTIONS['Thickness']

    # Initialize the external rectangle - domain height is reduced by the bl thickness
    domain = Rectangle(pos_x, pos_y + bl_thick, dx, dy/2 - bl_thick)

    '''
    Boundary layer points:
    4-----------3
    |           |
    1-----------2
    
    They follow the same convention as the external domain.
    '''

    bl_p1 = gmsh.model.geo.add_point(pos_x,      pos_y, 0)
    bl_p2 = gmsh.model.geo.add_point(pos_x + dx, pos_y, 0)
    bl_p3 = domain.points[1]
    bl_p4 = domain.points[0]

    # Define lines of the bl (they follow the same convention as the external domain)
    bl_l1 = gmsh.model.geo.add_line(bl_p1, bl_p2)
    bl_l2 = gmsh.model.geo.add_line(bl_p2, bl_p3)
    bl_l3 = - domain.lines[0] # this line already exists, but it must be re-oriented
    bl_l4 = gmsh.model.geo.add_line(bl_p4, bl_p1)

    bl = BoundaryLayer([bl_p1, bl_p2, bl_p3, bl_p4],
                       [bl_l1, bl_l2, bl_l3, bl_l4])

    # Rename the boudaries
    center_lines = [domain.lines[2]]
    walls        = [bl.lines[0]]
    inlets       = [domain.lines[3], bl.lines[3]]
    outlets      = [domain.lines[1], bl.lines[1]]

    # Add physical groups for the boundaries
    gmsh.model.geo.add_physical_group(1, center_lines, name='centerLine')
    gmsh.model.geo.add_physical_group(1, walls,        name='wall')
    gmsh.model.geo.add_physical_group(1, inlets,       name='inlet')
    gmsh.model.geo.add_physical_group(1, outlets,      name='outlet')

    return domain, bl


# Main program
def main() -> None:
    gmsh.initialize()

    # create bodies
    bodies = []

    for j,col in enumerate(COLS):
        y_spacing = (H - col*h) / (col + 1)
        pos_x = x_0 + j*(x_dist + l) # x-coordinate of bodies (distance between inlet and bodies, fit row)

        n_bodies = int(col/2)

        for i in range(n_bodies):
            pos_y = y_spacing + i * (h + y_spacing)

            bodies.append(
                Body(pos_x, pos_y, l, h)
            )

            print(f'Body {i+1} for column {j+1} generated!')
    
    # define physical lines for bodies
    body_lines = []

    for body in bodies:
        body_lines.extend(body.lines)

    gmsh.model.geo.add_physical_group(1, body_lines, name='heatSource')
        
    # create external domain + boundary layer
    domain, bl = domain_initialization(0, 0, L, H)
    print('\nDomain generated!')

    # define plane surface for fluid domain
    curve_loops = [body.curve_loop for body in bodies]
    curve_loops.insert(0, domain.curve_loop)                     
    domain.surface = gmsh.model.geo.add_plane_surface(curve_loops)
    
    # define physical surface for fluid domain
    gmsh.model.geo.add_physical_group(2, [bl.surface, domain.surface], name='volume')
    gmsh.model.geo.synchronize()

    # create boundary layer field (only for bodies)
    bl_tag = gmsh.model.mesh.field.add('BoundaryLayer')

    # get lines from which boundary layer will be built
    bl_curves = []

    for body in bodies:
        bl_curves.extend(body.lines)

    # set boundary layer properties
    gmsh.model.mesh.field.set_numbers(bl_tag, 'CurvesList', bl_curves)

    for key, value in BL_OPTIONS.items():
        gmsh.model.mesh.field.set_number(bl_tag, key, value)
    
    gmsh.model.mesh.field.set_as_boundary_layer(bl_tag)

    print('\nBoundary layer generated!')

    # create a refinemente box to refine mesh where wake is expected
    box_tag = gmsh.model.mesh.field.add('Box')

    for key, value in REFBOX_OPTIONS.items():
        gmsh.model.mesh.field.set_number(box_tag, key, value)

    gmsh.model.mesh.field.set_as_background_mesh(box_tag)

    print('\nRefinement box created!')

    # generate and save mesh
    print('\nCreating mesh...')
    # gmsh.model.geo.mesh.set_algorithm(2, domain.surface, 2) # change mesh algorithm
    # gmsh.model.geo.mesh.set_recombine(2, domain.surface) # convert to quadrilaterals
    # gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.option.set_color("Geometry.Color.Points", 255, 165, 0)
    gmsh.option.set_color("Geometry.Color.Lines", 10, 109, 240)
    gmsh.option.set_color("Mesh.Color.One", 255, 0, 0)
    gmsh.option.set_color("Mesh.Color.Two", 0, 0, 255)
    print('Mesh done!\n')
    format = ".su2"
    name = config+refinement+format
    gmsh.write(name)

    # Launch the GUI to see the results:
    if '-nopopup' not in sys.argv:
        gmsh.fltk.run()

    gmsh.finalize()


if __name__ == '__main__':
    main()
