class Module(object):
    def __init__(self, name):
        self.name = name
        self.uses = set()
        self.owns = set()
        self.calls = dict()
        self.inherits = set()
        pass

    def inherit(self, other):
        self.inherits.add(other)
        pass

    def use(self, other):
        self.uses.add(other)
        pass

    def own(self, other):
        self.owns.add(other)
        pass

    def call(self, call, *args):
        if call in self.calls:
            self.calls[call].extend(args)
        else:
            self.calls[call] = list(args)
            pass
        pass
    pass

def draw(modules):
    print('subgraph {')
    for module in modules:
        for use in module.uses:
            print(f'    {module.name} -> {use.name}')
            pass
        for own in module.owns:
            print(f'    {module.name} -> {own.name} [arrowtail=odiamond, dir=back, color=blue, weight=10]')
            pass
        for call in module.calls.keys():
            args = module.calls[call]
            print(f'    {module.name} -> {call.name} [label="{", ".join(args)}"]')
            pass
        for inherit in module.inherits:
            print(f'    {inherit.name} -> {module.name} [arrowtail=empty, dir=back, color=blue, weight=10]')
            pass
        pass
    print('}')
    pass
