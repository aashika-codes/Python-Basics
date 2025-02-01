class india():
    def capital(self):
        print("The capital of india is New Delhi")
    def language(self):
        print("Hindi is the most spoken language of india")
    def type(self):
        print("India is a developing country")
class usa():
    def capital(self):
        print("Washington D.C is the capital of USA")
    def language(self):
        print("English is the most spoken language in USA.")
    def type(self):
        print("USA is a developed country")
objindia=india()
objusa=usa()
for country in (objindia,objusa):
    country.capital()
    country.language()
    country.type()