from flask import Flask  
app = Flask(__name__)  



@app.route('/')          
def hello_world():
    return 'Hello World!' 

###################################################################################################################################################################
##                                      The Actual code to the Block Chain
###################################################################################################################################################################

import hashlib

encoded = string.encode()

class Block:
    def __init__(self, index, timestamp, sender, receiver, amount, previousHash = ''):
        self.index = index
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.previousHash = previousHash
        self.hash = ''

        def calculateHash():
            return hashlib.sha256(index + previousHash + timestamp + sender + reciever + )
            pass
if __name__=="__main__":      
    app.run(debug=True) 