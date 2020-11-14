def argumenty(tab):
    def internal(function):
        def oper(*args):
            if function.__name__ == "suma":
                if len(args) == 4:
                    function(args[1], args[2], args[3])
                elif len(args) == 3:
                    function(args[1], args[2], tab[0])
                elif len(args) == 2:
                    function(args[1], tab[0], tab[1])
                else:
                    raise TypeError("suma() takes exactly 3 arguments (2 given)")


            if function.__name__ == "roznica":
                if len(args) == 3:
                    function(args[1], args[2])
                    return tab[0]
                elif len(args) == 2:
                    function(args[1], tab[0])
                    return tab[1]
                elif len(args) == 1:
                    function(tab[0], tab[1])
                    return tab[2]
        return oper
    return internal

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(a,b,c):
        print ("%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(x,y):
        print ("%d-%d=%d" % (x,y,x-y))

    def __setitem__(self,key,value):
        if key == 'suma':
            Operacje.argumentySuma = value
        elif key == 'roznica':
            Operacje.argumentyRoznica = value


