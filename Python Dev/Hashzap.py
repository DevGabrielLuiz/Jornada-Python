# importar o flet
import flet as ft


# criar função principal do código
def main(pagina):
    # pagina.bgcolor ="FFFFFF"
    #Titulo : Hashzap
    titulo = ft.Text("HashZap")
    #titulo Bem vindo ao Hashzap
    titulo_janela = ft.Text("Bem vindo ao HashZap")
    #Campo de texto escreva seu nome 
    campo_nome_usuario = ft.TextField(label="Escreva seu nome")
    
    
    
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # enviar mensagem  
        
            # Mostrar mesagem com o nome de quem enviou
        pagina.pubsub.send_all(texto)
        # limpar campo mensagem
        texto_mensagem.value = ""
        texto_mensagem.focus()
        pagina.update()
        
    
    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
    
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    chat = ft.Column()
    #Botão: entrar no chat 
    def entrar_chat(evento):
        # Sumir com o titulo e o botão inicial  
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        
        #  Fechar o PopUp
        janela.open = False
        # Criar o chat 
        pagina.add(chat)
        # adicionar linha de mensagem
        pagina.add(linha_mensagem)
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        # criar campo de texto enviar mensagem e  criar botao enviar        
        
        # (com a mensagem de "[nome] entrou no chat") or chat.controls.append(f" nome entrou no chat") 
        pagina.pubsub.send_all(texto_entrou_chat)      
        # pode usar do outro já que essa mesnagem só é exibida uma vez e não é armazenada 
        pagina.update()
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )
    
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    #Botão inciar chat
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)   # criando o tunel de comunicação     
    
    
    # adicionando os elementos a págoma
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o sistema
ft.app(main, view=ft.WEB_BROWSER )
