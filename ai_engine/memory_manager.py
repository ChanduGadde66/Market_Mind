chat_history=[]

def add_message(role,text):
    chat_history.append({"role":role,"text":text})

def get_history(limit=10):
    return chat_history[-limit:]