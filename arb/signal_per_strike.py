import pandas as pd
import numpy as np
from tqdm import tqdm
from signal_processing import load_all as signal
import matplotlib.pyplot as plt 

from util import *
from settings import *

# extract_all_tar(TAR_FILE_PATH, GZ_DIR)
full_strke_data = extract_all_gz(GZ_DIR)

pnl_dict = signal(full_strke_data)