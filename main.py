import os
from colabcode import ColabCode
from time import sleep
print("make sure to install colabcode by pip")
sleep(2)
os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz")
os.system("tar -xf ngrok-stable-linux-amd64.tgz")
os.system("!./ngrok authtoken 23C8Mj5lBcgqgglDqXTa2c5FnYw_7H5qAnw9AJ6KfHaEUPn5e")
