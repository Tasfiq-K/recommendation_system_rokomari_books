import pandas as pd
from functions import detect_language, translate_to_bangla, translate_from_id, correct_author_names

## Only Bangla Books

df_bn = pd.read_csv("rokomari_books_only_bangla_v2.csv")

df_bn['language_author'] = df_bn['author'].apply(detect_language)

for language in df_bn['language_author'].value_counts().index:
    if language == 'bn' or language == 'ar':
        continue
    else:
        print(f"Correcting Language: {language}")
        filt = (df_bn['language_author'] == language, 'author')
        df_bn.loc[filt] = df_bn.loc[filt].apply(translate_to_bangla)

print("\nDone")

df_bn['language_author'] = df_bn['author'].apply(detect_language)


# changing manually the author name Prabir Kumar Pal (সম্পাদক) to প্রবীর কুমার পাল

df_bn.loc[df_bn['author'] == 'Prabir Kumar Pal', 'author'] = 'প্রবীর কুমার পাল'

df_bn['language_author'] = df_bn['author'].apply(detect_language)

for language in df_bn['language_author'].value_counts().index:
    if language == 'bn' or language == 'ar':
        continue
    else:
        print(f"Correcting Language: {language}")
        filt = (df_bn['language_author'] == language, 'author')
        df_bn.loc[filt] = df_bn.loc[filt].apply(translate_to_bangla)

print("\nDone")

df_bn.loc[df_bn['language_author'] == 'id', 'author'] = df_bn.loc[df_bn['language_author'] == 'id', 'author'].apply(translate_from_id)

df_bn['language_author'] = df_bn['author'].apply(detect_language)
df_bn['language_author'].value_counts()

# let's see the names with arabic ones

for idx, names in enumerate(df_bn.loc[df_bn['language_author'] == 'ar', 'author']):
    print(f"{idx} | {names}")

# changing this name حكيم الامت مولانا اشرف علي تهانوي رح ( হাকীমুল উম্মত মাওলানা আশরাফ আলী থানভী রহ.) (সম্পাদক) to ( হাকীমুল উম্মত মাওলানা আশরাফ আলী থানভী রহ.)

df_bn.loc[df_bn['author'] == 'حكيم الامت مولانا اشرف علي تهانوي رح ( হাকীমুল উম্মত মাওলানা আশরাফ আলী থানভী রহ.) (সম্পাদক)', 'author'] = "হাকীমুল উম্মত মাওলানা আশরাফ আলী থানভী রহ."

# no more
df_bn.loc[df_bn['author'] == 'حكيم الامت مولانا اشرف علي تهانوي رح ( হাকীমুল উম্মত মাওলানা আশরাফ আলী থানভী রহ.) (সম্পাদক)', 'author'].shape

## Fixing the mixed language in author names (Arabic and Bangla)

filt = (df_bn['language_author'] == 'ar', 'author')
df_bn.loc[filt] = df_bn.loc[filt].apply(correct_author_names)


## Fixing the mixed language in author names (English and Bangla)

filt = (df_bn['language_author'] == 'en', 'author')

df_bn.loc[filt] = df_bn.loc[filt].apply(correct_author_names)


df_bn['language_author'] = df_bn['author'].apply(detect_language)

## Fixing all author names (keeping only with bangla letters)

df_bn.loc[:, 'author'] = df_bn['author'].apply(correct_author_names)

df_bn['language_author'] = df_bn['author'].apply(detect_language)

print(df_bn['language_author'].value_counts())

"""All Bangla! yay!"""

df_bn.to_csv("../csv_files/rokomari_books_only_bangla_v2.csv", index=False)