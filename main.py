from whatsapp_api.whatsapp_api import WhatsApp
import pandas as pd
from time import sleep

def enviarMensagem(whats, contato, mensagem):
  whats.search_contact(contato)
  whats.send_message(mensagem)

def main():
  wp = WhatsApp()

  input("Pressione enter após escanear o QR Code")

  df = pd.read_excel('lista_contatos.xlsx')
  contatos = df['Contato'].values.tolist()
  mensagens = df['Mensagem'].values.tolist()

  for contato, mensagem in zip(contatos, mensagens):
    enviarMensagem(wp, contato, mensagem)
    sleep(3)

  print('Finalizado envio das mensagens!')

  input("Pressione enter para sair")
  wp.driver.close()

if __name__ == '__main__':
  main()  
