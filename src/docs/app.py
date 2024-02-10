from modules import *


# Configuração de aparência da GUI
BACKGROUND_COLOR = "#ffe082"
FONT = ("Times New Roman", 20, "italic")
window = Tk()


class AnimatedBanner:
    """
    Classe para exibir um banner animado com texto colorido.

    Attributes:
        text (str): O texto que será exibido no banner.
        colors (list): Uma lista de cores do Colorama para colorir o texto.
        font (str): O estilo de fonte usado para renderizar o texto. Padrão é 'big'.
        custom_fig (pyfiglet.Figlet): Instância da classe Figlet para renderizar o texto com a fonte personalizada.
    """
    def __init__(self, text, colors, font='big'):
        """
        Inicializa um objeto AnimatedBanner.

        Args:
            text (str): O texto que será exibido no banner.
            colors (list): Uma lista de cores do Colorama para colorir o texto.
            font (str, opcional): O estilo de fonte usado para renderizar o texto. Padrão é 'big'.
        """
        self.text = text
        self.colors = colors
        self.custom_fig = Figlet(font=font)

    def run(self):
        """
        Executa a animação do banner.

        A função exibe o banner animado com as cores especificadas.
        """
        while True:
            for color in self.colors:
                for line in self.custom_fig.renderText(self.text).splitlines():
                    print(color + Style.BRIGHT + line, flush=True)
                    time.sleep(0.05)
            time.sleep(0.5)
            break


# Configuração do logger
log_directory = "log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
log_filename = os.path.join(log_directory, "email_sender.log")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_filename,
                    filemode='a')
logger = logging.getLogger()
logger.info("Aplicativo Iniciado e pronto para uso.")


def barLoading():
    color_bars = [Fore.GREEN]
    for color in color_bars:
        for i in trange(int(7**7.5), bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Fore.RESET)):
            pass
    os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)


def app():
    barLoading()
    banner = AnimatedBanner('Envio de e-mail!!', [Fore.MAGENTA])
    banner.run()


# ====================== FUNÇÕES DE UTILIDADE ====================#
def get_email_list_from_csv(file_path):
    email_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email_list.append(row['email'])
    return email_list


def get_email_list_from_csv(file_path):
    """
    Lê um arquivo CSV e retorna uma lista de dicionários contendo o nome e o e-mail de cada funcionário.
    """
    employee_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee_list.append({'nome': row['nomeFuncionario'], 'email': row['email']})
    return employee_list


def show_emails_sent_window(emails_sent_successfully):
    # Cria uma nova janela Tkinter
    email_window = tk.Toplevel()
    email_window.title("E-mails Enviados com Sucesso")
    email_window.geometry("400x300")  # Ajuste o tamanho conforme necessário

    # Adiciona um widget ScrolledText para exibir os e-mails
    text_area = scrolledtext.ScrolledText(email_window, wrap=tk.WORD, width=40, height=10)
    text_area.grid(column=0, pady=10, padx=10)
    text_area.insert(tk.INSERT, "\n".join(emails_sent_successfully))
    text_area.configure(state='disabled')  # Desabilita edição do texto

    # Adiciona um botão para fechar a janela
    close_button = tk.Button(email_window, text="Fechar", command=email_window.destroy)
    close_button.grid(column=0, pady=10)


