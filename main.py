import datetime

from generator_sets import Point, Set, Generator
from view import Graph, write_in_xl

# generate separated and none separated sets in 2d to show something
generator = Generator()
generator.init(sets_num=5, set_points=50, point_dimensions=2)
separated_sets = generator.generate()
none_separated_sets = generator.generate(separated=False)
# show some graphs
separated_graph = Graph()
not_separated_graph = Graph()
separated_graph.show_sets(separated_sets)
separated_graph.show()
not_separated_graph.show_sets(none_separated_sets)
not_separated_graph.show()

# generate separated and none separated sets in 5d to save it exel
generator = Generator()
generator.init(sets_num=5, set_points=50, point_dimensions=5)
separated_sets = generator.generate()
none_separated_sets = generator.generate(separated=False)
write_in_xl(separated_sets, none_separated_sets, "sets")







