def multiply(list1, list2):
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            result.append(list1[i] * list2[j])
    return result

#input multiplication 

list1 = [631042796123702335066700534619845449206964597506533516098361]
list2 = [397947695810425487466494958255617656357136036376512433634409]

print(multiply(list1, list2))