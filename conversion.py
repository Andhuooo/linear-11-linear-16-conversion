def fullfun()
    import math

    def compliment(val):

        if val[0] == "1":
          dict={"0":"1","1":"0"}
          a =''.join(dict[x] for x in val)
          ##print(a)
          b = "1"
          binary_sum = lambda a,b : bin(int(a, 2) + int(b, 2))
          out = binary_sum(a,b)[2:] 
          exp = int(out, 2)
          #print(exponent)
          comp = exp* -1
          return comp
        else:
          comp = int(val, 2)
          return comp
    def linear11():
        f = open('path of txt file where the linear 11 value saved in str format')
        string = f.read()
        hexval =  string[2:]
        res = "{0:016b}".format(int(hexval, 16))
        exp = ""
        for index in range(5):
          
          exp += (res[index])
        mant = ""
        for index in range(5, 16):
          
          mant += (res[index])
        #print(mant)
        mantdec = compliment(mant)
        exponent = compliment(exp)
        x = mantdec * pow(2, exponent)
        return x
    #print ('The linear 11 converted value is : ', linear11() )

    def linear16():
        expl16 = -9
        f = open('path of txt file where the linear 16 value saved in str format')
        string = f.read()
        hexval =  string[2:]  
        res = "{0:016b}".format(int(hexval, 16)) 
        print (res) 
        mantl16 = compliment(res)
        x = mantl16 * pow(2, expl16)
        return x
    print ('The linear 11 converted value is : ', linear16() )
return True
