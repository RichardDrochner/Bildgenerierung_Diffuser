@echo off
setlocal

REM
set HTTP_PROXY=
set HTTPS_PROXY=
set http_proxy=
set https_proxy=

REM
set NO_PROXY=127.0.0.1,localhost
set no_proxy=127.0.0.1,localhost

if not exist .venv (
  py -3.11 -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
python -m pip install -r requirements.txt

python app.py

pause