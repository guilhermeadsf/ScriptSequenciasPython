import pymysql
from GerarSequencias.MySQL import insert_post

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='tweepyifg', user='admin', passwd='admin')

listaScreenNamesCampus = ('IFG_Goias'), ('IFGAguasLindas'), ('IFG_Anapolis'), \
                         ('ifg_aparecida'), ('IFG_Goiania'), ('IFGGoianiaOeste'), \
                         ('ifginhumas') , ('IFG_Itumbiara'),('IFG_Jatai'), ('IFG_Luziania'), ('IFG_Uruacu')

# Cria um cursor:
cursor = conexao.cursor()

for campus in listaScreenNamesCampus:
    cursor.execute("SELECT * FROM " + campus)
    resultado = cursor.fetchall()

    for linha in resultado:

        L = ''
        Rt = ''
        Rtk = ''

        if(linha[1] != 0):
            L = 'L'
        else:
            L = '!L'

        if(linha[2] != 0):
            Rt = 'Rt'
        else:
            Rt = '!Rt'

        if(linha[3] != 0):
            Rtk = 'Rtk'
        else:
            Rtk = '!Rtk'

        insert_post(campus, L, Rt, Rtk)

# Finaliza a conexão
conexao.close()