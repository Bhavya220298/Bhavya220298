#install all these first
sudo apt install pip3
pip3 install fastapi
sudo apt install uvicorn
pip install uvicorn

#Once all packages are installed, run the below command
wget https://raw.githubusercontent.com/melwinvinod/melwinvinod/main/main.py

#Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8080
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
