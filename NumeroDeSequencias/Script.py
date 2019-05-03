import pymysql
from NumeroDeSequencias.MySQL import insert_post

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='seqtweets', user='admin', passwd='admin')

listaScreenNamesCampus = ('IFG_Goias'), ('IFGAguasLindas'), ('IFG_Anapolis'), \
                         ('ifg_aparecida'), ('IFG_Goiania'), ('IFGGoianiaOeste'), \
                         ('ifginhumas') , ('IFG_Itumbiara'),('IFG_Jatai'), ('IFG_Luziania'), ('IFG_Uruacu')

# Cria um cursor:
cursor = conexao.cursor()

for campus in listaScreenNamesCampus:
    cursor.execute("SELECT * FROM " + campus)
    resultado = cursor.fetchall()

    # L Rt Rtk
    Seq1 = 0
    # L Rt !Rtk
    Seq2 = 0
    # L !Rt Rtk
    Seq3 = 0
    # L !Rt !Rtk
    Seq4 = 0
    # !L Rt Rtk
    Seq5 = 0
    # !L Rt !Rtk
    Seq6 = 0
    # !L !Rt Rtk
    Seq7 = 0
    # !L !Rt !Rtk
    Seq8 = 0
    total = 0

    for linha in resultado:

            if(linha[1] == 'L' and linha[2] == 'Rt' and linha[3] == 'Rtk'):
                Seq1 = Seq1 + 1

            if(linha[1] == 'L' and linha[2] == 'Rt' and linha[3] == '!Rtk'):
                Seq2 = Seq2 + 1

            if (linha[1] == 'L' and linha[2] == '!Rt' and linha[3] == 'Rtk'):
                Seq3 = Seq3 + 1

            if (linha[1] == 'L' and linha[2] == '!Rt' and linha[3] == '!Rtk'):
                Seq4 = Seq4 + 1

            if (linha[1] == '!L' and linha[2] == 'Rt' and linha[3] == 'Rtk'):
                Seq5 = Seq5+ 1

            if (linha[1] == '!L' and linha[2] == 'Rt' and linha[3] == '!Rtk'):
                Seq6 = Seq6 + 1

            if (linha[1] == '!L' and linha[2] == '!Rt' and linha[3] == 'Rtk'):
                Seq7 = Seq7 + 1

            if (linha[1] == '!L' and linha[2] == '!Rt' and linha[3] == '!Rtk'):
                Seq8 = Seq8 + 1

    total = Seq1 + Seq2 + Seq3 + Seq4 + Seq5 + Seq6 + Seq7 + Seq8
    insert_post(campus, Seq1, Seq2, Seq3, Seq4, Seq5, Seq6, Seq7, Seq8, total)

# Finaliza a conexão
conexao.close()