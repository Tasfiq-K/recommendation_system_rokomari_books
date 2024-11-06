# -*- coding: utf-8 -*-
# Setup
import re
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import langdetect as ld
import deep_translator as dt
from deep_translator import GoogleTranslator
from functions import (translate_to_bangla,
                       keep_only_bangla_v2,
                       detect_language,
                       remove_unnecessary_characters,
                       fix_more_categories_issue
                       )

# Only Bangla Books

# load the rokomari_bn_books.csv
df_bn = pd.read_csv("rokomari_books_only_bangla_v2.csv")

## 2.2 Fixing categories detected as other language to Bangla and mixed lanugage

### 2.2.1 Fixing categories detected as other language to Bangla
df_bn['language_categories'] = df_bn['categories'].apply(detect_language)


for language in df_bn['language_categories'].value_counts().index:
    if language == 'bn' or language == 'ar':
        continue
    else:
        print(f"Correcting Language: {language}")
        filt = (df_bn['language_categories'] == language, 'categories')
        df_bn.loc[filt] = df_bn.loc[filt].apply(translate_to_bangla)

print("\nDone")

## 2.2.2 Fixing categories with mixed languages with Bangla"""

filt = (df_bn['language_categories'] == 'ar', 'categories')

df_bn.loc[filt] = df_bn.loc[filt].apply(keep_only_bangla_v2)

df_bn.loc[df_bn['language_categories'] == 'en', 'categories']

df_bn['language_categories'] = df_bn['categories'].apply(detect_language)


df_bn.loc[df_bn['categories'] == 'নবী-রাসূল, সাহাবা, তাবেয়ী ও অলি-আউলিয়া', 'categories'] = "নবী-রাসুল, সাহাবী, তাবেঈ, ওলি-আউলিয়া"

df_bn.loc[df_bn['language_categories'] == 'fr', 'categories'] = "যখন ৪-৮, উপকথা"

df_bn.loc[df_bn['language_categories'] == 'vi', 'categories'] = "টোফেল"

df_bn.loc[df_bn['language_categories'] == 'en', 'categories'] = "উক্তি, বাণী, প্রবাদ"

### 3.2 Stripping unnecessary characters

df_bn.loc[:, 'categories_fixed'] = df_bn['categories'].apply(remove_unnecessary_characters)


## 3.2.1 Keeping only the bangla characters"""

df_bn.loc[:, 'categories_fixed'] = df_bn['categories_fixed'].apply(keep_only_bangla_v2)

df_bn.loc[df_bn['categories_fixed'] == "ফ্যামিলি , পার্সোনাল লস", 'categories_fixed']

# নারী, শিশু ল
# ফ্যামিলি , পার্সোনাল লস
# অন্যরা
df_bn.loc[df_bn['categories_fixed'] == "ফ্যামিলি , পার্সোনাল লস", 'categories_fixed'] = "ফ্যামিলি, পার্সোনাল লস"

# text = "ক্লাস ৯, ১০ এসএসসি, রসায়ন পাঠ সোহায়িকা, পাঠো সোহায়িকা"

df_bn.loc[:, 'categories_fixed'] = df_bn['categories_fixed'].apply(fix_more_categories_issue)


df_bn.to_csv("rokomari_books_only_bangla_v2.csv", index=False)