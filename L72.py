#Rosemary and Emily
#B
def number_of_os(word):
    total=0
    for n in word:
        if n=="o":
            total=total+1

    print(total)


number_of_os("common")
number_of_os("bonbon")
