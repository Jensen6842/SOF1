def main():

    while True: #Makes sure an integer between 2 and 49 is entered
        try: 
            test_number = int(input("Enter an integer above 1. "))
            if test_number == 1:
                print("Entry was not above 1")
            else:
                break
        except ValueError:
            print("Entry was not an integer.")

    if test_number == 2:
        print("Prime!")
        return

    for i in [2, round(pow(test_number, 0.5))]: #Checks against ever prime up to swrt of test_number
        if (test_number % i) == 0:
            print("Not prime!")
            break
        if i == round(pow(test_number, 0.5)):
            print("Prime!")
            break
        
while True: #Keeps asking for another number
    main()
