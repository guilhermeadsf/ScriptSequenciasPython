import pymysql

config = {
    'user': 'admin',
    'host': 'localhost',
    'password': 'admin',
    'database': 'quantidadetweets'
}

# Conexão com o Banco de Dados MySQL, arquivo config contém as informações de conexão.
cnx = pymysql.connect(**config)
cursor = cnx.cursor()

# O "CHARACTER SET utf8mb4" serve para evitar o erro de encode, repassando a configuração de UTF-8 ao MySQL.
cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")
cnx.commit()

# Define a tabela postas e suas propriedades.
table_name = 'tweepyIFG'

table = ("CREATE TABLE `IFG_Goias` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFGAguasLindas` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Anapolis` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `ifg_aparecida` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_FORMOSA` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Goiania` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFGGoianiaOeste` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `ifginhumas` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Itumbiara` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Jatai` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Luziania` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Uruacu` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Seq1` int (11),"
             "  `Seq2` int (11),"
             "  `Seq3` int (11),"
             "  `Seq4` int (11),"
             "  `Seq5` int (11),"
             "  `Seq6` int (11),"
             "  `Seq7` int (11),"
             "  `Seq8` int (11),"
             "  `total` int (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB")

# Função para criar a tabela "posts" no banco de dados e seta os caracteres em "utf-8".
def create_db_table():
    for t in table:
        cursor.execute('SHOW DATABASES;')
        all_dbs = cursor.fetchall()
        if all_dbs.count((config['database'],)) == 0:
            print("Creating db")
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(config['database']))

        cursor.execute('USE %s;' % config['database'])
        cursor.execute("SHOW TABLES;")
        all_tables = cursor.fetchall()
        if all_tables.count(('pages',)) == 0:
            print("creating table")
            cursor.execute(t)

# Chama a função de criação da tabela, por padrão sem comentário.
create_db_table()

# Função para inserção dos dados.
def insert_post(screen_name, seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, total):
    # Define a inserção de dados no banco de dados.
    insert = "INSERT INTO " + screen_name + ""
    add_message = (insert +
                   "(Seq1,Seq2,Seq3,Seq4,Seq5,Seq6,Seq7,Seq8,total)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(add_message, (seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, total))
    cnx.commit()