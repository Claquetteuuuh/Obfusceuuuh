import random
import re

def gen_quotes(n: int):
    quotes = ['"', "'"]
    string_tab = []
    for i in range(n):
        quote = random.choice(quotes)
        string_tab.append(quote)
        string_tab.append(quote)

    return "".join(string_tab)

def interrupt(payload: str):
    """
        Une fonction vraiment dégueulasse fait a la zeub a minuit si vous avez mieux pour mettre des quotes seulement entre les Cmdlet je suis preneur
    """
    fnl = ""
    stop = False
    stop_quote = False
    crochet = 0
    separator = [" ", ";", "'", '"', "`", "=", ","]
    payload_divided_if = payload.split("if")
    for j in range(len(payload_divided_if)):
        payload_divided_else = payload_divided_if[j].split("else")
        for h in range(len(payload_divided_else)):
            payload_divided_catch = payload_divided_else[h].split("catch")
            for x in range(len(payload_divided_catch)):
                payload_divided_func = payload_divided_catch[x].split("function")
                for y in range(len(payload_divided_func)):
                    payload_divided_try = payload_divided_func[y].split("try")
                    for z in range(len(payload_divided_try)):
                        payload_divided_while = payload_divided_try[z].split("while")
                        for a in range(len(payload_divided_while)):
                            payload_list = list(payload_divided_while[a])
                            payload_list.append("¨")
                            i = 0

                            while payload_list[i] != "¨":
                                if payload_list[i] == "$" or payload_list[i] == "." or payload_list[i] == "-":
                                    stop = True
                                elif payload_list[i] == "'" or payload_list[i] == '"':
                                    if stop_quote:
                                        stop_quote = False
                                    else:
                                        stop_quote = True
                                elif payload_list[i] == "[" :
                                    crochet += 1
                                elif payload_list[i] == "]":
                                    crochet -= 1            
                                elif  payload_list[i] in separator:
                                    stop = False
                                elif crochet == 0 and stop == False and stop_quote == False and i != 0 and re.match("[a-zA-Z]", payload_list[i-1]) and re.match("[a-zA-Z]", payload_list[i]) and re.match("[a-zA-Z]", payload_list[i+1]):
                                    payload_list.insert(i, gen_quotes(1))
                                    i += 1
                                i +=1
                            payload_list.pop()
                            fnl += "".join(payload_list)

                            if a < len(payload_divided_while) -1:
                                fnl += "while"

                        if z < len(payload_divided_try) -1:
                            fnl += "try"

                    if y < len(payload_divided_func) -1:
                        fnl += "function"

                if x < len(payload_divided_catch) -1:
                    fnl += "catch"
            if h < len(payload_divided_else) -1:
                fnl += "else"
        if j < len(payload_divided_if) -1:
            fnl += "if"
    return fnl

if __name__ == "__main__":
    print(interrupt("mange tes.grand.mort[stp]; $cailloux = Test.dd; "))