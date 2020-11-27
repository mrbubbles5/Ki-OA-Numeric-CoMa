def get_lattice_point_number(h,a1,a2,b1,b2=int):
    
    
    if h < 0:

        return "Die Eingabe ist fehlerhaft."

    R = convert_to_standard(a1,a2,b1,b2)
    
    if intersects(h,R[0],R[1],R[2],R[3]):
        points = (get_delta_x1(R[0],R[2]) + 1) * (get_delta_x2(h,R[1],R[3]) + 1)

        return "Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {}.".format(points)

    else:

        return "Der Schnitt im gegebenen Rechteck ist leer."


def convert_to_standard(a1,a2,b1,b2=int):
    R = (min(a1,b1),min(a2,b2),max(a1,b1),max(a2,b2))

    return R


def intersects(h,a1,a2,b1,b2):

    if get_delta_x1(a1,b1) < 0 or get_delta_x2(h,a2,b2) < 0:

        return False

    else:

        return True


def get_delta_x1(a1,b1):
    delta_x1 = min(b1 - max(a1,0),6 - max(a1,0))
        
    return delta_x1


def get_delta_x2(h,a2,b2):
    delta_x2 = min(b2 - max(a2,0),h - max(a2,0))

    return delta_x2
