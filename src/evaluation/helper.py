from importlib import import_module

def get_eval_method(example_path, method_name):
    example_path = example_path.replace('/', '.')
    mod = import_module(example_path[:-3], 'geneticengine')
    return getattr(mod, method_name)