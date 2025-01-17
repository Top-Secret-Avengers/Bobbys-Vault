import socket
import sys
import time
import random
from scapy.all import IP, UDP, TCP, ICMP, DNS, DNSQR, send

def start_ctf_server(port=1234, host='0.0.0.0'):

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 queued connections
    print(f"Server is running on {host}:{port}")
    
    try:
        while True:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            #print(f"Connection from {client_address}")
            
            #Define flag in binary
            flag="01010010010011010101010100101101010100100100111101001100010011000010110100110100001110000011011100110110"
            #RMU-ROLL-4876
            
            #Send different types of packets
            for bit in flag:
                if bit == "0":
                    #Send good packet
                    pkt = IP(dst=client_address[0]) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="https://www.youtube.com/watch?v=dQw4w9WgXcQ", qtype=1))
                elif bit == "1":
                    pkt = IP(dst=client_address[0]) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="https://www.youtube.com/watch?v=dQw4w9WgXcQ", qtype=28))
                        
                #Send packet
                send(pkt, verbose=False)
                    
                #Wait before sending next packet
                time.sleep(.1)
            
            #Send hint packet
            #print("Finished flag packets, sending confirmation packet")
            pkt = IP(dst=client_address[0]) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="Getting warmer! Should have 105 packets (including this one)", qtype=15))
            send(pkt, verbose=False)
            
            #Send goofy message over netcat, docker didn't like match case for some reason
            ran = random.randint(1, 18)

            if ran == 1:
                client_socket.sendall(b'Ooooooh you almost had it, gotta be quicker than that')
            elif ran == 2:
                client_socket.sendall(b'Keep trying buddy')
            elif ran == 3:
                client_socket.sendall(b'Sniff a little harder')
            elif ran == 4:
                client_socket.sendall(b'Man, you stink. Connor solved this in 5 minutes')
            elif ran == 5:
                client_socket.sendall(b"You've got this")
            elif ran == 6:
                client_socket.sendall(b'I sure could go for some rolls right now')
            elif ran == 7:
                client_socket.sendall(b'What is happening!?!')
            elif ran == 8:
                client_socket.sendall(b'I sure could go for a double nut sundae right about now')
            elif ran == 9:
                client_socket.sendall(b"I've been struggling in class lately, maybe I should make more queries to my professors")
            elif ran == 10:
                client_socket.sendall(b'rick')
            elif ran == 11:
                client_socket.sendall(b'Be patient. Or dont. Im not your dad')
            elif ran == 12:
                client_socket.sendall(b'Bypassing the mainframe, uploading the payload, cracking their system')
            elif ran == 13:
                client_socket.sendall(b'Some of these are hints, btw. Atrocious ones at that')
            elif ran == 14:
                client_socket.sendall(b'Just kidding')
            elif ran == 15:
                client_socket.sendall(b'I hacked your mom last night')
            elif ran == 16:
                client_socket.sendall(b'RMU-OHYOUWISHBUDDY-6969')
            elif ran == 17:
                client_socket.sendall(b'How was your day at school, sport?')
            elif ran == 18:
                client_socket.sendall(b'It takes roughly 20 per witty quip, jsyk')
                    
            # Close the connection
            client_socket.close()
    except KeyboardInterrupt:
        print("Shutting down the server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    
    if(len(sys.argv) > 1):
        start_ctf_server(int(sys.argv[1]))
    else:
    	start_ctf_server()
