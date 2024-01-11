import pyautogui
import time

#Bot que envia imagem pra nego

class bot():
    def __init__(self):
        pass

    def marcar_posição_do_bot(self,x,y):
        time.sleep(3)
        pyautogui.click(x,y)

    def setar(self):
        time.sleep(3)
        print(pyautogui.position())

    def pesquisar(self,x,y,palavra_chave):
        pyautogui.click(x,y)
        pyautogui.write(palavra_chave)
        time.sleep(10)
        pyautogui.press("enter")
    
    def clicar(self,x,y):
        time.sleep(10)
        pyautogui.click(x,y)
    
    def clique_right(self,x,y):
        time.sleep(10)
        pyautogui.rightClick(x,y)

    def copiar_imagem(self,x,y,a1,b1):
        time.sleep(5)
        pyautogui.moveTo(x,y)
        time.sleep(3)
        pyautogui.click(a1,b1)

    def pesquisar2(self,x,y):
        time.sleep(5)
        pyautogui.click(x,y)

    def procurar_nome_no_whatsapp(self,x,y):
        time.sleep(3)
        pyautogui.click(x,y)

    def escrever_nome_no_whatsapp(self,palavra_chave):
        time.sleep(3)
        pyautogui.write(palavra_chave)

    def pressionar(self):
        time.sleep(5)
        pyautogui.press("enter")

def main():
    obter=bot()
    time.sleep(5)
    obter.marcar_posição_do_bot(663,740)
    time.sleep(10)
    obter.pesquisar(236,63,'Mensagens de bom dia')
    obter.clicar(295,199)
    obter.clique_right(102,655)
    obter.copiar_imagem(178,447,178,447)
    obter.pesquisar2(293,20)
    obter.pesquisar(236,63,'web.whatsapp.com')
    obter.procurar_nome_no_whatsapp(126,174)
    #Numero que o Usuario quiser digitar
    obter.escrever_nome_no_whatsapp("") #<-------------- Bote numero ou nome para pesquisar
    obter.clicar(162,175)
    for i in range(0,2,1): #<------------ (Numero inicializador,quantidade de mensagens para enviar,a cada passo)
        obter.clicar(737,674)
        obter.clique_right(737,674)
        obter.clicar(821,398)
        obter.pressionar()

if __name__ == "__main__":
    main()