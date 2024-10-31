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
# ------------------------------