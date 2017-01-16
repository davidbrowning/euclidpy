def is_prime(n):
    if(n <= 1):
        print('false');
        return False;
    elif(n <= 3):
        print('true');
        return True;
    elif(n % 2 == 0 or n % 3 == 0):
        print('false');
        return False;
    i = 5;
    while(i * i <= n):
        if (n%i == 0 | n % (i+2) == 0):
            print('false');
            return False;
        i = i + 6;
    print('true');
    return True;

is_prime(7);
is_prime(9);
is_prime(10);
