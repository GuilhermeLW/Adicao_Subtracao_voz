import speech_recognition as sr
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