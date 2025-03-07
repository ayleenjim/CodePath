# def manage_stage_changes(changes):
#     mainStack = []
#     reschedule = []

#     for c in changes:
#         if (c == 'Cancel' and mainStack):
#             reschedule.append(mainStack.pop())
#             #mainStack.pop() #pops twice!
#         elif (c == 'Reschedule' and mainStack):
#             mainStack.append(reschedule[-1])
#         else:
#             mainStack.append(c[-1])
    
#     return mainStack


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

import heapq

def process_performance_requests(requests):
    sortPriority = sorted(requests, key=lambda pair: pair[0], reverse=True)
    ans = [pair[1] for pair in sortPriority]

    return ans

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))