from controller.settings import *
import tqdm
import os
import socket
import pickle


class Network:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def quit(self):
        self.client.close()

    def send(self, data):
        try:
            # pickled data
            d = pickle.dumps(data)
            d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
            self.client.sendall(d)

            # receive and return data
            header = self.client.recv(HEADER_SIZE)
            d = self.client.recv(int(header))
            data = pickle.loads(d)
            return data
        except socket.error as e:
            print(e)

    def send_file(self, file_path):
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)

        # send indicator with file size
        d = pickle.dumps(("U", (file_size, file_name)))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        self.client.sendall(d)

        # sick progress bar
        progress = tqdm.tqdm(range(file_size), f"Sending file {file_name}",
                             unit="B", unit_scale=True, unit_divisor=1024)

        # send the file binary data in buffer size chunks
        with open(file_path, "rb") as file:
            while True:
                # read the bytes from the file
                bytes_read = file.read(BUFFER_SIZE)
                if not bytes_read:
                    # finish
                    d = bytes(f"{-1:<{HEADER_SIZE}}", FORMAT)
                    self.client.sendall(d)
                    break

                d = bytes(f"{len(bytes_read):<{HEADER_SIZE}}", FORMAT) \
                    + bytes_read
                self.client.sendall(d)

                # receive acknowledgement
                ack = self.client.recv(3)

                # update progress bar
                progress.update(len(bytes_read))


def main():
    network = Network(HOST, PORT)
    # print(network.id)

    # zip_code = input("Zip code: ")
    # title = input("title: ")
    # author = input("author: ")
    # description = input("description: ")
    # path = input("path: ")
    network.send_file(r"C:\Users\ythua\Desktop\image0.png")


if __name__ == "__main__":
    main()
