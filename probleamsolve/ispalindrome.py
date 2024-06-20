# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         res = ""
#         for i in s:
#             if i.isalnum():
#                 res=res+i
#         res = res.lower()
#         return res == res[::-1]
    
    



class Solution:
    def isPalindrome(self,s:str)->bool:
        res=''
        for i in s:
            if  i.isalnum():
                res=res+i
            res=res.lower()
            return res==res[::-1]
s=Solution()
print(s.isPalindrome("A man, a plan, a cameo, Zena, Bird, Mocha, Prowel, a rave, Uganda, Wait, a lobola, Argo, Goto, Koser, Ihab, Udall, a revocation, Ebarta, Muscat, eyes, Rehm, a cession, Udella, E-boat, OAS, a mirage, IPBM, a caress, Etam, FCA, a mica, Ojai, Lebowa, Yaeger, a barge, Rab, Alsatian, a mod, Adv, a rps, Ileane, Valeta, Grenada, Hetty, Fayme, REME, HCM, Tsan, Owena, Tamar, Yompur, Isa, Nil, Lorrin, Riksdag, Mona, Ronn, O'Conner, Kirk, an okay, Nafl, Lira, Robi, Rame, FIFA, a need, Rodi, Muharram, Ober, a coma, carri, Hwang, Taos, Salado, Olfe, Camag, Kdar, a hdkf, Jemina, Nadler, Ehud, Rutan, a baster, Ebn, aedegi, a gals, Ira, Tepper, a minim, a gowd, Ulda, Ogawa, TSgt, Callida, Rodl, Ewart, seraphs, Ain, Newgate, Vaden, navettes, Sabah, Swat, Luci, Pam, Arda, pools, a boar, Akira, Gally, CSC, Avalon, a tuba, AAM, Artima, AFB, Selah, wellies, Ronald, BArch, nullos, Uni, an aet, Nadabus, Tyree, Poop, Sennar, CAB, a nanny, Let, Efahan, Dasya, Moon, Ikaria, Nam, Lamar, Egor, Rover, Tanana, Lok..."))
    

# s= 'Lok...'
# list1=[]
# for i in s:
#     if i.isalpha():
#         list1.append(i.lower())
# join1=''.join(list1)
# print(list1)
# print(join1)
# list1.reverse()
# print(list1)
# print(''.join(list1))
