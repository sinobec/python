set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
set2 = ["pineapple", "cherry"]
#set1.intersection_update(set2)
#set1.symmetric_difference_update(set2)
#print(set1)
 
set3 = set1.symmetric_difference(set2)
print(set3)