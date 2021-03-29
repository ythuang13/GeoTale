from _thread import *
import socket
import mysql.connector
import pickle
import tqdm

DB = mysql.connector.connect(host="localhost",
                             port="3306",
                             user="admin",
                             password="GeoTale21!",
                             database="geotale")
CURSOR = DB.cursor(dictionary=True)
HEADER_SIZE = 10
BUFFER_SIZE = 1024 * 4
HOST = "172.31.35.237"
PORT = 5555
FORMAT = "utf-8"


def process_action(conn, indicator, data):
    if indicator == "Q":
        # query and return story from zip code
        CURSOR.execute("SELECT * FROM story WHERE zip_code = %s", (data,))
        result = CURSOR.fetchall()

        # return status code
        data = pickle.dumps(result)
        d = bytes(f"{len(data):<{HEADER_SIZE}}", FORMAT) + data
        conn.sendall(d)
    elif indicator == "I":
        # parse data
        zip_code, title, author, description, length = data

        # insert into mysql
        print(zip_code, title, author, length, description)

        # return status code
        data = pickle.dumps("200")
        d = bytes(f"{len(data):<{HEADER_SIZE}}", FORMAT) + data
        conn.sendall(d)
    elif indicator == "U":
        file_size, file_name = data
        extension = file_name.split(".")[-1]

        # another sick progress bar
        progress = tqdm.tqdm(range(file_size), f"Receiving {file_name}",
                             unit="B", unit_scale=True, unit_divisor=1024)

        # get save file name
        CURSOR.execute("SELECT story_id FROM story ORDER BY story_id DESC")
        i = CURSOR.fetchone().get("story_id")
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

                # update the progress bar
                progress.update(len(data_chunks))
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
