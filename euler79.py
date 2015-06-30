passkeys=["129", "160", "162", "168", "180", "289", "316", "318", "319", "362", "368", "380", "389", "620", "629", "690", "710","716", "718","719", "731", "736", "760", "762", "769", "790", "890"]

# take_out=[ ]
# for x in passkeys:
#     nomatch = True
#     for y in passkeys:
#         if x == y:
#             pass
#         elif x[0] == y[-1] or x[-1] == y[0]:
#             nomatch = False
#         elif x[:2] == y[-2:] or y[:2] == x[-2:]:
#             nomatch = False
#     if nomatch:
#         take_out.append(x)
#
# print take_out


# start_nums=[]
# for x in set(passkeys)-set(take_out):
#     startonly = True
#     for y in passkeys:
#         if x == y:
#             pass
#         elif x[0] == y[-1]:
#             startonly = False
#         elif x[:2] == y[-2:]:
#             startonly = False
#     if startonly:
#         start_nums.append(x)
#
# print start_nums

# end_nums=[]
# for x in set(passkeys)-set(take_out):
#     endonly = True
#     for y in passkeys:
#         if x == y:
#             pass
#         elif x[-1] == y[0]:
#             endonly = False
#         elif x[-2:] == y[:2]:
#             endonly = False
#     if endonly:
#         end_nums.append(x)
#
# print end_nums

take_out=["380","710","719","760","790"] # +15
take_out_combine = ["389", "890","769","690","718","180"] # + 12
start_nums = ['762', '769', '389', '731', '736', '718', '716']
end_nums = ['129', '160', '180', '319', '620', '629', '690', '890']
final_end_nums = ['129', '160', '319', '620', '629'] # + 5-15
longest_starting_chains = ["3890", "716890", "71620", "71629", "7162890", "71690", "71629", "7160", "71620", "7180", "71890", "731620", "73162890", "731629", "7319", "73180", "73160", "73129", "731620", "731629", "7316890", "73160", "731620", "731629", "731690", "73180", "731890", "73162890", "7316890", "736890", "73629", "73620", "7362890", "73690", "73620", "73629", "7620", "762890", "7629", "7690"]
longest_modified_chains = []
start = ['762', '731', '736', '716']

pass_keys = list(set(passkeys) - set(take_out) - set(take_out_combine) - set(end_nums))
all_paths = ['76289', '7318', '73168', '7368', '7168', '73168', '7316289', '736289', '716289', '7316289']

combos = ['762|628|289|731|318|716|168','762|628|289|731|168','762|628|289|736|368','762|628|289|716|168']
complete_paths = []
all_paths = ['76289|7318|7168']
while len(all_paths)>0:
    print len(all_paths)
    test = all_paths.pop(0)
    complete = True
    for x in pass_keys:
        if x in test:
            continue
        if test[-2:] == x[:2]:
            all_paths.append(test +x[-1])
            complete = False
        elif test[-1] == x[0]:
            all_paths.append(test +x[-2:])
            complete = False
        else:
            all_paths.append(test +"|"+ x)
            complete = False
    if complete:
        complete_paths.append(test)
        print test
        # if complete and not a:
        #     print "winner"
        #     break
