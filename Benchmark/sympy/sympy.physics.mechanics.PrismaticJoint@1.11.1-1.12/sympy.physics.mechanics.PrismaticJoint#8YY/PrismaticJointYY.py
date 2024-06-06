from sympy.physics.mechanics import Body, PrismaticJoint
parent = Body('P')
child = Body('C')
joint = PrismaticJoint('PC', parent=parent, child=child, coordinates=None)
