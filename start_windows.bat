@echo off
setlocal

cd /d "%~dp0"

if not exist .venv (
  py -3.11 -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
python -m pip install -r requirements.txt

if not exist "%USERPROFILE%\.cache\huggingface\stored_tokens" (
  echo [HINWEIS] Kein HuggingFace Login gefunden. Ihr benötigt einen HuggingFace-Account um dieses Modell zu nutzen
  echo Bitte einmal ausfuehren:
  echo.
  echo   hf auth login
  echo.
  echo Mit einem HuggingFace Token einloggen und danach dieses Skript erneut starten.
  pause
  exit /b
)

if not exist "models\stable-diffusion-v1-5\model_index.json" (
  echo [INFO] Stable Diffusion Modell fehlt. Starte Download...
  hf download runwayml/stable-diffusion-v1-5 ^
    --local-dir models\stable-diffusion-v1-5 ^
    --max-workers 8

  if errorlevel 1 (
    echo [FEHLER] Download fehlgeschlagen.
    echo Moegliche Gruende:
    echo  - Lizenz nicht akzeptiert
    echo  - Kein Internet
    echo  - HuggingFace Token fehlt
    pause
    exit /b
  )
)

python app.py

pause