import speech_recognition as sr
# biblioteca para conversão das palavras em números
numeros = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'duas': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seiscentos': 600,
    'setecentos': 700,
    'oitocentos': 800,
    'novecentos': 900,
    'mil': 1000
}
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio, language='pt-BR')
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Ouvindo...")

    while True:
        entrada = recognize_speech_from_mic(recognizer, microphone)

        if entrada["error"]:
            print("ERROR: {}".format(entrada["error"]))

        if entrada["transcription"]:
            print("Você disse: {}".format(entrada["transcription"]))

            palavras = entrada["transcription"].split()

            operation = None
            operands = []
            # palavra "sair" para finalizar
            if "sair" in palavras:
                print ('Saindo...')
                break  # sai do loop principal
            # quando o transcript selecionado (maior confiabilidade) for palavra, aqui será convertido em números
            if palavras[0] in numeros:
                num = numeros[palavras[0]]
                operands.append(num)
            elif palavras[0].isdigit():
                operands.append(int(palavras[0]))
            else:
                print("A entrada dos dados não é válida para o algoritmo.")
                break
            if palavras[2] in numeros:
                num = numeros[palavras[2]]
                operands.append(num)
            elif palavras[2].isdigit():
                operands.append(int(palavras[2]))
            else:
                print("A entrada dos dados não é válida para o algoritmo.")
                break
            for word in palavras:
                if word.lower() == "+" or word.lower() == "mais":
                    operation = "soma"
                elif word == "-" or word.lower() == "menos":
                     operation = "subtração"
                elif word.lower() == "vezes" or word.lower() == "x" or word.lower() == "multiplicado":
                    operation = "outra_operacao"
                elif word.lower() == "dividido" or word.lower() == "/":
                    operation = "outra_operacao"

            if operation == "soma":
                result = operands[0] + operands[1]
                print("{} + {} = {}".format(operands[0], operands[1], result))
            elif operation == "subtração":
                result = operands[0] - operands[1]
                print("{} - {} = {}".format(operands[0], operands[1], result))
            elif operation == "outra_operacao":
                print('O algoritmo trata apenas as operações de Adição e Subtração.')