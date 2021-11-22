import sys
from importlib import import_module

from src.evaluation.gengine_evaluation import *
from src.evaluation.ponyge_evaluation import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        examples = sys.argv[1:]
    else:
        examples = list()

    evaluate_ponyge(examples)
    evaluate_geneticengine(examples)