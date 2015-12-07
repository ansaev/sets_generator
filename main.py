import datetime

from generator_sets import Point, Set, Generator
from view import Graph, write_in_xl

# generate separated and none separated sets in 2d to show something
generator = Generator()
generator.init(sets_num=5, set_points=50, point_dimensions=5)
separated_sets = generator.generate(separated=True)
# none_separated_sets = generator.generate(separated=False)
# show some graphs

# not_separated_graph = Graph()
cords = ['x', 'y', 'z', 'k', 'v']
for x in cords:
    cords.remove(x)
    for y in cords:
        print(x, y)
        separated_graph = Graph()
        separated_graph.show_sets(separated_sets, x=x, y=y)
        separated_graph.show()
# not_separated_graph.show_sets(none_separated_sets)
# not_separated_graph.show()

# generate separated and none separated sets in 5d to save it exel
generator = Generator()
generator.init(sets_num=5, set_points=50, point_dimensions=5)
separated_sets = generator.generate()
# none_separated_sets = generator.generate(separated=False)
write_in_xl(sets_separated=separated_sets, name="sets")







