import pandas
import numpy
import matplotlib
import seaborn
import sklearn
import scipy

# affiche le nom et la version de chaque bibliotheque
bibliotheques = [pandas, numpy, matplotlib, seaborn, sklearn, scipy]
for module in bibliotheques:
    print(module.__name__, "->", module.__version__)