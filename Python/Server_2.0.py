import network
import socket
import ure

# Set up Wi-Fi network
ssid = 'Aman197'
password = 'ushaaman'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

# Wait for Wi-Fi connection
while station.isconnected() == False:
    pass

# Print IP address of ESP32 board
print('ESP32 IP address:', station.ifconfig()[0])

# Set up server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

with open("index.html", "r") as file:
    html = file.read()

# Define function to handle client requests
def handle_client(conn):
    # Receive data from client
    data = conn.recv(1024)

    # Extract HTTP request method and path
    request_method = ''
    path = ''
    if data:
        decoded_data = data.decode('utf-8')
        lines = decoded_data.split('\r\n')
        request_method, path, _ = lines[0].split(' ')

    # If path is /, return HTML form
    if path == '/':
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html
        conn.send(response.encode())

    # If path is /submit, process form data
    elif path == '/submit':
        # Extract form data
        form_data = decoded_data.split('\r\n')[-1]
        input_text = ure.search('input=(.+)', form_data).group(1)
        input_text = input_text.replace('+', ' ')
        
        print(input_text)

    elif path == '/button2':
        print('Button press ho gaya !')


# Listen for incoming connections
while True:
    conn, addr = s.accept()
    handle_client(conn)


