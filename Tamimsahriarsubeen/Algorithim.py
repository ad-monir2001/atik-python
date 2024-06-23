
class Alogarithim:
    def search(self,a:list[int],m:int)->int:
        a.sort()
        left=0
        right=len(a)+1
        mid=(right+left)//2
        if a[mid]==m:
            return mid
        if a[mid]>m:
            right=mid
        if a[mid]<m:
            left=mid
        (a.sort())
        print(a)
        return mid
    
a=Alogarithim()
print(a.search([1,4,8,7,52,36,97,45,61,25,48,1,2,3,5,4,8,71,9,0,9],int(input('enter your number '))))

