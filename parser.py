from display import *
from matrix import *
from draw import *
import copy

ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus' ]

def parse_file( fname, edges, transform, screen, color ):

    f = open(fname)
    lines = f.readlines()

    step = 0.1
    c = 0
    while c < len(lines):
        print 'hi'
        for thing in transform:
            print_matrix(thing)
            
        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:            
            c+= 1
            args = lines[c].strip().split(' ')
            #print 'args\t' + str(args)
            
        if line == 'sphere':
            #print 'SPHERE\t' + str(args)
            edge=[]
            add_sphere(edge,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_polygons(edge, screen, color)
            display(screen)
            
        elif line == 'torus':
            #print 'TORUS\t' + str(args)
            edge=[]
            add_torus(edge,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step)
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_polygons(edge, screen, color)
            display(screen)
            
        elif line == 'box':
            #print 'BOX\t' + str(args)
            edge=[]
            add_box(edge,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_polygons(edge, screen, color)
            display(screen)
            
        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            edge=[]
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_lines(edge, screen, color)
            display(screen)
            
        elif line == 'hermite' or line == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            edge=[]
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)                      
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_lines(edge, screen, color)
            display(screen)
                        
        elif line == 'line':            
            #print 'LINE\t' + str(args)
            edge=[]
            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
            transform.append(matrix_mult(edge,copy.deepcopy(transform.pop())))
            clear_screen(screen)
            draw_lines(edge, screen, color)
            display(screen)
            
        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            transform.append(matrix_mult(copy.deepcopy(transform.pop()),t))

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            transform.append(matrix_mult(copy.deepcopy(transform.pop()),t))

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)
            
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            transform.append(matrix_mult(copy.deepcopy(transform.pop()),t))
                
        elif line == 'clear':
            edges = []
            
        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )

        elif line == 'display' or line == 'save':
            clear_screen(screen)
            draw_polygons(edges, screen, color)

            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])
        elif line == 'push':
            t=copy.deepcopy(transform.pop())
            t2=copy.deepcopy(t)
            transform.append(t)
            transform.append(t2)
        elif line == 'pop':
            transform.pop()
            
        c+= 1
