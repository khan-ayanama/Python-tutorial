# l = ['abc','tuv','xyz']
# ans = [name[::-1] for name in l]
# print(ans)

input = [True,False,[1,2,3],1,1.0,3]


output = [item for item in input if type(item)==int or type(item)==float]




# for item in input:
#     if type(item) == float or type(item) == int:
#         output.append(item)

print(output)
