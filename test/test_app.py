import os
import pytest
from tkinter import Tk, messagebox
from unittest.mock import patch
from app import get_email_list_from_csv, log_directory, log_filename, send_email_now, choose_attachment  # Ajuste para o nome do seu script

# Caminho para um arquivo CSV de teste
CSV_TEST_PATH = './src/data/dados_funcionarios.csv'

@pytest.fixture
def setup_csv_file(tmpdir):
    data = """id,nomeFuncionario,email,cargo
1,Estevam,estevamsouzalaureth@gmail.com,Museum/gallery exhibitions officer
2,Patricia Warren,plowe@gmail.org,Rural practice surveyor
"""
    p = tmpdir.mkdir("sub").join("dados_funcionarios_test.csv")
    p.write(data)
    return str(p)

def test_get_email_list_from_csv(setup_csv_file):
    expected = [
        {'nome': 'Estevam', 'email': 'estevamsouzalaureth@gmail.com'},
        {'nome': 'Patricia Warren', 'email': 'plowe@gmail.org'}
    ]
    result = get_email_list_from_csv(setup_csv_file)
    assert result == expected, "A função get_email_list_from_csv não retornou a lista esperada."

def test_log_directory_and_file_creation():
    assert os.path.exists(log_directory), "O diretório de log não foi criado."
    assert os.path.exists(log_filename), "O arquivo de log não foi criado."

@pytest.fixture
def employee_list():
    return [
        {'nome': 'Test User', 'email': 'test@example.com'}
    ]

@patch('main.smtplib.SMTP')
def test_send_email_now(mock_smtp, employee_list):
    with patch('main.get_email_list_from_csv', return_value=employee_list):
        send_email_now()
        assert mock_smtp.called, "SMTP não foi chamado para enviar e-mail."

def test_choose_attachment():
    with patch('main.filedialog.askopenfilename', return_value='path/to/file.txt'):
        root = Tk()
        root.withdraw()  # Para evitar que a janela do Tkinter abra
        choose_attachment()
        root.destroy()
        assert attachment_path == 'path/to/file.txt', "O caminho do anexo não foi atualizado corretamente."

@pytest.mark.parametrize("smtp_server,expected", [
    ("smtp.gmail.com", {"email": "estevamsouzalaureth@gmail.com", "password": "exzegozaswezqhwo", "port": 587}),
    ("smtp.office365.com", {"email": "estevamsouzalaureth@hotmail.com", "password": "liqlnqteemeqzczh", "port": 587}),
])
def test_smtp_selection(smtp_server, expected):
    with patch('main.smtp_server_var.get', return_value=smtp_server):
        assert send_email_now().get('email') == expected['email']
        assert send_email_now().get('password') == expected['password']
        assert send_email_now().get('port') == expected['port']

@patch('main.messagebox')
def test_unsupported_smtp_server(mock_messagebox):
    with patch('main.smtp_server_var.get', return_value="unsupported_smtp"):
        send_email_now()
        mock_messagebox.showerror.assert_called_once_with("Erro", "Servidor SMTP não suportado.")

@patch('main.smtplib.SMTP')
@patch('main.filedialog.askopenfilename', return_value='path/to/test_file.pdf')
def test_complete_email_sending_flow(mock_file_dialog, mock_smtp):
    choose_attachment()  # Simula a escolha de um arquivo
    with patch('main.get_email_list_from_csv', return_value=[{'nome': 'Test', 'email': 'test@example.com'}]):
        send_email_now()
    mock_smtp.assert_called_once()

@patch('main.schedule.every')
def test_schedule_email(mock_schedule_every):
    with patch('main.schedule_time.get', return_value="12:00"):
        schedule_email()
        mock_schedule_every().day.at.assert_called_once_with("12:00")

# ======================================================================================================================

from app import validate_schedule_time  # Supondo que esta função existe

def test_invalid_schedule_time():
    invalid_times = ["25:00", "24:60", "abcd", "13:60"]
    for time in invalid_times:
        with patch('main.schedule_time.get', return_value=time):
            result = validate_schedule_time()
            assert not result, f"Horário inválido '{time}' foi aceito como válido."

def test_predefined_message_and_subject_loading():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela da GUI
    app = EmailApp(root)  # Supondo que você tenha uma classe para o app
    assert app.subject.get() == "Atualizações Semanais da [Nome da Empresa]", "O assunto pré-definido não foi carregado corretamente."
    assert app.message.get("1.0", tk.END).strip() == predefined_message.strip(), "A mensagem pré-definida não foi carregada corretamente."
    root.destroy()

@patch('main.tkinter.Tk.destroy')
def test_exit_button(mock_destroy):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela da GUI
    exit_button.invoke()  # Supondo que você tenha um botão de saída chamado exit_button
    mock_destroy.assert_called_once(), "O botão de saída não fechou a aplicação."

@patch('main.smtplib.SMTP')
def test_email_sending_with_attachment(mock_smtp):
    with patch('main.filedialog.askopenfilename', return_value='path/to/test_file.pdf'), \
         patch('main.get_email_list_from_csv', return_value=[{'nome': 'Test', 'email': 'test@example.com'}]):
        send_email_now()
        # Verifica se o SMTP foi chamado com os parâmetros corretos, incluindo um anexo
        # Esta parte depende da implementação específica de como você está anexando o arquivo ao e-mail
        assert mock_smtp.mock_calls, "O SMTP não foi chamado para enviar o e-mail com anexo."

@patch('main.smtplib.SMTP')
@patch('main.filedialog.askopenfilename', return_value='path/to/test_file.pdf')
@patch('main.get_email_list_from_csv', return_value=[{'nome': 'Test User', 'email': 'test@example.com'}])
def test_complete_integration(mock_get_email_list, mock_file_dialog, mock_smtp):
    # Simula a execução completa do app, desde a abertura até o envio de e-mails
    # Isso requer que você estruture seu código para permitir essa simulação
    complete_app_run_simulation()  # Esta função precisa ser definida de acordo com a estrutura do seu app
    assert mock_smtp.called, "O processo de envio de e-mail completo não foi executado corretamente."

def test_password_security():
    # Supondo que existe uma função para configurar a senha
    set_password("password123")  # Esta função precisa ser implementada
    # Verificar se a senha é armazenada de forma segura, e não em texto claro
    assert not is_password_stored_in_plain_text(), "A senha está armazenada em texto claro."

def test_recipient_email_validation():
    invalid_emails = ["test@", "@example.com", "test@example", "plainaddress", "", "test@.com"]
    for email in invalid_emails:
        assert not is_valid_email(email), f"Endereço de e-mail inválido '{email}' foi aceito."

@patch('main.messagebox.showinfo')
@patch('main.messagebox.showerror')
@patch('main.smtplib.SMTP')
def test_user_feedback_after_email_sending(mock_smtp, mock_showerror, mock_showinfo):
    simulate_email_sending_process()  # Esta função simula o processo de envio de e-mail
    # Verificar se uma das caixas de mensagem foi chamada
    assert mock_showinfo.called or mock_showerror.called, "Nenhum feedback foi fornecido ao usuário."

def test_form_cleanup_after_sending():
    fill_and_send_email_form()  # Preenche e envia o formulário de e-mail
    # Verificar se os campos do formulário foram limpos
    assert is_form_cleaned(), "O formulário não foi limpo após o envio."

@patch('main.logger.info')
def test_logging_user_actions(mock_logger_info):
    perform_user_actions()  # Realiza ações do usuário que deveriam ser logadas
    assert mock_logger_info.called, "Ações do usuário não estão sendo registradas no arquivo de log."
