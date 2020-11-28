from sklearn.ensemble import AdaBoostClassifier
from utils import TreeBasedModel
from config import RANDOM_STATE
from hyperopt import hp
from hyperopt.pyll import scope
import numpy as np


class AdaBoostModel(TreeBasedModel):
    @staticmethod
    def build_estimator(args, train_data=None):
        return AdaBoostClassifier(random_state=RANDOM_STATE, **args)

    hp_space = {
        "algorithm": hp.choice("algorithm", ["SAMME", "SAMME.R"]),
        "n_estimators": scope.int(
            hp.qloguniform("n_estimators", np.log(10.5), np.log(1000.5), 1)
        ),
        "learning_rate": hp.lognormal("learning_rate", np.log(0.01), np.log(10.0)),
    }
