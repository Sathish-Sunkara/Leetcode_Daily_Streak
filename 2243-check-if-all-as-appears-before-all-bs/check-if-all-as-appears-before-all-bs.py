class Solution:
    def checkString(self, s: str) -> bool:
        a_last_index = -99
        b_first_index = -99
        for i, ch in enumerate(s) :
            if ch == "a" :
                a_last_index = i
            if ((ch == "b") and (b_first_index == -99)) :
                b_first_index = i
        # print(a_last_index ,b_first_index)
        
        if b_first_index != -99 and a_last_index != -99 :
            if a_last_index < b_first_index :
                return True
            else :
                return False

        elif b_first_index == -99  :
            return True

        else :
            return True

        