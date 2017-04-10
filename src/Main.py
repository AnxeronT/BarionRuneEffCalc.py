import Calculator
rune_level  = 6
# pprefix, sub1, sub2, sub3, sub4
rune_stat_type = [2,8,6,7,1]
# prefix, sub1, sub2, sub3, sub4
rune_stat_value = [8,18,14,12,8]

rune1 = Calculator.RuneData(rune_level,rune_stat_type,rune_stat_value)
print(rune1.rune_stat_eff)
print(rune1.rune_eff)

rune1.something = rune1.stat_max(rune_stat_type[1])
print(rune1.something)

# total_eff + rune_level_multiplier * 100