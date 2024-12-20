import  math as ma

def frange2(start, stop, step):#for con float
    n_items = int(ma.ceil((stop - start) / step))
    return [redu_deci(start + i*step )  for i in range(n_items+1)]

def redu_deci(a:float): #Reducir decimales a maxima 3 cifras significativas
    return round(int(a*1000)/1000,2)


class Point:
    def __init__(self,x:float,y:float):
        self.__x=x
        self.__y=y

    def get_x(self):
        return self.__x
    def set_x(self,x:float):
        self.__x=x 
    def get_y(self):
        return self.__y
    def set_y(self,y:float):
        self.__y=y
    
    def __repr__(self):
        return "("+str(self.__x)+","+str(self.__y)+")"


class Line:
    def __init__(self, start:Point, end:Point):
        self.__start=start
        self.__end=end
        self.__length:float
        self.__slope:float
        self.__discretized_line:list

    def get_start(self):
        return self.__start
    def set_start(self,start:Point):
        self.__start=start

    def get_end(self):
        return self.__end
    def set_end(self,end:Point):
        self.__end=end

    def get_length(self):
        return self.__length
    def set_length(self,length:float):
        self.__length=length

    def get_slope(self):
        return self.__slope
    def set_slope(self,slope:float):
        self.__slope=slope

    def get_discretized_line(self):
        return self.__discretized_line
    
    def compute_length(self):
        self.__length=ma.sqrt((self.__end.get_x()-self.__start.get_x())**2+(self.__end.get_y()-self.__start.get_y())**2)
        return self.__length
    
    def compute_slope(self):
        self.__slope=ma.degrees(ma.atan((self.__end.get_y()-self.__start.get_y())/(self.__end.get_x()-self.__start.get_x())))
        return self.__slope

    def compute_horizontal_cross(self):
        if (self.__start.get_y()<=0<=self.__end.get_y() or self.__start.get_y()>=0>=self.__end.get_y()):
            return True
        else:
            return False
        
    def compute_vertical_cross(self):
        if (self.__start.get_x()<=0<=self.__end.get_x() or self.__start.get_x()>=0>=self.__end.get_x()):
            return True
        else:
            return False
        
    def discretize_line(self,com:Point=None):# list,bool
        m:float=0
        b:float=0
        if self.__end.get_x()!=self.__start.get_x():
            m=(self.__end.get_y()-self.__start.get_y())/(self.__end.get_x()-self.__start.get_x())
            b=(self.__end.get_y()-m*self.__end.get_x())
            N=[]
            H=frange2(self.__start.get_x(),self.__end.get_x(),0.05)
            for i in H:
                a=Point( i, redu_deci(m*i + b ))
                N.append(a)
            self.__discretized_line=N
        else :
            N=[]
            H=frange2(self.__start.get_y(),self.__end.get_y(),0.05)
            for i in H:
                a=Point( self.__start.get_x(),i )
                N.append(a)
            self.__discretized_line=N
            
        if com==None:
            return self.__discretized_line
        elif com.get_x()==self.__start.get_x()  and self.__end.get_x()==self.__start.get_x() and com.get_y() in range(self.__start.get_y(),self.__end.get_y()+1):
            return True
        elif com.get_y()!=m*com.get_x()+b and com.get_x() in range(self.__start.get_x(),self.__end.get_y()+1) and self.__end.get_x()!=self.__start.get_x():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return "("+str(self.__start)+","+str(self.__end)+")"
    
