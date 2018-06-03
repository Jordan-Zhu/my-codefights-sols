# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def convert(l):
    res = []
    while l is not None:
        res.append(l.value)
        l = l.next
    return res


def rearrangeLastN(l, n):
    new_list = convert(l)
    
    return new_list[-n:] + new_list[:-n]
