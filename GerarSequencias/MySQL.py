import pymysql

config = {
    'user': 'admin',
    'host': 'localhost',
    'password': 'admin',
    'database': 'seqtweets'
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
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFGAguasLindas` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Anapolis` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `ifg_aparecida` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_FORMOSA` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `num_likes` int(11),"
             "  `num_retweet` int(11),"
             "  `num_retweet_comments` int(11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Goiania` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFGGoianiaOeste` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `ifginhumas` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Itumbiara` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"),("CREATE TABLE `IFG_Jatai` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Luziania` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
             "  PRIMARY KEY (`id`)"
             ") ENGINE=InnoDB"), ("CREATE TABLE `IFG_Uruacu` ("
             "  `id` int(11) NOT NULL AUTO_INCREMENT,"
             "  `Curtir` varchar (11),"
             "  `Retweet` varchar (11),"
             "  `Retweet_Comentario` varchar (11),"
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
def insert_post(screen_name, num_likes, num_retweet, num_retweet_comments):
    # Define a inserção de dados no banco de dados.
    insert = "INSERT INTO " + screen_name + ""
    add_message = (insert +
                   "(Curtir, Retweet, Retweet_Comentario)"
                   "VALUES (%s, %s, %s)")
    cursor.execute(add_message, (num_likes, num_retweet, num_retweet_comments))
    cnx.commit()