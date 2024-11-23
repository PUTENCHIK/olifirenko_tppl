import socket


def repl(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        while True:
            print("\nIn: ", end="")
            try:
                text = input()
            except KeyboardInterrupt:
                break
            
            print(f": {text}")
            if text == "exit" or len(text) < 1:
                break
            
            sock.send(text.encode())
            answer = sock.recv(1024)
            print(f"\nOut: {answer.decode()}")
    
    print("\n\nProgram ended")
