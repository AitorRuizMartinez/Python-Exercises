# Exercise 28: Calculate the diffence of sets with colour elementes.

color_list_1 = ['Green', 'Black', 'Red', 'Orange']
color_list_2 = ['Green', 'Black', 'Red', 'Orange', 'Purple', 'White']

# A, B; A - B; A / B

colorset_1 = set(color_list_1)
colorset_2 = set(color_list_2)

diff_color = colorset_2 - colorset_1

print(diff_color)