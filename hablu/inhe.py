

class BAbA:
    car="BMW"
    mobile="i phone"
    taka=5000000
    
class Ma:
    property=200000
    land='2 hector'
    
class KaKA: # Kakar sontan nai #
    car='motor cycle'  
    land='2 biga'
    
class CHILD(BAbA,Ma,KaKA):
    None
    
C=CHILD()
C.property=C.property+C.taka
print(C.property)