class Shape:
    def __init__(self) :
        self.__is_regular:bool
        self.__vertices:list=None
        self.__edges:list=None
        self.__inner_angles:list

    def set_is_regular(self,is_regular:bool):
        self.__is_regular=is_regular
    def get_is_regular(self):
        return self.__is_regular
    
    def set_vertices(self,vertices:list):
        self.__vertices=vertices
    def get_vertices(self):
        if self.__vertices==None:
            self.corregir()
        return self.__vertices
    
    def set_edges(self,edges:list):
        self.__edges=edges
    def get_edges(self):
        if self.__edges==None:
            self.corregir()
        return self.__edges
    
    def set_inner_angles(self,inner_angles:list):
        self.__inner_angles=inner_angles
    def get_inner_angles(self):
        return self.__inner_angles
        
    def corregir(self):
        if self.__edges==None and self.__vertices!=None:
            B=[]
            C=self.__vertices
            B.append(Line(C[0],C[1]))
            B.append(Line(C[1],C[2]))
            B.append(Line(C[2],C[3]))
            B.append(Line(C[3],C[0]))
            self.set_edges(B)
        elif self.__edges!=None and self.__vertices==None:
            B=[]
            C=self.__edges
            for i in C:
                B.append(i.get_start())

            self.set_vertices(B)

    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.set_is_regular(False)
        self.set_inner_angles([90,90,90,90])


    def compute_area(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            if i not in A:
                A.append(i.compute_length())
        return A[0]*A[1]
        
    def compute_perimeter(self):
        self.corregir()
        A=0
        for i in self.get_edges():
           A+=i.compute_length()
        return A

    def __repr__(self):
        return str(self.__dict__)
    
class Square(Rectangle):
    def __init__(self):
        super().__init__()
        self.set_is_regular(True)
        
    def compute_area(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            if i not in A:
                A.append(i.compute_length())
        return A[0]**2
        
    def compute_perimeter(self):
        self.corregir()
        A=0
        for i in self.get_edges():
           A+=i.compute_length()
        return A

    def __repr__(self):
        return str(self.__dict__)

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()
        self.set_is_regular(False)

    def compute_area(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        a,b=0,0
        if A.count(A[0])==1:
            b=A[0]
            a=A[1]
        elif  A.count(A[1])==1:
            b=A[1]
            a=A[0]
        elif  A.count(A[2])==1:
            b=A[2]
            a=A[0]
        
        return redu_deci(0.5*b*(a**2 - (b**2)/4)**(1/2))

    def compute_perimeter(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        return redu_deci(A[0]+A[1]+A[2])
    
    def compute_inner_angles(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        a,b=0,0
        if A.count(A[0])==1:
            b=A[0]
            a=A[1]
        elif  A.count(A[1])==1:
            b=A[1]
            a=A[0]
        elif  A.count(A[2])==1:
            b=A[2]
            a=A[0]

        c=redu_deci(ma.degrees(ma.acos(b/(2*a))))
        d=180-2*c
        C=[c,d,c]
        return C 
    
class Equilateral(Triangle):
    def __init__(self):
        super().__init__()
        self.set_is_regular(True)

    def compute_area(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            if i not in A:
                A.append(i.compute_length())
        a=redu_deci(((3**(1/2))/4 )*A[0]**2)
        return a

    def compute_perimeter(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        return redu_deci(A[0]*3)
    
    def compute_inner_angles(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())

        c=redu_deci(ma.degrees(ma.acos(A[0]/(2*A[0]))))
        d=180-2*c
        C=[c,d,c]
        return C 

class Scalene(Triangle):
    def __init__(self):
        super().__init__()
        self.set_is_regular(False)

    def compute_area(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        s=(A[0]+A[1]+A[2])/2
        a=(s*(s-A[0])*(s-A[1])*(s-A[2]))**(1/2)
        return redu_deci(a)

    def compute_perimeter(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        return redu_deci(A[0]+A[1]+A[2])
    
    def compute_inner_angles(self):
        self.corregir()
        A,C=[],[]
        for i in self.get_edges():
            A.append(i.compute_length())

        s=A[0]**2-A[1]**2-A[2]**2
        C.append(redu_deci(ma.degrees(ma.acos(-(A[0]**2-A[1]**2-A[2]**2)/(2*A[1]*A[2])))))
        C.append(redu_deci(ma.degrees(ma.acos(-(-A[0]**2+A[1]**2-A[2]**2)/(2*A[0]*A[2])))))
        C.append(redu_deci(ma.degrees(ma.acos(-(-A[0]**2-A[1]**2+A[2]**2)/(2*A[0]*A[1])))))
        
        return C 
        
class TriRectangle(Triangle):
    def __init__(self):
        super().__init__()
        self.set_is_regular(False)

    def compute_area(self):
        self.corregir()
        s=self.get_edges()
        b,h=0,0
        for i in s:
            if i.get_start().get_y()==i.get_end().get_y():
                b=i.compute_length()
            if i.get_start().get_x()==i.get_end().get_x():
                h=i.compute_length()
        return redu_deci(b*h*0.5)

    def compute_perimeter(self):
        self.corregir()
        A=[]
        for i in self.get_edges():
            A.append(i.compute_length())
        return redu_deci(A[0]+A[1]+A[2])
    
    def compute_inner_angles(self):
        self.corregir()
        A,C=[],[]
        for i in self.get_edges():
            A.append(i.compute_length())

        C.append(redu_deci(ma.degrees(ma.acos(-(A[0]**2-A[1]**2-A[2]**2)/(2*A[1]*A[2])))))
        C.append(redu_deci(ma.degrees(ma.acos(-(-A[0]**2+A[1]**2-A[2]**2)/(2*A[0]*A[2])))))
        C.append(redu_deci(ma.degrees(ma.acos(-(-A[0]**2-A[1]**2+A[2]**2)/(2*A[0]*A[1])))))
        return C 


b=Rectangle()
b.set_edges([Line(Point(0,0),Point(0,3)),Line(Point(0,3),Point(4,3)),Line(Point(4,3),Point(4,0)),Line(Point(4,0),Point(0,0))])
print(b.compute_area(),b.compute_perimeter(),b.get_is_regular())
print(b.get_vertices(),"\n")

c=Square()
c.set_vertices([Point(0,0),Point(0,3),Point(3,3),Point(3,0)])
print(c.compute_area(),c.compute_perimeter())
print(c.get_edges(),c.get_is_regular(),"\n")


a=Isosceles()
a.set_edges([Line(Point(0,0),Point(2,3)),Line(Point(2,3),Point(4,0)),Line(Point(4,0),Point(0,0))])
print(a.compute_area(), a.compute_perimeter(),a.get_is_regular(),a.compute_inner_angles(),"\n")

d=Equilateral()
d.set_edges([Line(Point(0,0),Point(2,ma.sqrt(12))),Line(Point(2,ma.sqrt(12)),Point(4,0)),Line(Point(4,0),Point(0,0))])
print(d.compute_area(), d.compute_perimeter(),d.get_is_regular(),d.compute_inner_angles(),"\n")

e=Scalene()
e.set_edges([Line(Point(0,0),Point(2,2)),Line(Point(2,2),Point(5,0)),Line(Point(5,0),Point(0,0))])
print(e.compute_area(), e.compute_perimeter(),e.get_is_regular(),e.compute_inner_angles(),"\n")

f=TriRectangle()
f.set_edges([Line(Point(0,0),Point(0,4)),Line(Point(0,4),Point(5,0)),Line(Point(5,0),Point(0,0))])
print(f.compute_area(), f.compute_perimeter(),f.get_is_regular(),f.compute_inner_angles(),"\n")