from setuptools import setup,find_packages

NAME="DL project CNN"
VERSION="0.0.0.1"
DESC="CNN Project on image classification"
AUTHOR="hrishikesh bhagawati"
AUTHOR_EMAIL="hrishikeshbhagawati@gmail.com"
URL="url"
REQ="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements():
    with open(REQ, "r") as requir:
        requir=requir.readlines()

        req1=[i.replace("\n","") for i in requir]

        if HYPHEN_E_DOT in req1:
            req1.remove(HYPHEN_E_DOT)
    return req1


setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=get_requirements()
    )