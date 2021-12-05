primes = [2, 3, 5, 7] #Primes the computer knows

def main():

    while True: #Makes sure an integer between 2 and 49 is entered
        try: 
            test_number = int(input("Enter an integer between 2 and 49. "))
            if 2 <= test_number <= 49:
                break
            else:
                print("Entry was not between 2 and 49.")
        except ValueError:
            print("Entry was not an integer.")

    if test_number in primes: #Prime if in prime list
        print("Prime!")
        return

    for i in primes: #Checks against ever prime up to swrt of 49
        if (test_number % i) == 0:
            print("Not prime!")
            break
        if i == 7:
            print("Prime!")
            break
        
while True: #Keeps asking for another number
    main()
