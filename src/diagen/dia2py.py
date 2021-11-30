import sys

in_fn =  sys.argv[1]
in_fo = open(in_fn, 'r')

print('import diagen as dg')
print('')

module_name = '_'

all_modules = set('_')

def graph_head():
    print('def define_relations():')
    pass

def graph_foot():
    print('')

    for module_name in all_modules:
        print(f'{module_name} = dg.Module({repr(module_name)})')
        pass

    print('')
    print(f'all_modules = [{", ".join(all_modules)}]')
    print('')
    print('define_relations()')
    print('')
    print('dg.draw(all_modules)')
    pass

print('print(\'digraph {\')')

graph_head()
for line in in_fo.readlines():
    if line.strip() == '':
        continue
    if line.strip() == '---':
        graph_foot()
        graph_head()
        module_name = '_'
        all_modules = set('_')
        continue

    if line[0] == ' ':
        relname, *args = line.strip().split()
        args = [args[0]] + [repr(arg) for arg in args[1:]]
        print(f'    {module_name}.{relname}({", ".join(args)})')
        all_modules.add(args[0])
    else:
        module_name = line.strip()
        all_modules.add(module_name)
        pass
    pass

graph_foot()

print('print(\'}\')')

