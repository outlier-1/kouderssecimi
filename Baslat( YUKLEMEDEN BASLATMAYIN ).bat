cd C:\Users\%USERNAME%\Desktop\DersSecimi\

ECHO "Checking For PIP Existence..."
python get-pip.py
ECHO "Checking For Binding Libraries..."
pip install -r requirements.txt
ECHO "Google Chrome Driver is Setting as Environment Variable..."
setx path "%path%;C:\Users\%USERNAME%\Desktop\DersSecimi\chromedriver.exe"
cls
ECHO "Program Was Succesfully Started!"
python main.py
