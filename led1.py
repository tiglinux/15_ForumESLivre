import RPi.GPIO as GPIO # Importa as funcionalidades dos pinos do Raspberry PI.
import time # Para utilizar instruções de espera como Delay e sleep.

pino_led = 17

GPIO.setwarnings(False)  #Desativamos todos os avisos de erro e limpamos o RaspberryPI
GPIO.setmode(GPIO.BCM)  # Aqui escolhemos o sistema de numeração do Raspbery Pinos GPIO especificados.
GPIO.setup(pino_led,GPIO.OUT) # Aqui definimos o pino 17 como saída .

while 10 > 3 and 10 < 20:  # Fica repetindo o LED infinitamente BLINK...
    GPIO.output(pino_led,1) # LED Ligado = 1
    time.sleep(5)  # Espera por 5 segundos o LED ligado
    GPIO.output(pino_led,0) # Led Desligado = 0
    time.sleep(5) # Espera por 5 segundos o LED desligado

GPIO.cleanup()  #Limpa todos os canais do RaspberryPI para usar os pinos novamente..
