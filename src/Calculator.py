class RuneData:
    """
    Automatically generates stat efficiency and rune efficiency\n
    Also contains methods for calculation
    """
    def __init__(self,rune_level,rune_stat_type,rune_stat_value):
        self.rune_stat_eff = self.cal_stat_eff(rune_stat_type,rune_stat_value)
        self.rune_eff = self.cal_rune_eff(rune_level,self.rune_stat_eff)

    def stat_max(self,rune_stat_type):
        """
        Return a value ranging from 30 to 40 depending on the type of stat it is\n
        Return None if rune_stat_type is out of bound

        >>> stat_max(1)
        40
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
        
    def rune_multiplier(self,rune_level):
        """
        Return a value based on the level of the rune(from 0.3 to 1)\n
        Return None if out of bounds

        >>> rune_multiplier(6)
        1
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

    def cal_stat_eff(self,rune_stat_type,rune_stat_value):
        rune_stat_eff = 0.0
        for i in range(5):
            rune_stat_eff += (rune_stat_value[i]/self.stat_max(rune_stat_type[i]))
        return rune_stat_eff

    def cal_rune_eff(self,rune_level,rune_stat_eff):
        return (((rune_stat_eff + (self.rune_multiplier(rune_level)))/2.8)*100)
        
