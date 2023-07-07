import socket
from jikanpy import Jikan
import requests
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "Baciacia",
    password = "alex",
    database = "AnimeDB"
)

mycursor = mydb.cursor()  #
#mycursor.execute('CREATE TABLE WWAnimes (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), nrEps VARCHAR(255), score VARCHAR(255),pref VARCHAR(255), Description TEXT)' )


def DataScore(name):
    anime_id = int(name)
    request_url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    
    response = requests.get(request_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def existInDb(name, db):
    sql = "SELECT * FROM {} WHERE EXISTS (SELECT %s FROM {} WHERE name = %s)".format(db,db)
    val = (name,name)
    mycursor.execute(sql, val)
    return mycursor.fetchall()
    

def InfoFromString(stringg):
    stringg = stringg.split('\n')
    name = stringg[0][stringg[0].index(':')+1:]
    Nreps = stringg[1][stringg[1].index(':')+1:]
    score = stringg[2][stringg[2].index(':')+1:]
    description = stringg[3][stringg[3].index(':')+1:]
    return name,Nreps,score,description



def Connection(adress, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((adress,port))
    s.listen(4)
    (connection, address) = s.accept()
    print ("Connectd address:",address);

    while True:
        data = connection.recv(10000).decode("UTF-8")
        if not data: break
        if "exit" in data: break
        if data[-4:] == 'addW':
            name,nrEp,score,description = InfoFromString(data)
            if existInDb(name,"WWAnimes"):
                message = "The Anime is already in watched".encode('utf-8')
            else:
                sql = "INSERT INTO WWAnimes (name, nrEps, score,pref, description) VALUES (%s, %s, %s, %s,%s)"
                val = (name,nrEp,score,'0',description)
                mycursor.execute(sql, val)
                mydb.commit()
                message = "The Anime was introduced succesfully in watched animes".encode('utf-8')
            connection.send(message)

        elif data[-4:] == 'addL':
            name,nrEp,score,description = InfoFromString(data)
            if existInDb(name,"LWAnime"):
                message = "The Anime is already in later-watch".encode('utf-8')
            else:
                sql = "INSERT INTO LWAnime (name, nrEps, score, description) VALUES (%s, %s, %s, %s)"
                val = (name,nrEp,score,description)
                mycursor.execute(sql, val)
                mydb.commit()
                message = "The Anime was introduced succesfully in later-watch".encode('utf-8')
            connection.send(message)


        elif data[-4:] == 'addP':
            name,nrEp,score,description = InfoFromString(data)
            sql = "UPDATE WWAnimes SET pref = %s WHERE name = %s"
            val = ('1',name)
            mycursor.execute(sql, val)
            mydb.commit()
            message = "The Anime was introduced as one of your preferates".encode('utf-8')
            connection.send(message)

        elif data == 'tabW':
            sql = "SELECT name FROM WWAnimes"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            sendRes = ''
            for row in result:
                nameAnime = str(row)
                nameAnime = nameAnime[3:len(nameAnime)-3]
                sendRes = sendRes + nameAnime + '\n'
            print(sendRes)
            sendRes_byte = sendRes.encode('utf-8')
            connection.send(sendRes_byte)

        elif data == 'tabL':
            sql = "SELECT name FROM LWAnime"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            sendRes = ''
            for row in result:
                nameAnime = str(row)
                nameAnime = nameAnime[3:len(nameAnime)-3]
                sendRes = sendRes + nameAnime + '\n'
            print(sendRes)
            sendRes_byte = sendRes.encode('utf-8')
            connection.send(sendRes_byte)

        elif data == 'deleteW':
            sql = "DROP TABLE WWAnimes"   #DELETE FROM WAnime WHERE id > 0
            mycursor.execute(sql)
            result = mycursor.fetchall()
            sendRes = 'Empty'
            sendRes_byte = sendRes.encode('utf-8')
            connection.send(sendRes_byte)
        
        elif data == 'deleteL':
            sql = "DELETE FROM LWAnime WHERE id > 0"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            sendRes = 'Empty'
            sendRes_byte = sendRes.encode('utf-8')
            connection.send(sendRes_byte)

        else:
            if data == '0':
                response = "Invalid id"
                connection.send(response.encode('utf-8'))
            else:
                serverResponse = DataScore(data)
                if serverResponse != None and serverResponse['data']['title_english'] != None:
                    data = serverResponse['data']
                    nameAnime = data['title_english']
                    nrEpisodes = data['episodes']
                    score = data['score']
                    description = data['synopsis']
                    response = "Name: " + nameAnime + "\nNumber Episodes: "+str(nrEpisodes)+"\nScore: "+str(score) + "\nDescription: "+ description +"\n"
                    connection.send(response.encode('utf-8'))

                else:
                    response = "Invalid id"
                    connection.send(response.encode('utf-8'))

        
        
    connection.close()
    print ("Server closed")

if __name__ == '__main__':

    Connection("127.0.0.1",1234)
    


