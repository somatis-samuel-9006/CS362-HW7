def fizzbuzz():
    fizz_string = ""
    for i in range(1,101):
        if(i % 3 == 0) and (i % 5 == 0):
           fizz_string = fizz_string + " fizzbuzz"
        elif(i % 3 == 0):
            fizz_string = fizz_string + " fizz"
        elif(i % 5 == 0):
            fizz_string = fizz_string + " buzz"
        else:
            str_i = str(i)
            fizz_string = fizz_string + " " + str_i
    return fizz_string

fizzbuzz()

