__author__ = 'ansaev'
import matplotlib.pyplot as plt


class Graph(object):
    colors = {0: "ro", 1: "bo", 2: "co", 3: "mo", 4: "yo"}
    set_num = 0
    plt.axis([100, 1000, 100, 1000])

    def show_set(self, set, x='x', y='y'):
        poits_x = []
        poits_y = []
        for point in set.points:
            poits_x.append(point.cords[x])
            poits_y.append(point.cords[y])
        plt.plot(poits_x, poits_y, self.colors[self.set_num])
        self.set_num += 1

    def show_sets(self, sets, x='x', y='y'):
        for set in sets:
            self.show_set(set, x=x, y=y)

    def show(self):
        plt.show()


def write_set(sets, data):
    i = 0
    for set in sets:
        # data.append(["set number: "+str(i)])
        for point in set.points:
            row =[]
            for cord, value in point.cords.items():
                row.append(value)
            row.append(i)
            data.append(row)
        i += 1
    return data

def write_data_in_exel(data, name):
    import xlwt
    book = xlwt.Workbook(encoding="utf8")
    sheet = book.add_sheet('sheet_1')
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            sheet.write(r, c, label=col)
    book.save(name+'.xls')

def write_in_xl(sets_separated=None, sets_noneseparated=None, name='Sets default name'):
    data = [["x", "y", "z", "k", "v", "class"]]
    data.append(["separated sets"])
    if sets_separated:
        write_set(sets_separated, data)
    data.append(["not separated sets"])
    if sets_noneseparated:
        write_set(sets_noneseparated, data)
    write_data_in_exel(data, name)
