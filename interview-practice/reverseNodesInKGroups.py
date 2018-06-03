# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def convert(link_l):
    new_list = []
    while link_l is not None:
        new_list.append(link_l.value)
        link_l = link_l.next
    return new_list

def reverseNodesInKGroups(l, k):
    temp = convert(l)
    
    res = []
    for start in range(0, len(temp), k):
        end = start + k
        sub_list = temp[start:end]
        if len(sub_list) < k:
            res += sub_list[:]
        else:
            res += sub_list[::-1]
        
    return res
    
