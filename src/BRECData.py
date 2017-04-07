def stat_max(rune_stat_type):
    """
       Return a value ranging from 30 to 40 depending on the type of stat it is
       Return None if rune_stat_type is out of bound
    """
    # HP, DEF, ACC, ATK, RES
    if rune_stat_type <= 5:
        return 40
    # CD
    elif rune_stat_type == 6:
        return 35
    # CR, SPD
    elif rune_stat_type >=7 & rune_stat_type < 8:
        return 30
    else:
        return None
    
def rune_multiplier(rune_level):
    """
        Return a value based on the level of the rune(from 0.3 to 1)
        Return None if out of bounds
    """
    if rune_level == 1:
        return 0.3
    elif rune_level == 2:
        return 0.45
    elif rune_level == 3:
        return 0.6
    elif rune_level == 4:
        return 0.75
    elif rune_level == 5:
        return 0.85
    elif rune_level == 6:
        return 1
    else:
        return None

