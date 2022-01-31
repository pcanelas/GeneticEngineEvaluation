import sys
import logging 

sys.path.append('GeneticEngine/')


from src.ponyge_comparison.gengine_evaluation import evaluate_geneticengine

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    
    if len(sys.argv) > 1:
        examples = sys.argv[2:]
    else:
        examples = list()
    
    # --mode=generations or --mode=timer
    if len(sys.argv) < 2 or '--mode=' not in sys.argv[1]:
        raise Exception('The --mode=generations or --mode=timer should be included after ./run_ponyge_comparison.sh')
    mode = sys.argv[1].split('=')[1]

    #evaluate_ponyge(examples)
    evaluate_geneticengine(examples, mode)