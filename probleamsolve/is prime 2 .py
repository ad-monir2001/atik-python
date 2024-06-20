

class Solution:
    def count_is_prime(self,n):

        for i in (2,n):
            if n%i!=0:
                return f'{n} is a prime number because {n} is not divisible any number without 1,{n}'
            else:
                return f'{n} is not a prime number because {n} is divisible by 1,{i},{n}'

s=Solution()
print(s.count_is_prime(int(input("enter a number "))))


