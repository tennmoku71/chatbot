import setuptools

def _requirements():
    return ["os","http", "cgi", "sys", "io" , "importlib"]

def _test_requirements():
    return ["os","http", "cgi", "sys", "io" , "importlib"]
 
setuptools.setup(
    name="chatbotweb",
    version="0.0.4",
    author="Yoshiki Ohira",
    author_email="ohira.yoshiki@irl.sys.es.osaka-u.ac.jp",
    description="Automatic generation of web interface for user-defined chatbot",
    long_description="An interface that allows you to chat on the web using the chatbot engine of the question and answer type you created",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={
        'chatbotweb': ['cgi-bin/base.html','cgi-bin/chatbot.py','cgi-bin/default.html'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)