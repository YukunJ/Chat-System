
from chat_client_class import *
from sign_up import *

def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()
    login_in()
    fileobject = open('temporary_login_name.txt','r')
    entrancename = fileobject.readline().strip()
    fileobject.close() 
    client = Client(args,entrancename)
    client.run_chat()

main()
