# I traverse both lists using two pointers. 
# When a pointer reaches the end, I switch it to the head of the other list. 
# This equalizes the distance traveled, allowing the pointers to meet at the intersection node 
# or both reach None if there is no intersection.

#Intersection of two linked list
def intersection_linked_list(head1,head2):
    
    cur1, cur2 = head1, head2
    
    while cur1 != cur2:
        cur1 = cur1.next if cur1 else head2
        cur2 = cur2.next if cur2 else head1
    
    return cur1

#Brute Force Approach
def intersection_linked_list(head1, head2):

    cur1 = head1

    while cur1:

        cur2 = head2

        while cur2:

            if cur1 == cur2:
                return cur1

            cur2 = cur2.next

        cur1 = cur1.next

    return None