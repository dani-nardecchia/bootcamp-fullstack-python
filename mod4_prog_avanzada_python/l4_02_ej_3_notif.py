class Notificacion():
    def __init__(self, destinatario, mensaje, fecha_envio, prioridad):
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio
        if prioridad in ["baja", "media", "alta"]:
            self.priodidad = prioridad
        else:
            self.prioridad = "baja"
    
    #•enviar(): imprime "Enviando notificación básica"
    def enviar(self):
        print ("Enviando notificacion básica")
    
    #validar(): devuelve True si destinatario no está vacío
    def validar(self):
        if self.destinatario == "":
            return False
        else:
            return True
    
    #obtener_tipo(): devuelve "Notificación genérica"
    def obtener_tipo(self):
        return "Notificacion genérica"
    
    #formatear_mensaje(): devuelve el mensaje en mayúsculas
    def formatear_mensaje(self):
        return self.mensaje.upper()

class Email(Notificacion):
    def __init__(self, destinatario, mensaje, fecha_envio, prioridad, asunto, remitente, adjuntos):
        super().__init__(destinatario, mensaje, fecha_envio, prioridad)
        self.asunto = asunto
        self.remitente = remitente
        self.adjuntos = adjuntos
    
    #enviar(): sobrescribe - imprime "📧 Enviando EMAIL a [destinatario]"
    def enviar(self):
        print(f"Enviando Email a {self.destinatario}.")

    #obtener_tipo(): sobrescribe - devuelve "Email"
    def obtener_tipo(self):
        return "Email"
    
    #agregar_adjunto(archivo): método propio
    def agregar_adjunto(self,archivo):
        self.adjuntos.append(archivo)

    #formatear_mensaje(): sobrescribe - añade "Estimado/a," al inicio
    def formatear_mensaje(self):
        self.mensaje = "Estimado/a," + self.mensaje

class SMS(Notificacion):
    def __init__(self,destinatario, mensaje, fecha_envio, prioridad, numero_telefono, operadora):
        super().__init__(destinatario, mensaje, fecha_envio, prioridad)
        self.numero_telefono = numero_telefono
        self.operadora = operadora
    
    #enviar(): sobrescribe - imprime "📧 Enviando SMS al [numero_telefono]"
    def enviar(self):
        print(f"Enviando SMS al {self.numero_telefono}")
    
    #obtener_tipo(): sobrescribe - devuelve "SMS"
    def obtener_tipo(self):
        return "SMS"
    
    #validar(): sobrescribe - valida que el número tenga 8 dígitos
    def validar(self):
        if self.numero_telefono.len() == 8:
            return True 
        else:
            False 

    #acortar_mensaje(): si mensaje > 160 chars, lo corta
    def acortar_mensaje(self):
        if self.mensaje.len() > 160:
            return self.mensaje[:160] 
    
    class Push(Notificacion):
        def __init__(self,destinatario, mensaje, fecha_envio, prioridad, dispositivo,icono):
            super().__init__(destinatario, mensaje, fecha_envio, prioridad)
            self.dispositivo = dispositivo
            self.icono = icono
        

        
            