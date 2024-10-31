# -*- coding: utf-8 -*-
"""rokomari_books_initial_preprocessing.ipynb

Original file is located at
    https://colab.research.google.com/drive/12y3KFlds057TSmPNCzkonK3mej3gzphQ

# Setup
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Dataset/rokomari_books/Rokomari Recommendation Dataset/Datasets

# !ls

def main():
    
    ## Importing
    # ------------------------------
    from functions import actual_ratings
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # ------------------------------

    # Load the data

    df = pd.read_csv("rokomari_book_data_v2.csv")

    # Initial preprocessing starts

    # -------------------------------------------------------------
    # convert all the "No Language" to "বাংলা"
    df.loc[df['language'] == 'No Language', 'language'] = 'বাংলা'

    df['actual_rating'] = df.apply(actual_ratings, axis=1) # apply
    # -------------------------------------------------------------

    ## Save the data when you're done with modifying

    # overwriting the rokomari_book_data_v2.csv (fi any) at current location
    df.to_csv("rokomari_book_data_v2.csv", index=False)

    # Only Bangla books

    df_bn = df.loc[(df['language'] == 'বাংলা') | df['language'].str.contains('Bangla')]

    # save the only bangla books dataframe at current location
    df_bn.to_csv("rokomari_books_only_bangla_v2.csv", index=False)

if __name__ == "__main__":
    main()

