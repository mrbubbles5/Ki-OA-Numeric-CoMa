#CoMa1 WS2020
#f(x) = ax² + bx + c
#g(x) = dx² + ex + f
#h(x) = x^5
#h+g*f = c_5*x^5 + c_4*x^4 + c_3*x^3 + c_2*x^2 + c_1*x^1 + c_0*x^0
def roots(a=int,b=int,c=int,d=int,e=int,f=int):
    #the function calculates the coefficients, puts them into a list and
    #counts if there is a switch between positive and negative Elements
    #if a switch mod 2 = 0 is found, the function will return the given
    #message aboout the roots
    #in the other case the output is equivalent
    c_0 = c * f
    c_1 = b*f + c*d 
    c_2 = a*f + b*e + c*d
    c_3 = a*e + b*d
    c_4 = a*d
    
    coeff = [c_0, c_1, c_2, c_3, c_4]
    
    switches = 0
    
    current = 1
    
    for i in coeff:
        if (i < 0 and current > 0) or (i > 0 and current < 0):
            
            current = i
            switches += 1
    
    if switches % 2 == 0:
        return "Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln."
    else:
        return "Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln."
