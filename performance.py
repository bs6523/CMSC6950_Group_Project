import sys
import pstats
p=pstats.Stats('output_main.prof')
p.sort_stats('tottime')
p.print_stats(15)

