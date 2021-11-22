import sys
import logging 

sys.path.append('GeneticEngine/')

from src.evaluation.gengine_evaluation import evaluate_geneticengine
from src.evaluation.ponyge_evaluation import evaluate_ponyge

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    
    if len(sys.argv) > 1:
        examples = sys.argv[1:]
    else:
        examples = list()

    evaluate_ponyge(examples)
    evaluate_geneticengine(examples)