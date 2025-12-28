#creamos una clase, con atributos de clase y de instancia 
#ademas creamos metodos de clase e instancia 

class CuentaBancaria:
    titular = ""
    saldo = 0 
    total_cuentas = 0 
    saldo_total = 0

    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo 

        print("Cuenta creada para: ", self.titular)

        #con esto llevo la cuenta cada vez que creo una instancia 
        CuentaBancaria.total_cuentas+= 1 
        CuentaBancaria.saldo_total += saldo

    
    def depositar(self,deposito):
        self.saldo = self.saldo + deposito
        CuentaBancaria.saldo_total += deposito

    def retirar(self,retiro):
        if self.saldo - retiro < 0:
            print("Error, saldo insuficiente!")
        else:
            self.saldo-= retiro 
            CuentaBancaria.saldo_total -= retiro
    
    def consultar_saldo():
        print("El saldo en su cuenta es: ", self.saldo)

    @classmethod
    #esto es un decorador, que convierte una funcion normal en un metodo de clase 
    #le dice a python que al usar este metodo debe pasarle como argumento 
    #la clase 
    #se usa cuadno el metodo no depende de una instancia y  
    #trabaja con datos de la clase 
    def informe_banco():
        print("El numero total de cuentas es: ", CuentaBancaria.total_cuentas)
        print("El saldo acumulado es de: ", CuentaBancaria.saldo_total )

    #el metodo de clase se puede escribir como 
    #informe_banco(cls) y en los atributos poner 
    #cls.total_cuentas y cls.saldo_total 

    #funciona igual escrito de ambas formas, solo que usar cls es mas seguro
    #por si despues deseo heredar de esta clase 
    #asi el metodo no queda acoplado a esa clase especifica si no que 
    #se puede usar con cualquiera que herede desde CuentaBancaria 

    #ideam, si quiero hacer herencias 
    #usar @classmethod 
    #si lo uso, al llamar al metodo desde una clase hija, el metodo 
    #sabe que tiene q usar al clase hija 
    #sin ponerle classmethod, el metodo ignora a la clase hija y usa a al clase padre 


#===============

c1 = CuentaBancaria("Dani", 2000)
c2 = CuentaBancaria("Raulito", 5000)
c3 = CuentaBancaria("Funado", 1000)

c1.depositar(1000)
c2.retirar(3000)

CuentaBancaria.informe_banco()


c2.retirar(10000)
c3.depositar(5000)
CuentaBancaria.informe_banco()
