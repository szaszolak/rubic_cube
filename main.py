from SearchAgent import SearchAgent

sa = SearchAgent()

print 'starting from'
sa.initial_cube.print_out()
print '============================='
sa.explore().cube.print_out()