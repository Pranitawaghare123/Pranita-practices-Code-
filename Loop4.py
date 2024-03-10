numbers = [12, 75, 150, 180, 145, 525, 50]
for items in numbers:
    if items%5==0:
        if items>150:
            continue
        if 500>=items :
             break
        print(items)