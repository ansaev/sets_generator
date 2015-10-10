__author__ = 'ansaev'
import matplotlib.pyplot as plt


class Graph(object):
    colors = {0: "ro", 1: "bo", 2: "co", 3: "mo", 4: "yo"}
    set_num = 0
    plt.axis([100, 1000, 100, 1000])

    def show_set(self, set):
        poits_x = []
        poits_y = []
        for point in set.points:
            poits_x.append(point.cords['x'])
            poits_y.append(point.cords['y'])
        plt.plot(poits_x, poits_y, self.colors[self.set_num])
        self.set_num += 1

    def show_sets(self, sets):
        for set in sets:
            self.show_set(set)

    def show(self):
        plt.show()


def write_set(sets, data):
    i = 0
    for set in sets:
        data.append(["set number: "+str(i)])
        i += 1
        for point in set.points:
            row =[]
            for cord, value in point.cords.items():
                row.append(value)
            data.append(row)
    return data

def write_data_in_exel(data, name):
    import xlwt
    book = xlwt.Workbook(encoding="utf8")
    sheet = book.add_sheet('sheet_1')
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            sheet.write(r, c, label=col)
    book.save(name+'.xls')

def write_in_xl(sets_separated, sets_noneseparated, name):
    data = [["x", "y", "z", "k", "v"]]
    data.append(["separated sets"])
    write_set(sets_separated, data)
    data.append(["not separated sets"])
    write_set(sets_noneseparated, data)
    write_data_in_exel(data, name)
