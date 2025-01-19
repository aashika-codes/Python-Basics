class dog:
    species="Dog"
    def __init__(self,name,age,colour,breed):
        self.name=name
        self.age=age
        self.colour=colour
        self.breed=breed
Ryugen=dog("Ryugen",9,"white","Poodle")
Benji=dog("Benji",21,"brown","Golden Retriever")
print("Ryugen is a {} and he is a {}".format(Ryugen.species,Ryugen.breed))
print("Woo is also a {} and he is a {}".format(Benji.species,Benji.breed))
print("{} is {} years old and he is {} in colour".format(Ryugen.name,Ryugen.age,Ryugen.colour))
print("{} is {} years old and he is {} in colour".format(Benji.name,Benji.age,Benji.colour))