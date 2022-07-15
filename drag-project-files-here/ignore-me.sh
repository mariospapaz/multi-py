
echo "Installing dependencies"

python3 -m pip install --upgrade pip

python3 -m pip install pyinstaller

python3 -m pip install -r ./requirements.txt

python3 -m PyInstaller --distpath ./executables/dist --workpath ./executables/build ./executables/build.spec

rm -rf ./executables/build