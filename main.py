history=[]
while True:
    print("Choose an option:")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Multiply Two Numbers")
    print("4. Divide Two Numbers")
    print("5. Print History")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter The Numbers to Add Seperated By Space: ")
            numbers = input()
            numbers = numbers.strip()
            numbers_seperated = numbers.split(' ')
            summ = 0.0
            history_element = " "
            for number in numbers_seperated:
                history_element = history_element+number+' + '
                number = float(number)
                summ = summ+number
            #history_element = history_element.replace(history_element[-1] , ' = ')
            history_element = history_element[:-1] + " = " + str(summ)
            history.append(history_element)
            print('The Sum of Numbers is ', summ)
            print("********")

        case 2:
            print("Enter The Numbers to Subtract Seperated By Space: ")
            numbers = input()
            numbers=numbers.strip()
            numbers_seperated = numbers.split(' ')
            subtraction = float(numbers_seperated[0])
            history_element = " "
            for number in numbers_seperated[1:]:
                history_element = history_element + number + ' - '
                number = float(number)
                subtraction = subtraction-number
            history_element = history_element[:-1] + " = " + str(subtraction)
            history.append(history_element)
            print('The Subtraction of Numbers is ', subtraction)
            print("********")

        case 3:
            print("Enter The Two Numbers to Multiply Seperated By Space: ")
            numbers = input()
            numbers_seperated = numbers.split(' ')

            multiplication = float(numbers_seperated[0]) * float(numbers_seperated[1])
            history_element = " "+numbers_seperated[0] + " * " + numbers_seperated[1] + " = " + str(multiplication)

            history.append(history_element)
            print('The Multiplication of Numbers is ', multiplication)
            print("********")

        case 4:
            print("Enter The Two Numbers to Divide Seperated")
            numbers = input()
            numbers_seperated = numbers.split(' ')
            if int(numbers_seperated[1]) == 0:
                print("Cannot Divide Zero")
            else:
                division = float(numbers_seperated[0]) / float(numbers_seperated[1])
                history_element = " "+numbers_seperated[0] + " / " + numbers_seperated[1] + " = " + str(division)
                history.append(history_element)
                print('The Division of Numbers is ', division)
                print("********")
        case 5:
            print("Histroy : ")
            for element in history:
                print(element)
                print(" ")
        case 6:
            exit()


