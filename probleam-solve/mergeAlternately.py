class Solution:
    def mergeAlternately(self,word1:str,word2:str)->str:
        list1=[] 
        list=[]
        if len(word1)==len(word2):
            for v,b in zip(word1,word2):
                list1.append(v)
                list1.append(b)
        else:
            if len(word1)>len(word2):
                t_len=len(word1)-len(word2)
                for i in range(1,t_len+1):
                    list.append(word1[-i])
                (list.reverse())
                join_thing=''.join(list)
                equal_word1=(word1.removesuffix(''.join(list)))
                for v,b in zip(equal_word1,word2):
                    list1.append(v)
                    list1.append(b)
                list1.append(join_thing)       
            else:
                t_len=len(word2)-len(word1)
                for i in range(1,t_len+1):
                    list.append(word2[-i])
                (list.reverse())
                join_thing=''.join(list)
                equal_word2=(word2.removesuffix(''.join(list)))
                for v,b in zip(word1,equal_word2):
                    list1.append(v)
                    list1.append(b)
                list1.append(join_thing)
        return str(''.join(list1))
        
S=Solution()
