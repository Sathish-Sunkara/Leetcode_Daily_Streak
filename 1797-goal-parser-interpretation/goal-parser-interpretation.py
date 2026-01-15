class Solution:
    def interpret(self, command: str) -> str:

        i = 0
        ans = ""
        while i < len(command) :
            if command[i] == "G" :
                ans += "G"
                i += 1
            elif command[i] == "(" :
                if command[i+1] == ")" :
                    i += 2
                    ans += "o"
                else :
                    i += 4
                    ans += "al"
        return ans
            

        