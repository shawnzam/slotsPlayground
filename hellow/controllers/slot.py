# coding: utf8
# try something like
import random
def index(): 
    slots = db().select(db.slot.ALL)
    return dict(slots=slots)

def show():
    id = request.args[0]
    slot = db.slot(id)
    return str(isWinner(slot.odds)) + " | "  + str(slot.odds)
    
def isWinner(odds):
    if odds > random.randint(0, 9):
        return True
    else: return False
