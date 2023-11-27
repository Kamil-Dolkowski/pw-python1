import re

text = "To nie jest nieodpowiedni tekst, dla tego zadania."

x = re.findall("nie", text)
print(x)

x = re.search("^To.*zadania.$",text)
print(x)

x = re.split("\s",text)
print(x)

x = re.sub("nie","_",text)
print(x)

x = re.sub("\s","_", text)
print(x)

x = re.findall(r'\bnie\b',text)
print(x)

x = re.findall(",",text)
print(x)

x = re.findall(r"[\w\.]+[\w\,]+",text)
print(x)

x = re.findall(r"\b[n]\w+",text)
print(x)



mail = "jakub.chmielak@pw.edu.pl"

x = re.split("@",mail)
print(x)


x = re.search("^[\w\.]+@[\w\.]+$", mail)
print(x)

x = re.match("^[\w\.]+@[\w\.]+$", mail)
print(x)
print(bool(x))



txt = "Rok 2023 będzie lepszy."

x = re.sub("\d","X",txt)
print(x)




kot = "Nasz kot ma 60 lat i waży 4 kg."

x = re.findall(r"\d+",kot)
print(x)

x = re.search("^nasz",kot,re.IGNORECASE)
print(x)




tel = "Mój numer to 623-456-7890."

x = re.findall(r"\d{3}-\d{3}-\d{3}",tel)
print(x)

x = re.search(r"\d{3}-\d{3}-\d{3}\b",tel)
print(x)

