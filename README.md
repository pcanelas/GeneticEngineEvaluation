# Genetic Engine Evaluation
## Steps to run the Evaluation

1 - Run the setup file: ``./setup.sh``.

2 - Run ``./update.sh`` to ensure you are running the latest version in master for each framework.

3 - Execute the run evaluation file: ``./run_evaluation.sh --mode=timer``. 

You can specify a single example to be evaluated with the command ``./run_evaluation.sh example``.

You **are required** to choose what mode you want to evaluate: either by generations or timer. by using the following command:
``./run_evaluation.sh --mode=generations example`` or ``./run_evaluation.sh --mode=timer example`` 

4 - Execute the plot generator file by running: ``./plot_generator.sh``. 

You can specify a single example to be evaluated with the command ``./plot_generator.sh example``.
