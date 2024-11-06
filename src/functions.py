# !pip install langdetect -q -q -q

# !pip install deep_translator --quiet


import re
import langdetect as ld
import deep_translator as dt
from deep_translator import GoogleTranslator

# useful functions
# ------------------------------
# Function for computing the actual rating
def actual_ratings(row):
    """
    if n_ratings == 0 and rating == 5, then return 0
    else return rating
    """
    if (row['n_ratings'] == 0) and (row['rating'] == 5):
        return 0
    else:
        return row['rating']

def keep_only_bangla(row):
    """
    The unicode range between \u0980 - \u09FF defines the Bangla characters
    and digits in the Unicode character set
    """
    # return re.sub(r'[^\u0980-\u09FF ]+', '', str(row)).strip()
    return re.sub(r'[^\u0980-\u09FF\u0041-\u005A\u0061-\u007A :?]+', '', str(row)).strip()

def detect_language(row):
    try:
        lang = ld.detect(str(row))
    except:
        return 'unknown'
    return lang

def keep_only_bangla_v2(row):
    """
    The unicode range between \u0980 - \u09FF defines the Bangla characters
    and digits in the Unicode character set
    """
    return re.sub(r'[^-|,|\u0980-\u09FF| ]+', '', str(row)).strip()

def translate_to_bangla(row):
    return GoogleTranslator(source='auto', target='bn').translate(text=str(row))

def remove_unnecessary_characters(row):
    # pattern = r'[ও|():/, ]+'
    digit_map = str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯')
    text = re.sub(r'[:|ঃ]', ",", str(row))
    # text = re.sub(r'[/]', ", ", text)
    text = re.sub(r'[(|)]', "", text)
    text = re.sub(r'(\s)ও(\s)|(,\s)ও(\s)|(\s)এবং(\s)|/', ', ', text)
    # text = re.sub(r'\sও\s', ', ', text)
    text = re.sub(r'[\d|\d+]', lambda x: x.group(0).translate(digit_map), text)

    return text.strip()

def fix_more_categories_issue(row):
    text = re.sub(r'ক্লাস ৯, ১০', "ক্লাস ৯-১০,", str(row))
    text = re.sub(r"(পাঠ\s)সোহায়িকা|(পাঠো\s)সোহায়িকা|(পাঠের\s)সোহায়িকা", "পাঠ্য সহায়িকা", text)

    return text

# ------------------------------