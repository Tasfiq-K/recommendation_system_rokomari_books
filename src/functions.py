import re

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
# ------------------------------