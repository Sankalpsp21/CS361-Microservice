import time
import random

# HOW TO USE:
# 1. Open the file "sentenceRequest.txt" and write the equation you want to be converted into a sentence. (Ex "6*3")
# 2. Read the file "sentenceResponse.txt" and you will have your sentence.

def compute(operand1, operand2, symbol):
    if symbol == "+":
        return int(operand1) + int(operand2)
    elif symbol == "-":
        return int(operand1) - int(operand2)
    elif symbol == "*":
        return int(operand1) * int(operand2)
    elif symbol == "/":
        return int(operand1) / int(operand2)
    else:
        return "Error"
        
def makeSentence(line, sentences):
    # 0, 1 add 
    # 2, 3 mul 
    # 4, 5 div 
    # 6, 7 sub

    symbols = ["+", "-", "*", "/"]
    symbol = ""

    for i in symbols:
        if i in line:
            symbol = i
            break
    
    operands = line.split(symbol)
    result = compute(operands[0], operands[1], symbol)

    sentenceChoice = random.randint(0, 1)

    if symbol == "+":
        return sentences[0 + sentenceChoice].replace("OPERAND1", operands[0]).replace("OPERAND2", operands[1]).replace("RESULT", str(result))
    elif symbol == "*":
        return sentences[2 + sentenceChoice].replace("OPERAND1", operands[0]).replace("OPERAND2", operands[1]).replace("RESULT", str(result))
    elif symbol == "/":
        return sentences[4 + sentenceChoice].replace("OPERAND1", operands[0]).replace("OPERAND2", operands[1]).replace("RESULT", str(result))
    elif symbol == "-":
        return sentences[6 + sentenceChoice].replace("OPERAND1", operands[0]).replace("OPERAND2", operands[1]).replace("RESULT", str(result))
    
    return

if __name__ == "__main__":
    print("sentenceGenerator.py is running...")

    sentenceFile = open("sentences.txt", "r")
    sentences = sentenceFile.readlines()
    sentenceFile.close()
    
    while(True):
        file = open("sentenceRequest.txt", "r")
        line = file.readline()
        file.close()
        if line:
            break
    

    file = open("sentenceResponse.txt", "w")
    file.write(makeSentence(line, sentences))
    file.close()

    file = open("sentenceRequest.txt", "w")
    file.close()


