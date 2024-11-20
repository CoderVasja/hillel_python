
def sum_from_string(*args):

    for i in (args):
    
        try:
            numbers = map(int, i.replace(" ", "").split(","))
            print(f"Сумма для '{i}':-> {sum(numbers)}")
    
        except ValueError:
            print (f'Не можу це зробити для елемента ({i}) бо тут є букви')

sum_from_string('1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3')