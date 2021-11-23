import sys
import logging 

sys.path.append('GeneticEngine/')
#sys.path.append('PonyGE2/')

#from src.evaluation.gengine_evaluation import evaluate_geneticengine
#from src.evaluation.ponyge_evaluation import evaluate_ponyge
from src.evaluation.ponyge_evaluation2 import evaluate_ponyge2

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    
    if len(sys.argv) > 1:
        examples = sys.argv[1:]
    else:
        examples = list()

    #evaluate_ponyge(examples)
    evaluate_ponyge2(examples)
    #evaluate_geneticengine(examples)