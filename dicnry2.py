d={1:2,0:5,3:1,6:8,4:11}
print('original dictionary:',d)
sorted_d=sorted(d.items())

print('dictionary in ascending order:',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('dictionary in discending order:',sorted_d)

