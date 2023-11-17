d1 , d2 , d3 = map(int , input().split())
ans1 = d1 + d2 + d3
ans2 = 2 * (d1 + d2)
ans3 = 2 * (d2 + d3)
ans4 = 2 * (d1 + d3)
print(min(ans1 , ans2 , ans3 , ans4))