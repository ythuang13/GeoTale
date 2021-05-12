from _thread import *
import socket
import mysql.connector
import pickle
import os

DB = mysql.connector.connect(host="localhost",
                             port="3306",
                             user="admin",
                             password="GeoTale21!",
                             database="geotale")
CURSOR = DB.cursor(dictionary=True, buffered=True)
HEADER_SIZE = 10
BUFFER_SIZE = 1024 * 4
HOST = "172.31.35.237"
PORT = 5555
FORMAT = "utf-8"


def process_action(conn, indicator, data):
    if indicator == "query":
        # query and return story from zip code
        if data == "":
            CURSOR.execute("SELECT * FROM story")
        else:
            CURSOR.execute("SELECT * FROM story WHERE zip_code = %s", (data,))
        result = CURSOR.fetchall()

        # return status code
        data = pickle.dumps(result)
        d = bytes(f"{len(data):<{HEADER_SIZE}}", FORMAT) + data
        conn.sendall(d)
    elif indicator == "query download":
        # query and return boolean from story id
        print(data)
        CURSOR.execute("SELECT * FROM story WHERE story_id = %s", (data, ))
        result = CURSOR.fetchone()

        # return true or false
        if result:
            result = True
        else:
            result = False
        data = pickle.dumps(result)
        d = bytes(f"{len(data):<{HEADER_SIZE}}", FORMAT) + data
        conn.sendall(d)
    elif indicator == "I":
        # parse data
        zip_code, title, author, description, length = data

        # insert into mysql
        sql = "INSERT INTO story (zip_code, title, author, length," \
              "description) VALUES (%s, %s, %s, %s, %s)"
        val = (zip_code, title, author, length, description)
        CURSOR.execute(sql, val)
        DB.commit()

        print(val)
        print(CURSOR.rowcount, "record inserted")

        # return status code
        data = pickle.dumps("200")
        d = bytes(f"{len(data):<{HEADER_SIZE}}", FORMAT) + data
        conn.sendall(d)
    elif indicator == "upload":
        file_size, file_name = data
        extension = file_name.split(".")[-1]

        # get save file name
        CURSOR.execute("SELECT story_id FROM story ORDER BY story_id DESC")
        temp = CURSOR.fetchone()
        i = temp.get("story_id", 0)
        save_file_name = f"storage/{i + 1}.{extension}"

        # receive file
        with open(save_file_name, "wb") as file:
            while True:
                header = conn.recv(HEADER_SIZE)
                data_chunks = bytearray()
                try:
                    read_size = int(header)
                except ValueError:
                    continue
                if read_size == -1:
                    break

                while len(data_chunks) < read_size:
                    data_chunks.extend(conn.recv(read_size))

                # write to the file the bytes we just received
                file.write(data_chunks)

                # acknowledgement
                conn.sendall(b"200")

    elif indicator == "download":
        temp = data[0]
        # check if filename is in directory
        file_path = f"storage/{temp}.wav"
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)

        # send file information, file_name and extension, and size
        d = pickle.dumps(("temp", (file_size, file_name)))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        conn.sendall(d)

        # send file
        with open(file_path, "rb") as file:
            while True:
                # read the bytes from the file
                bytes_read = file.read(BUFFER_SIZE)
                if not bytes_read:
                    # finish
                    d = bytes(f"{-1:<{HEADER_SIZE}}", FORMAT)
                    conn.sendall(d)
                    break

                d = bytes(f"{len(bytes_read):<{HEADER_SIZE}}", FORMAT) \
                    + bytes_read
                conn.sendall(d)

                # receive acknowledgement
                _ = conn.recv(3)

    elif indicator == "verify size":
        file_size = data[0]

        CURSOR.execute("SELECT story_id FROM story ORDER BY story_id DESC")
        temp = CURSOR.fetchone()
        file_name = temp.get("story_id")

        storage_file_size = os.path.getsize(os.path.join("storage",
                                                         f"{file_name+1}.wav"))
        if storage_file_size == file_size:
            status_code = "200"
        else:
            status_code = "404"

        # return status code back
        d = pickle.dumps(("D", (status_code, )))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        conn.sendall(d)

    elif indicator == "verify insert":
        pass
    else:
        print("else")


def threaded_client(conn):
    # initial confirmation
    conn.send(pickle.dumps("200"))

    while True:
        try:
            header = conn.recv(HEADER_SIZE)
            d = conn.recv(int(header))
            indicator, data = pickle.loads(d)
            print(indicator, data)

            process_action(conn, indicator, data)

        except ValueError:
            print("Disconnect with exit code: 0")
            break
        except ConnectionResetError:
            print("Disconnect with exit code: -1")
            break

    conn.close()
    print("Connection close")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
        except socket.error as e:
            print(e)

        s.listen(1)
        print(f"{HOST} listening on {PORT}...")

        while True:
            # handle incoming client
            connection, address = s.accept()
            print(f"Connection from {address} has been established.")
            start_new_thread(threaded_client, (connection,))


if __name__ == "__main__":
    main()
