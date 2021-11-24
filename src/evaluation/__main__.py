import sys
import logging 

sys.path.append('GeneticEngine/')
#sys.path.append('PonyGE2/')


from src.evaluation.gengine_evaluation import evaluate_geneticengine
#from src.evaluation.ponyge_evaluation import evaluate_ponyge
from src.evaluation.ponyge_evaluation2 import evaluate_ponyge2

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    
    if len(sys.argv) > 1:
        examples = sys.argv[2:]
    else:
        examples = list()
    
    # --mode=generations or --mode=timer
    if len(sys.argv) < 2 or '--mode=' not in sys.argv[1]:
        raise Exception('The --mode=generations or --mode=timer should be included after ./run_evaluation.sh')
    mode = sys.argv[1].split('=')[1]

    #evaluate_ponyge(examples)
    # evaluate_ponyge2(examples, mode)
    evaluate_geneticengine(examples, mode)