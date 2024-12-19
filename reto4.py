#entrante maindish bebidas porciones postres armar menu mostrar
class MenuItem:
    def __init__(self,nombre:str,precio:int,tipo:str):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __repr__(self):
        return str(self.__dict__)      

    def set_nombre(self,nombre:str):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    def set_tipo(self,tipo:str):
        self.tipo=tipo
    def get_tipo(self):
        return self.tipo
    def set_precio(self,precio:float):
        self.precio=precio
    def get_precio(self):
        return self.precio
    
class MainDish(MenuItem):
    def __init__(self, nombre, precio, tipo="Main Dish"):
        super().__init__(nombre, precio, tipo)

    def __repr__(self):
        return str(self.__dict__)                                            

class Drinks(MenuItem):
    def __init__(self, nombre, precio, tipo="Drinks"):
        super().__init__(nombre, precio, tipo)

    def __repr__(self):
        return str(self.__dict__)                                            

class Startes(MenuItem):
    def __init__(self, nombre, precio, tipo="Starters"):
        super().__init__(nombre, precio, tipo)

    def __repr__(self):
        return str(self.__dict__)                                            

class Sides(MenuItem):
    def __init__(self, nombre, precio,tipo="sides"):
        super().__init__(nombre, precio, tipo)

    def __repr__(self):
        return str(self.__dict__)

class Desserts(MenuItem):
    def __init__(self, nombre, precio, tipo="Dessserts"):
        super().__init__(nombre, precio, tipo)

    def __repr__(self):
        return str(self.__dict__)

class Order:
    def __init__(self):
        self.order:list=[]
        #self.menuitem=MenuItem()

    def add_item(self,o:MenuItem):
        self.order.append(o)

    def compute_price(self):
        x={}
        for i in self.order:
            if i.get_tipo() not in x:
                #x.update(i.tipo,1)
                x[i.get_tipo()]=1
            else:
                #x.update(i.tipo,(x.get(i.tipo)+1))
                x[i.get_tipo()]=x.get(i.get_tipo())+1
        if "Main Dish" not in x:
            #x.update("Main Dish",0)
            x["Main Dish"]=0
        if "Drinks" not in x:
            #x.update("Drinks",0)
            x["Drinks"]=0
        if "Dessserts" not in x:
            #x.update("Drinks",0)
            x["Dessserts"]=0

        descount:int=0
        if x.get("Main Dish")>=1 and x.get("Drinks")>=1:
            a=min(x.get("Main Dish"),x.get("Drinks"))
            b=0
            for i in self.order:
                if  i.get_tipo() =="Drinks" and b<a:
                    descount+=i.get_precio()
                    #i.set_precio(0)   
                    b+=1
        if x.get("Main Dish")>=1 and x.get("Dessserts")>=1:
            a=min(x.get("Main Dish"),x.get("Dessserts"))
            b=0
            for i in self.order:
                if  i.get_tipo()  =="Dessserts" and b<a:
                    descount+=int(i.get_precio()*0.4)
                    #i.set_precio(int(i.get_precio()*0.6))
                    b+=1

        pricetotal:int=0
        for i in self.order:
            pricetotal+=i.get_precio()
        return [pricetotal,descount]
    
    def ver_recibo(self):
        print("{:<30} {:>6} ".format("Pedido", "Precio"))
        print("{:<30} {:>6} ".format("------------------------------", "--------"))
        for i in self.order:
            #print(i.nombre,"\t",i.precio)
            print("{:<30} {:>6}".format(i.get_nombre(), i.get_precio()))
        #print("Total \t",self.compute_price())
        e=self.compute_price()
        #print(e)
        print("{:<30} {:>6}".format("Total Completo", e[0]))
        print("{:<30} {:>6}".format("Descuento", -1*e[1]))
        print("{:<30} {:>6}".format("Total", e[0]-e[1]))
    
    def get_item(self,item:int):
        return self.order[item]
    
    def drop_item(self,item:int):
        self.order.pop(item)

    def __repr__(self):
        return str(self.__dict__)

class Payment:
  def __init__(self):
    pass

  def pagar(self, monto):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(Payment):
  def __init__(self, numero, cvv):
    super().__init__()
    self.numero = numero
    self.cvv = cvv

  def pagar(self, bill:Order):
    a=bill.compute_price()
    monto=a[0]-a[1]
    print(f"Pagando {monto} con tarjeta {self.numero[-4:]}")

class Efectivo(Payment):
  def __init__(self, monto_entregado):
    super().__init__()
    self.monto_entregado = monto_entregado

  def pagar(self, bill:Order):
    a=bill.compute_price()
    monto=a[0]-a[1]
    if self.monto_entregado >= monto:
      print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
    else:
      print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")





si1=Sides("Porcion papas a la francesa",6000)
si2=Sides("yuca frita",7000)
si3=Sides("Porcion papas a la francesa",6000)
m1=MainDish("Bandeja de carne",25000)
m2=MainDish("Bandeja de pollo",23000)
de1=Desserts("Copa de Helado",12000)
de2=Desserts("Tiramisu",9000)
d1=Drinks("Gaseosa Manzana",3000)
d2=Drinks("Gaseosa Coca Cola",3000)
d3=Drinks("Malteada",8000)
s1=Startes("Nuggets",10000)
o1=Order()
o1.add_item(si1)
o1.add_item(si2)
o1.add_item(si3)
o1.add_item(m1)
o1.add_item(m2)
o1.add_item(d1)
o1.add_item(d2)
o1.add_item(de1)
o1.add_item(de2)
o1.add_item(s1)
print(o1.ver_recibo())
#print(o1.compute_price())

pago1 = Tarjeta("1234567890123456", 123)
pago2 = Efectivo(100000)

pago1.pagar(o1)
pago2.pagar(o1)
#print(o1.ver_recibo())
#Descuento = por cada combo maindish + drink, drink es gratis o por cada postre con un maindish postre al 60%
#print(o1)
#print(o1.compute_price())
