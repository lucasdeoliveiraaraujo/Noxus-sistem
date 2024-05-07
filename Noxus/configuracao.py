from decouple import config
from mysql.connector import connection
from mysql.connector import errorcode
from io import StringIO
#import sys
#sys.path.append("..")
import os


def alterarquivoconfig(nomearquivo: str):

    try:
        db_connection = connection.MySQLConnection(host="localhost",
                                                   user=config("USERDATABASE"),
                                                   password=config("PASSWORD"),
                                                   database=config("DATABASE"))

        cursor = db_connection.cursor()
        sql = ("""select emailnotificao,
                               porta,
                               senha,
                               tls,
                               host
                        from noxusapp_configuracao""")
        cursor.execute(sql)
        dados = {
            "emailnotificacao": "",
            "porta": 0,
            "senha": "",
            "tls": False,
            "host": ""
        }
        for (emailnotificacao, porta, senha, tls, host) in cursor:
            dados["emailnotificacao"] = emailnotificacao
            dados["porta"] = porta
            dados["senha"] = senha
            dados["tls"] = bool(tls)
            dados["host"] = host

            buffer = StringIO()
            print(dados)
            with open(f"{os.getcwd()}/Noxus/{nomearquivo}", "r") as arquivo:
                for linhas in arquivo:

                    if linhas.find("EMAIL_PORT") == 0:
                        buffer.write(f"\nEMAIL_PORT = {dados['porta']}")
                    elif linhas.find("EMAIL_HOST_PASSWORD") == 0:
                        buffer.write(f"\nEMAIL_HOST_PASSWORD = {dados['senha']}")
                    elif linhas.find("EMAIL_HOST_USER") == 0:
                        buffer.write(f"\nEMAIL_HOST_USER = {dados['emailnotificacao']}")
                    elif linhas.find("EMAIL_USE_TLS") == 0:
                        buffer.write(f"\nEMAIL_USE_TLS = {dados['tls']}")
                    elif linhas.find("EMAIL_BACKEND") == 0:
                        buffer.write(f"\nEMAIL_BACKEND = {dados['host']}")
                    else:
                        if linhas.find("[settings]") == 0:
                            buffer.write(" $ ".join(linhas.splitlines()))
                        else:
                            buffer.write("\n" + (" $ ".join(linhas.splitlines())))

            with open(f"{os.getcwd()}/Noxus/settings.ini", "w") as setting:
                setting.write(buffer.getvalue())
    except connection.errors.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)

    else:
        db_connection.close()

