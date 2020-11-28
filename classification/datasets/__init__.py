from .loaders import DefaultCreditCardDataset
from .loaders import AdultDataset
from .loaders import YeastDataset
from .loaders import SeismicBumpsDataset
from .loaders import StatlogAustralianDataset
from .loaders import StatlogGermanDataset
from .loaders import SteelPlatesFaultsDataset
from .loaders import RetinopathyDataset
from .loaders import BreastCancerDataset
from .loaders import ThoraricSurgeryDataset

all_datasets = [
    StatlogAustralianDataset,
    StatlogGermanDataset,
    SteelPlatesFaultsDataset,
    ThoraricSurgeryDataset,
    YeastDataset,
    SeismicBumpsDataset,
    RetinopathyDataset,
    BreastCancerDataset,
    # These ones were done with 3000s instead of 1000s and 1000 per step
    AdultDataset,
    DefaultCreditCardDataset,
]
