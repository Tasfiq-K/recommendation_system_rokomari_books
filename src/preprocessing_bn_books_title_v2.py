# -*- coding: utf-8 -*-
"""# Import"""

import time
import numpy as np
import pandas as pd
from functions import keep_only_bangla

"""# 1. Load Dataframe"""

df_bn = pd.read_csv("rokomari_books_only_bangla_v2.csv")
df_bn['bangla_title'] = df_bn['title'].apply(keep_only_bangla)

# sanity check if everthing got erased or subbed with space
print(df_bn.loc[(df_bn['bangla_title'] == ' ') | (df_bn['bangla_title'] == '')])


# save the dataframe

df_bn.to_csv("rokomari_books_only_bangla_v2.csv", index=False)