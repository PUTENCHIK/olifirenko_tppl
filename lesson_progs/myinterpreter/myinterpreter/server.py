import socket
from .interpreter import Interpreter, Parser


def start_server(host, port) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(2)
        
        while True:
            print("Wait for new connection...")
            conn, addr = sock.accept()
            print(f"Connected: {addr}")
            
            while True:
                message = conn.recv(1024)
                print(f"Message: {message.decode()}")
                if message in (b"exit", b""):
                    conn.send(b"Program ended")
                    break
                
                interpreter = Interpreter()
                try:
                    if message.startswith(b"@"):
                        parser = Parser()
                        result = parser.eval(message[1:].decode())
                    else:
                        result = interpreter.eval(message.decode())
                        
                    conn.send(str(result).encode())
                except (RuntimeError, SyntaxError) as e:
                    conn.send(f"Error: {e}".encode())
