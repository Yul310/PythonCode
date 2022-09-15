class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        array = {
            "{":"}",
            "[":"]",
            "(":")"  
        }  
        new = []
       
        if len(s)%2 != 0:
            return False
        for a in s:
            if a in array:
                new.append(array.get(a))
            elif len(new) != 0 and new[len(new)-1] == a:
                new.pop()
            else:
                return False
                
        if len(new) == 0:
            return True
        else:
            return False
                
    
    
    
#         array = []
#         for a in s:
#                 array.append(a)
#                 if len(array) > 1 and array[len(array)-2] == "{" and array[len(array)-1]=="}":
#                      array.pop(len(array)-1)
#                      array.pop(len(array)-1)
#                 elif len(array) > 1 and array[len(array)-2] == "[" and array[len(array)-1]=="]":
#                      array.pop(len(array)-1)
#                      array.pop(len(array)-1)
#                 elif len(array) > 1 and array[len(array)-2] == "(" and array[len(array)-1]==")":  
#                      array.pop(len(array)-1)
#                      array.pop(len(array)-1)
          
    
#         if len(array) == 0:
#             return True
#         else:
#             return False