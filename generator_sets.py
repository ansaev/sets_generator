__author__ = 'ansaev'
import random


class Generator(object):
    def __init__(self):
        self.sets_num = 0
        self.set_points = 0
        self.point_dimensions = 0

    def init(self, sets_num=5, set_points=5, point_dimensions=2):
        self.sets_num = sets_num
        self.set_points = set_points
        self.point_dimensions = point_dimensions

    def generate_point(self, rangeL=0, rangeR=20):
        point = Point()
        cords = []
        for i in range(self.point_dimensions):
            cords.append(random.uniform(rangeL, rangeR))
        point.init_mass(cords)
        return point

    def generate_point_in_range(self, range_set):
        point = Point()
        keys = {0: 'x', 1: 'y', 2: 'z', 3: 'k', 4: 'v'}
        cords = []
        for i in range(self.point_dimensions):
            cords.append(random.uniform(range_set[keys[i]]['min'], range_set[keys[i]]['max']))
        point.init_mass(cords)
        return point

    def generate_points(self, number, rangeL=0, rangeR=20):
        points = []
        for i in range(number):
            point = self.generate_point(rangeL, rangeR)
            points.append(point)
        return points

    def generate(self, separated=True):
        sets = []
        set = Set()
        range1 = random.uniform(100, 1000)
        range2 = random.uniform(500, 1000)
        # gengerate borders
        points = self.generate_points(6, range1, range2)
        set.init(points)
        i = 6
        # learn the range of borders
        set_range = set.getRange()
        while i < self.set_points:
            point = self.generate_point_in_range(set_range)
            # accept only points that in the range
            if not set.belong(point):
                points.append(point)
                i += 1
        set.init(points)
        sets.append(set)
        set_id = 1
        while set_id < self.sets_num:
            set = Set()
            range1 = random.uniform(100, 1000)
            range2 = random.uniform(500, 1000)
            # gengerate borders
            points = self.generate_points(6, range1, range2)
            set.init(points)
            range_my = set.getRange()
            passed = True
            this_passed = False

            for set_ex in sets:
                # we need to generate separated sets or not
                if separated:
                    # if yes then we chek if it's range not interact with other sets ranges
                    this_passed = False
                    this_passed = set_ex.not_in_range(range_my)
                    passed = passed and this_passed
                else:
                    # if not chek if at least 1 points included in other set
                    for point_s in set.points:
                        this_passed = this_passed or set_ex.in_borders(point_s)
                    passed = this_passed
            if not passed:
                continue
            i = 6
            # generate left points in border of 6 accepted points
            while i < self.set_points:
                point = self.generate_point_in_range(range_my)
                if not set.belong(point):
                    points.append(point)
                    i += 1
            set.init(points)
            sets.append(set)
            set_id += 1
        return sets


class Point(object):

    def __init__(self):
         self.cords = {}

    def init(self, x=0, y=0, z=0, k=0, v=0):
        self.cords['x'] = x
        self.cords['y'] = y
        self.cords['z'] = z
        self.cords['k'] = k
        self.cords['v'] = v

    def init_mass(self, mas):
        self.init()
        if 6 > mas.__len__() > 0:
            keys = {0: 'x', 1: 'y', 2: 'z', 3: 'k', 4: 'v'}
            for i, value in enumerate(mas):
                self.cords[keys[i]] = value

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
    def not_in_range(self, range):
        this_range = self.getRange()
        x_not_in_range = this_range['x']['max'] < range['x']['min'] or this_range['x']['min'] > range['x']['max']
        y_not_in_range = this_range['y']['max'] < range['y']['min'] or this_range['y']['min'] > range['y']['max']
        z_not_in_range = this_range['z']['max'] < range['z']['min'] or this_range['z']['min'] > range['z']['max']
        k_not_in_range = this_range['k']['max'] < range['k']['min'] or this_range['k']['min'] > range['k']['max']
        v_not_in_range = this_range['v']['max'] < range['v']['min'] or this_range['v']['min'] > range['v']['max']
        return x_not_in_range or y_not_in_range or z_not_in_range or k_not_in_range or v_not_in_range

    def getRange(self):
        range = {'x':{'min': self.points[0].cords['x'], 'max': self.points[0].cords['x']}, 'y':{'min': self.points[0].cords['y'], 'max': self.points[0].cords['y']},'z':{'min': self.points[0].cords['z'], 'max': self.points[0].cords['z']},'k':{'min': self.points[0].cords['k'], 'max': self.points[0].cords['k']},'v':{'min': self.points[0].cords['v'], 'max': self.points[0].cords['v']}}
        ind =0
        for point in self.points:
            for cord, value in point.cords.items():
                if range[cord]['min'] > value:
                    range[cord]['min'] = value
                elif range[cord]['max'] < value:
                    range[cord]['max'] = value
            ind += 1
        return range

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
        if not (x_changed or y_changed or z_changed or k_changed or v_changed):
            return False
        return True

    def print_(self):
        for point in self.points:
            point.print_()

