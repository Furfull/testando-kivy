import csv
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('D:/Gabriel/Scripts/transferoacademy_transações_2.csv')

df1 = pd.read_csv('D:/Gabriel/Scripts/transferoacademy_saldos.csv')

print (df.shape[0] < df1.shape[0])