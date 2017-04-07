from BRECData import rune_multiplier
from BRECData import stat_max
rune_level  = 6
# pprefix, sub1, sub2, sub3, sub4
rune_stat_type = [2,8,6,7,1]
# prefix, sub1, sub2, sub3, sub4
rune_stat_value = [8,18,14,12,8]

rune_stat_efficiency = 0.0
for i in range(5):
    rune_stat_efficiency += (rune_stat_value[i]/stat_max(rune_stat_type[i]))

print(rune_stat_efficiency)
print((((rune_stat_efficiency + (rune_multiplier(rune_level)))/2.8)*100))
# total_eff + rune_level_multiplier * 100