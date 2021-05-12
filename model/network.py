from controller.settings import *
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
        except Exception:
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
        except ValueError:
            self.id = None

    def send_file(self, file_path) -> str:
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)

        # send indicator with file size
        d = pickle.dumps(("upload", (file_size, file_name)))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        self.client.sendall(d)

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
                _ = self.client.recv(3)

        # verify
        d = pickle.dumps(("verify size", (file_size,)))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        self.client.sendall(d)

        header = self.client.recv(HEADER_SIZE)
        d = self.client.recv(int(header))
        data = pickle.loads(d)
        status_code = data[1][0]

        return status_code

    def request_file(self, request_data):

        # send indicator with request_data
        d = pickle.dumps(("download", (request_data, )))
        d = bytes(f"{len(d):<{HEADER_SIZE}}", FORMAT) + d
        self.client.sendall(d)

        # receive file data
        header = self.client.recv(HEADER_SIZE)
        d = self.client.recv(int(header))
        data = pickle.loads(d)
        file_name = data[1][1]

        save_file_name = path.join("tmp", f"{file_name}")
        # receive file
        with open(save_file_name, "wb") as file:
            while True:
                header = self.client.recv(HEADER_SIZE)
                data_chunks = bytearray()
                try:
                    read_size = int(header)
                except ValueError:
                    continue
                if read_size == -1:
                    break

                while len(data_chunks) < read_size:
                    data_chunks.extend(self.client.recv(read_size))

                # write to the file the bytes we just received
                file.write(data_chunks)

                # acknowledgement
                self.client.sendall(b"200")
