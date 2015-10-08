import datetime
from generator_sets import Point, Set, Generator

print('hi')
generator = Generator()
generator.init()
checktime = datetime.datetime.today()
sets = generator.generate()

i = 1
for set in sets:
    print('set number ', i)
    set.print_()
    i += 1
print(datetime.datetime.today() - checktime)





