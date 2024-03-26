#REGULAR EXPRESION
import re 
#var="anything"
#*rules=(re.search("any",var))
# rules.group()
# re.findall(r"condition",var)
# re.split(r"\w+","multiple word here")

a="cv6v82v5"
p=(re.split(r"[6-8]+",a ,flags=re.IGNORECASE))
print("".join(p))
#*LINEAR SEARCH