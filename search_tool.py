import requests
import argparse
from bs4 import BeautifulSoup
import socket
from concurrent.futures import ThreadPoolExecutor

p=argparse.ArgumentParser()
p.add_argument("-u",type=str,help="example:python search_tool.py -u example.com ")
a=p.parse_args()
print(f"""

███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████╗█████╗  ███████║██████╔╝██║     ███████║       ██║   ██║   ██║██║   ██║██║     
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║       ██║   ██║   ██║██║   ██║██║     
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                       
       

      ------------------------------
      target:{a.u}
      scan:started
      ------------------------------                                                            

""")


with open("google_dorking.txt","r") as google:
    google_dorking_list=google.read().splitlines()
    google.close()
with open("fuzz.txt","r") as fuzz:
    fuzz_list=fuzz.read().splitlines()
    fuzz.close()


for fuzz1 in fuzz_list:
    try:
        req=requests.get(f"{a.u}{fuzz1}")
        print(f"{req.status_code}-{a.u}{fuzz1}")
    except requests.exceptions.RequestException as e:
        print(f"page not found- {a.u+fuzz1}")
        print(e)
        continue