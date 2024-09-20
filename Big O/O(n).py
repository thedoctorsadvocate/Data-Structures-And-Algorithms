def finder(items: list[int], target: int) -> None:
    counter = 0
    for item in items:
        counter += 1
        if item == target:
            print(f'Target has been found: {item}')
    
    print(f'Algorithm took {counter} iterations to complete.\nThis is linear, meaning the more inputs in the list, the more iterations will be needed to complete the function. The number grows linearly')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 8
finder(l, t)