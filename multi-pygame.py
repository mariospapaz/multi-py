import platform
import subprocess

OS_NAME = platform.system()
OS_ARCHITECTURE = platform.machine()

if OS_NAME == "Darwin":
    OS_NAME = "mac"

if OS_ARCHITECTURE == "arm64":
    OS_ARCHITECTURE = "aarch64"

# Notes
# M1 Users can install the Catalina M1 and alpine-arm64 but not windows
#
#


# Todo, 
# There are problems with arm64users 
# Python does not seem to have an arm64 for windows or a darwin python image
# So I might have to kick them

print(f"""
Hello '{OS_NAME} {OS_ARCHITECTURE}' user.

A disclaimer before we continue.

An {OS_ARCHITECTURE} cpu will build an {OS_ARCHITECTURE} executable. 
Due to limitations of the software that I am using.

""")

while True:

    ans = input("You okay with that? [y/n]: ").upper()

    if ans == "Y":
        break 

    elif ans == "N":
        print("Learn GitHub Actions and do it in your own I believe in you!")
        raise SystemExit

    else:
        print("Wrong input")
        continue


import os
skip_install = os.path.isdir("./docker")

if not skip_install:
    print("Installing Docker 20.10.10...")
    url = f"https://download.docker.com/{OS_NAME}/static/stable/{OS_ARCHITECTURE}/docker-20.10.10.tgz"

    import requests
    import shutil
    from tqdm.auto import tqdm

    # if user decides to cancel the program, we do not want to leave docker behind 🐳
    try:
        with requests.get(url, stream=True) as r:

            if r.status_code == 200:
                # check header to get content length, in bytes
                total_length = int(r.headers.get("Content-Length"))
            
                # implement progress bar via tqdm
                with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
                    with open("./docker.tgz", 'wb') as docker:
                        shutil.copyfileobj(raw, docker)

                        print("Extracting docker and removing the compressed file..")

                        shutil.unpack_archive("./docker.tgz", ".")

                        subprocess.run(["rm", "-rf", "./docker.tgz"])
                
                print("Docker successfully installed! Time to rock and roll!")

            else:
                print("Failed to install docker")
                raise SystemExit

    except KeyboardInterrupt:
        print("Cancelling docker installation, deleting temp file")
        subprocess.run(["rm", "-rf", "./docker.tgz"])
        raise SystemExit

req = "./drag-project-files-here/requirements.txt"
if not os.path.isfile(req):
    raise ValueError("""\n\n
        You do not have a requirements.txt in /drag-project-files-here
        We need your modules in order to continue, dont worry you will return here!
    """)

print("Time to run the compose file")
pull = subprocess.run(["./docker/docker", "compose", "up"], capture_output=True, text=True)
print(pull.stdout)
print(pull.stderr)


# Once docker compose exits 0 , it will go back to deleting docker
subprocess.run(["./docker/docker", "rm", "linux", "windows", "mac"])

rem = subprocess.run(["rm", '-rf', "./docker"] , capture_output=True, text=True)
print(rem.stdout)
print(rem.stderr)