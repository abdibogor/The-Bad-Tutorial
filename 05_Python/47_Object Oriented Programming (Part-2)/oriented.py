class myclass:
    sample=0
    w=0
    b=0
    g=0
    o=o
    color_list=['black','white','gray']
    def __init__(self, name):
                           myclass.name=name
                           print("What's the color of your car?")
                           myclass.color=input()
                            myclass.sample=myclass.sample+1
                    def check_color(self):
                            if myclass.color in myclass.color_list:
                                if myclass.color==myclass.color_list[0]:
                                    myclass.b=myclass.b+1
                                elif myclass.color==myclass.color_list[1]:
                                        myclass.w=myclass.w+1
                                else:
                                        myclass.g=myclass.g+1
                                else:
                                        myclass.o=myclass.o+1
                        def display_result(self):
                            print("Hello", myclass.name)
                            print("Total number of black cars:", myclass.b)
                            print("Total number of white cars:", myclass.w)
                            print("Total number of gray cars:", myclass.g)
                            print("Other:", myclass.o)
                            print("sample Size:", myclass.sample)
                var=0
                names=['Roger',  'Rafa', 'Andy',  'Novak']
                mylist=[]
                while var<4:
                    mylist.append(myclass(names[var]))
                    mylist[var].check_color()
                    mylist[var].display_result()
                    var=var+1
                myobj=myclass("John")
                myobj.check_color()
                myobj.display_result()
                myobj=myclass("Roger")
                myobj.check_color()
                myobj.display_result()
