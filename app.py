# Author: br-ow
from flask import Flask
from flask import render_template
import os
import email
from jinja2 import Environment, select_autoescape, BaseLoader

app = Flask(__name__)

@app.route("/")
def main():
    #the environment in which to render the jinja template
    #required by jinja
    jenv = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
    ),
    loader=BaseLoader(),)


    msgs = parse_msgs('./smallset')

    return render_template('jtemplate.html', emails=msgs)

def parse_msgs(directory):
    #reference: 
    # https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
    # https://products.fileformat.com/email/python/msg-extractor/

    msg_list = []

    #iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        #check if it is a file
        if os.path.isfile(f):
            #parse the message and add it to the list

            msg = email.message_from_file(open(f, "r"))
            msg_list.append(msg)
            #os.close(f)
    
    return msg_list