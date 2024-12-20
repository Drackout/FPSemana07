
class Mensagem:
    def __init__(self):
        pass

class Email(Mensagem):
    def __init__(self, destinatario, assunto, corpo):
        #super().__init__()
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo

    def enviar_mensagem(self):
        return f"Email({self.destinatario}). Assunto: {self.assunto}"

class SMS(Mensagem):
    def __init__(self, numero, mensagem):
        #super().__init__()
        self.numero = numero
        self.mensagem = mensagem

    def enviar_mensagem(self):
        return f"SMS({self.numero}). {self.mensagem}"

class NotificacaoPush(Mensagem):
    def __init__(self, dispositivo_id, mensagem):
        #super().__init__()
        self.dispositivo_id = dispositivo_id
        self.mensagem = mensagem

    def enviar_mensagem(self):
        return f"Notificação Push({self.dispositivo_id}). {self.mensagem}"

def realizar_envio(mensagem:Mensagem):
    print(mensagem.enviar_mensagem())


email = Email(destinatario="joao.silva@email.com", assunto="Reunião",
corpo="Reunião marcada para as 10h.")
sms = SMS(numero="912345678", mensagem="A sua Encomenda Chegou.")
notificacao = NotificacaoPush(dispositivo_id="abc123", mensagem="Tem uma Nova Mensagem.")

realizar_envio(email)
realizar_envio(sms)
realizar_envio(notificacao)