# Função para enviar e-mail agora
def send_email_now():
    employee_list = get_email_list_from_csv('src/data/dados_funcionarios.csv')
    subject_text = subject.get()
    message_text = message.get("1.0", END)
    smtp_server = smtp_server_var.get()

    emails_sent_successfully = []  # Lista para coletar os emails enviados com sucesso

    # Configuração dos servidores SMTP em um dicionário
    smtp_servers = {
        "smtp.gmail.com": {
            "email": "estevamsouzalaureth@gmail.com",
            "password": "exzegozaswezqhwo",
            "port": 587,
            "message": "smtp do Google adicionado."
        },
        "smtp.office365.com": {
            "email": "estevamsouzalaureth@hotmail.com",
            "password": "liqlnqteemeqzczh",
            "port": 587,
            "message": "smtp do Outlook adicionado."
        },
        "smtp.ibge.com": {
            "email": "estevam.estagio@ibge.gov.com",
            "password": "liqlnqteemeqzczh",
            "port": 587,
            "message": "smtp do IBGE adicionado."
        }
    }

    # Verifica se o servidor SMTP selecionado está no dicionário
    if smtp_server in smtp_servers:
        server_config = smtp_servers[smtp_server]
        my_email = server_config["email"]
        password = server_config["password"]
        port = server_config["port"]
        logger.info(server_config["message"])
        messagebox.showinfo("Sucesso", server_config["message"])
    else:
        messagebox.showerror("Erro", "Servidor SMTP não suportado.")
        logger.error("Servidor SMTP não suportado.")
        return

    try:
        with smtplib.SMTP(smtp_server, port=port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for employee in employee_list:
                emails_sent_successfully.append(f"{employee['nome']} ({employee['email']})")
                msg = MIMEMultipart()
                msg['From'] = my_email
                msg['To'] = employee['email']
                msg['Subject'] = subject_text
                
                msg.attach(MIMEText(message_text, 'plain', 'utf-8'))
                
                if attachment_path:
                    part = MIMEBase('application', "octet-stream")
                    with open(attachment_path, 'rb') as file:
                        part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
                    msg.attach(part)
                    # logger.info("Documento adicionado.")

                # Imprimir no terminal
                logger.info(f"Enviando para: {employee['nome']} ({employee['email']})")
                print(f"Enviando para: {employee['nome']} ({employee['email']})")
                # messagebox.showerror("Sucesso", "Começando a enviar os e-mails.")
                
                connection.send_message(msg)
                
        if emails_sent_successfully:
            show_emails_sent_window(emails_sent_successfully)
            success_message = "E-mails enviados com sucesso para:\n" + "\n".join(emails_sent_successfully)
            messagebox.showinfo("Sucesso", success_message)
            print("Sucesso!!! Os e-mails foram enviados")
            logger.info("Sucesso!!! Os e-mails foram enviados.")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao enviar os e-mails: {e}")
        print(f"Error!!! Não foi possível enviar os e-mails: {e}")
        logger.error("Todos os e-mails Não foram enviados com sucesso.")


# Função para agendar envio de e-mail
def schedule_email():
    send_time = schedule_time.get()
    if send_time:
        schedule.clear()  # Limpa os trabalhos agendados anteriores
        schedule.every().day.at(send_time).do(send_email_now)
        messagebox.showinfo("Agendado", f"E-mails serão enviados diariamente às {send_time}.")
        print("==========================")
        print("Os e-mails foram agendados")
        print("==========================")
        logger.info("Os e-mails foram agendados com sucesso.")

    else:
        messagebox.showerror("Erro", "Por favor, insira um horário válido.")
        print("===================================================")
        print("Aviso!!! Defina um horário para o envio dos e-mails")
        print("===================================================")
        logger.error("Defina um horário para o envio dos e-mails.")


# Função para executar tarefas agendadas (chamada periodicamente)
def run_scheduled_tasks():
    schedule.run_pending()
    window.after(10000, run_scheduled_tasks)  # Reagendar a execução em 10 segundos


# Função para selecionar um arquivo
def select_file():
    file_path = filedialog.askopenfilename()  # Abre o diálogo para escolher o arquivo
    if file_path:  # Se um arquivo foi selecionado
        attachment_var.set(file_path)  # Atualiza a variável com o caminho do arquivo
        attachment_label.config(text=f"Arquivo selecionado: {file_path}")  # Atualiza o label com o nome do arquivo

logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def on_exit():
    # Registro da ação de saída no logger
    logging.info("Cliente saiu do aplicativo.")
    
    # Exibir uma caixa de mensagem
    messagebox.showinfo("Sair", "Cliente saiu do aplicativo.")
    
    print("=================================================")
    print("Você acabou de sair da aplicação, volte sempre!!!")
    print("=================================================")
    
    # Fechar a janela
    window.destroy()


# Função para validar o CNPJ
def validar_cnpj(cnpj):
    # Aqui você colocaria a lógica para validar o CNPJ
    # Esta é apenas uma implementação de exemplo, substitua pela sua lógica de validação
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False
    return True


# Função chamada quando o CNPJ Entry perde o foco
def on_cnpj_focusout(event):
    cnpj = cnpj_entry.get()
    if not validar_cnpj(cnpj):
        messagebox.showwarning("CNPJ Inválido", "O CNPJ informado está incorreto. Por favor, verifique.")


# Definição e inserção da mensagem pré-definida
def update_predefined_message():
    predefined_message = f"""Olá {cnpj_entry.get()} - {razao_social_entry.get()}, estamos entrando em contato sobre a [PESQUISA] para avaliar que:
{variavel_adicional1_entry.get()}
Tal tal tal
{variavel_adicional2_entry.get()}"""

    message.delete('1.0', tk.END)
    message.insert('1.0', predefined_message)


# Defina a função choose_attachment após a criação de todos os widgets que ela usa
def choose_attachment():
    global attachment_path
    attachment_path = filedialog.askopenfilename(title="Select a file", filetypes=(("all files", "*.*"), ("pdf files", "*.pdf")))
    if attachment_path:
        file_name = os.path.basename(attachment_path)
        file_extension = os.path.splitext(attachment_path)[1]
        logging.info(f"Documento adicionado: {file_name}, Tipo: {file_extension}")
        attachment_label.config(text=file_name)
    else:
        # Quando nenhum arquivo é selecionado, limpe attachment_path
        attachment_path = ""  # Reinicializa para indicar que nenhum arquivo foi escolhido
        attachment_label.config(text="No file selected")


# ====================== GUI SETUP SECTION ====================#
app()

window.title("GUI E-Mail Sender")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

FONT = ("Times New Roman", 20, "italic")
BACKGROUND_COLOR = "#ffe082"

# Botão para enviar e-mail imediatamente
send_now_button = Button(window, text="Enviar Agora", command=send_email_now, font=FONT, bg=BACKGROUND_COLOR)
send_now_button.grid(column=2, row=6)  # Ajuste a posição conforme necessário

# Botão para agendar o envio de e-mail
schedule_button = Button(window, text="Agendar Envio", command=schedule_email, font=FONT, bg=BACKGROUND_COLOR)
schedule_button.grid(column=2, row=5)  # Ajuste a posição conforme necessário

# Botão para sair da aplicação
exit_button = Button(window, text="Sair", command=on_exit, font=FONT, bg=BACKGROUND_COLOR)
exit_button.grid(column=2, row=7)

# Seleção do servidor SMTP
smtp_server_label = Label(window, text="SMTP Server:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
smtp_server_label.grid(column=0, row=0)
smtp_server_var = StringVar(window)
smtp_server_var.set("smtp.gmail.com")  # valor padrão
smtp_server_dropdown = tk.OptionMenu(window, smtp_server_var, "smtp.gmail.com", "smtp.office365.com")
smtp_server_dropdown.grid(column=1, row=0)

# Logo
canvas = Canvas(width=128, height=128, highlightthickness=0, bg=BACKGROUND_COLOR)
logo_image = Image.open("public/logo.png")
logo_photo = ImageTk.PhotoImage(logo_image)
canvas.create_image(64, 64, image=logo_photo)
canvas.grid(column=2, row=0, rowspan=2)

# Configuração do widget de entrada do CNPJ com um bind para o evento de perda de foco
# Campos de entrada para CNPJ, Razão Social e Variáveis Adicionais
cnpj_label = Label(window, text="CNPJ:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
cnpj_label.grid(column=0, row=4)
cnpj_entry = Entry(window, width=30, highlightthickness=0)
cnpj_entry.grid(column=1, row=4)
cnpj_entry.bind("<FocusOut>", on_cnpj_focusout)

razao_social_label = Label(window, text="Razão Social:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
razao_social_label.grid(column=0, row=5)
razao_social_entry = Entry(window, width=30, highlightthickness=0)
razao_social_entry.grid(column=1, row=5)

variavel_adicional1_label = Label(window, text="Variável adicional 1:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
variavel_adicional1_label.grid(column=0, row=6)
variavel_adicional1_entry = Entry(window, width=30, highlightthickness=0)
variavel_adicional1_entry.grid(column=1, row=6)

variavel_adicional2_label = Label(window, text="Variável adicional 2:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
variavel_adicional2_label.grid(column=0, row=7)
variavel_adicional2_entry = Entry(window, width=30, highlightthickness=0)
variavel_adicional2_entry.grid(column=1, row=7)

# Campo de Assunto com valor pré-definido
subject_label = Label(window, text="Subject:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
subject_label.grid(column=0, row=1)
subject = Entry(window, width=30, highlightthickness=0)
subject.grid(column=1, row=1)
predefined_subject = "Atualizações Semanais da [Nome da Empresa]"
subject.insert(0, predefined_subject)

# Campo de Mensagem com valor pré-definido
message_label = Label(text="Message:", bg=BACKGROUND_COLOR, font=FONT, anchor='w')
message_label.grid(column=0, row=2)
message = Text(height=15, width=60)
message.grid(column=0, row=3, columnspan=3)  # Expandir para abranger três colunas

update_predefined_message_button = Button(window, text="Atualizar Mensagem", command=update_predefined_message, font=FONT, bg=BACKGROUND_COLOR)
update_predefined_message_button.grid(column=0, row=8, columnspan=2, sticky=W)  # Estende-se pelas colunas 0 e 1, alinhado à esquerda

attachment_label = Label(window, text="No file selected", bg=BACKGROUND_COLOR, font=FONT)
attachment_label.grid(column=3, row=4)  # Ajuste a posição conforme necessário

attachment_path = ""  # Isso assume que você definiu esta variável globalmente

# Botão para escolher o anexo configurado após a definição de attachment_label
choose_attachment_button = Button(window, text="Choose Attachment", command=choose_attachment, font=FONT, bg=BACKGROUND_COLOR)
choose_attachment_button.grid(column=2, row=4) 

# Implementações adicionais para `send_email_now`, `schedule_email`, etc., são omitidas para brevidade

window.mainloop()  # Loop principal da interface gráfica