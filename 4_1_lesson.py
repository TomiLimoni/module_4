# ## решение задачи на O(N**2)
#
# def strcounter(s):
#     for lit in s:
#         counter = 0
#         for sub_lit in s:
#             if lit==sub_lit:
#                 counter += 1
#         print(lit,counter)
# strcounter('abdsadsdb')

# ## решение задачи O(N*M)
#
# # str = 'ejfnsekfj'
# # print(str)
# # print(set(str))
#
# def str(s):
#     for lit in set(s):
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter+=1
#         print(lit, counter)
# str('jfsdfsdfmlfsdkvl')

## решение задачи за O(N+N) -> O(N) -> O(N)

# def str(s):
#     lits_counter = {}
#     for lit in s:
#         lits_counter[lit] = lits_counter.get(lit, 0) + 1
#     for lits, counter in lits_counter.items():
#         print(lits,counter)
# str('aaadkfmdlfk')