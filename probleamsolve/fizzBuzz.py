

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        list=[]
        for i in range(1,n+1):
            if (i%5 == 0) and (i%3 != 0):
                list.append("Buzz")
            elif (i%3 == 0) and (i%5 != 0):
                list.append("Fizz")
            elif (i%3==0 and i%5==0):
                list.append("FizzBuzz")
            else:
                list.append(str(i))
        return list



s=Solution()
print(s.fizzBuzz(3))