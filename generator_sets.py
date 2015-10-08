__author__ = 'ansaev'
import random


class Generator(object):
    def __init__(self):
        self.sets_num = 0
        self.set_points = 0
        self.point_dimensions = 0

    def init(self, sets_num=5, set_points=3, point_dimensions=2):
        self.sets_num = sets_num
        self.set_points = set_points
        self.point_dimensions = point_dimensions

    def generate(self):
        sets = []
        set = Set()
        points = []
        for i in range(self.set_points):
            point = Point()
            point.init(random.random()*100, random.random()*100, random.random()*100, random.random()*100, random.random()*100)
            points.append(point)
        set.init(points)
        sets.append(set)
        for set_id in range(1, self.sets_num):
            set = Set()
            points = []
            i = 0
            while i < self.set_points:
                point = Point()
                point.init(random.uniform(0, 20), random.uniform(0, 20), random.uniform(0, 20), random.uniform(0, 20), random.uniform(0, 20))
                in_borders = False
                for set_ex in sets:
                    in_borders = in_borders or set_ex.in_borders(point)
                if not in_borders:
                    print("accepted")
                    points.append(point)
                    i += 1
                # else:
                #     print("nope")
            set.init(points)
            sets.append(set)
        return sets


class Point(object):
    def __init__(self):
         self.cords = {}
    def init(self, x=0, y=0, z=0, k=0, v=0):
        self.cords['x'] = x
        self.cords['y'] = y
        self.cords['z']= z
        self.cords['k'] = k
        self.cords['v'] = v

    def equal(self, point):
        for cord, value in self.cords.items():
            if point.cords[cord] != value:
                return False
        return True

    def print_(self):
        msg = ""
        for cord, value in self.cords.items():
            msg += str(cord) + ": " + str(value) + ", "
        print(msg)



class Set(object):
    def __init__(self):
        self.points = []

    def init(self, points):
        self.points = points

    def belong(self, point):
        for b_point in self.points:
            if b_point.equal(point):
                return True
        return False

    def in_borders(self, point):
        if self.belong(point):
            return True
        x_right = self.points[0].cords['x'] < point.cords['x']
        x_changed = False
        y_right = self.points[0].cords['y'] < point.cords['y']
        y_changed = False
        z_right = self.points[0].cords['z'] < point.cords['z']
        z_changed = False
        k_right = self.points[0].cords['k'] < point.cords['k']
        k_changed = False
        v_right = self.points[0].cords['v'] < point.cords['v']
        v_changed = False

        for set_point in self.points:
            if (set_point.cords['x'] < point.cords['x']) != x_right:
                x_changed = True
            if (set_point.cords['y'] < point.cords['y']) != y_right:
                y_changed = True
            if (set_point.cords['z'] < point.cords['z']) != z_right:
                z_changed = True
            if (set_point.cords['k'] < point.cords['k']) != k_right:
                k_changed = True
            if (set_point.cords['v'] < point.cords['v']) != v_right:
                v_changed = True
        # print("try to border separate", x_changed, y_changed, z_changed, k_changed, v_changed)
        if not (x_changed or y_changed or z_changed or k_changed or v_changed):
            return False
        return True

    def print_(self):
        for point in self.points:
            point.print_()

