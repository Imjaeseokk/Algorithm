class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = ["" for _ in range(n)]
        for i in range(n):
            j = i+1
            if j%3 == 0:
                answer[i] += "Fizz"
            
            if j%5 == 0:
                answer[i] += "Buzz"
            
            if answer[i] == "":
                answer[i] = str(j)
        
        return answer