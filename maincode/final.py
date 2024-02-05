from tkinter import *
import tkinter as tk
from tkinter import PhotoImage

def peso_tmb():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        idade = float(entry_idade.get())
        return peso, altura, idade
    except ValueError:
        print("Digite algum número.")
        return None


def calculo_mulher(peso, altura, idade):
    global tmb
    tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    return tmb

def calculo_homem(peso, altura, idade):
    global tmb
    tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    return tmb

tmb = 0

def calcular_tmb():
    dados = peso_tmb()
    if dados is not None:
        sexo = var_sexo.get()
        if sexo == 1:
            tmb = calculo_mulher(*dados)
        elif sexo == 2:
            tmb = calculo_homem(*dados)
        resultado_var.set(f"Sua taxa de metabolismo basal é {tmb:.2f} calorias por dia.")
    else:
        resultado_var.set ("Preencha os campos acima primeriro! ")


def calcular_necessidades(proposito, peso):
    proposito = var_proposito.get()
    peso = float(entry_peso.get())

    if proposito == 1:  # Perder
        necessidades = perder(peso)
    elif proposito == 2:  # Manter
        necessidades = manter(peso)
    elif proposito == 3:  # Ganhar
        necessidades = calculo(peso)
    
    proteina, carbo, gordura = necessidades
    resultado_proteina.set(f"Proteína: {proteina:.2f}g")
    resultado_carbo.set(f"Carboidrato: {carbo:.2f}g")
    resultado_gordura.set(f"Gordura: {gordura:.2f}g")

def perder(peso):
    proteina = peso * 2.5
    carbo = peso * 2
    gordura = peso * 1
    return proteina, carbo, gordura

def manter(peso):
    proteina = peso * 2.2
    carbo = peso * 2
    gordura = peso * 0.6
    return proteina, carbo, gordura

def calculo(peso):
    proteina = peso * 2.5
    carbo = peso * 3
    gordura = peso * 1.5
    return proteina, carbo, gordura

def personalizar_entradas():
    entry_peso.config(bg="#a9a9a9", bd=3, relief="solid", font=("Arial", 12))
    entry_altura.config(bg="##a9a9a9", bd=3, relief="solid", font=("Arial", 12))
    entry_idade.config(bg="#a9a9a9", bd=3, relief="solid", font=("Arial", 12))

def ganhar_tmb():
    global maispeso
    maispeso = tmb * 0.5
    if maispeso > 1:
        maispeso_var.set(f"Você precisa aumentar {maispeso:.2f} calorias por dia.")
    else:
        maispeso_var.set (f"Calcule seu TMB primeiro")
        return maispeso
    return maispeso
def manter_tmb():
    maispeso = tmb * 1
    if maispeso > 1:
        maispeso_var.set(f"Você precisa manter {maispeso:.2f} calorias por dia.")
    else:
        maispeso_var.set (f"Calcule seu TMB primeiro")
        return maispeso
    return maispeso

def perder_tmb ():
    maispeso = tmb * -0.2
    if maispeso <=-1:
        maispeso_var.set(f"Você precisa diminuir {maispeso:.2f} calorias por dia.")
    else:
        maispeso_var.set (f"Calcule seu TMB primeiro")
        return maispeso
    return maispeso

def exercios_leve ():
    exercicio = tmb * 0.2
    if exercicio >= 1:
        exercicio_var.set (f"você gasta {exercicio:.1f} amais do que seu tmb todos os dias ")
    else:
        exercicio_var.set ("Calcule seu TMB primeiro")
        return maispeso

def exercicio_medio ():
    global exercicio
    exercicio = tmb * 0.4
    if exercicio >= 1:
        exercicio_var.set (f"você gasta {exercicio:.1f} amais do que seu tmb todos os dias ")
    else:
        exercicio_var.set ("Calcule seu TMB primeiro")
        return exercicio
    

def exercicio_pesado ():
    exercicio = tmb * 0.8
    if exercicio >= 1:
        exercicio_var.set (f"voce gasta {exercicio:.1f} amais do que seu tmb todos os dias ")
    else:
        exercicio_var.set ("Calcule seu TMB primeiro")
        return exercicio
maispeso =0 
exercicio = 0  
 

janela = Tk()
janela.iconbitmap("\\Users\Rober\Desktop\CODE\imagens\images.ico")
logo_inicial = PhotoImage(file=r"C:\Users\Rober\Desktop\CODE\imagens\download (1).png")


janela.iconphoto(False, logo_inicial)
janela.title('TMB e Calculo de Nutrientes')
janela.geometry('420x330')
var_sexo = IntVar()
var_proposito = IntVar()
var_proposito_calorias = IntVar ()
maispeso= IntVar()
var_exercicios = IntVar ()

label_peso = Label(janela, text="Digite seu peso:")
label_altura = Label(janela, text="Digite sua altura em cm:")
label_idade = Label(janela, text="Digite sua idade:")
label_sexo = Label(janela, text="Selecione seu :")
label_proposito = Label(janela, text="Calcule seus macro:")
label_calorias = Label (janela, text = "Objetivo",font=('Arial', 10, 'bold'))
label_rotina = Label (janela, text="ROTINA",font=('Arial', 10, 'bold'))

entry_peso = Entry(janela)
entry_altura = Entry(janela)
entry_idade = Entry(janela)
radio_mulher = Radiobutton(janela, text="Mulher", variable=var_sexo, value=1)
radio_homem = Radiobutton(janela, text="Homem", variable=var_sexo, value=2)

radio_perder = Radiobutton(janela, text="Perder", variable=var_proposito, value=1, )
radio_manter = Radiobutton(janela, text="Manter", variable=var_proposito, value=2)
radio_calculo = Radiobutton(janela, text="ganhar", variable=var_proposito, value=3)


button_calcular_tmb = Button(janela, text="Calcular TMB", command=calcular_tmb)
button_calcular_necessidades = Button(janela, text="Calcular Necessidades",justify="left",
                                       command=lambda: calcular_necessidades(var_proposito.get(), 
                                                                             float(entry_peso.get())))

button_maispeso = Button(janela, text="Mais (kcal)",command=ganhar_tmb,width=11)
button_manterpeso = Button(janela, text="Manter (kcal)", command=manter_tmb, width=11)
buttons_perderpeso = Button(janela, text="Diminuir (kcal)",  command=perder_tmb, width=11)

button_exercicio_leve = Button (janela, text= "rotina leve",command= exercios_leve,width=11  )
button_exercicio_medio = Button (janela, text= "rotina media", command = exercicio_medio, width=11)
button_exercicio_pesado = Button (janela, text= "rotina pesada", command = exercicio_pesado, width=11)

#button_resultadofinal = Button (janela, text= "calcule seu resultado final", command = resultado_final, width=11)

resultado_var = StringVar()
resultado_proteina = StringVar()
resultado_carbo = StringVar()
resultado_gordura = StringVar()
maispeso_var = StringVar()
exercicio_var = StringVar ()
resultadofinal_var = IntVar()

label_resultado_tmb = Label(janela, textvariable=resultado_var)
label_resultado_proteina = Label(janela, textvariable=resultado_proteina)
label_resultado_carbo = Label(janela, textvariable=resultado_carbo)
label_resultado_gordura = Label(janela, textvariable=resultado_gordura)
label_resultado_mais_peso = Label(janela, textvariable=maispeso_var)
label_ganharpeso = Label (janela,textvariable=button_maispeso)
##label_resultadofinal = Label (janela,textvariable=resultadofinal_var)


label_exercicios = Label (janela,textvariable=exercicio_var)

label_peso.grid(row=0, column=0, sticky="E")
entry_peso.grid(row=0, column=1)

label_altura.grid(row=1, column=0, sticky="E")
entry_altura.grid(row=1, column=1)

label_idade.grid(row=2, column=0, sticky="E")
entry_idade.grid(row=2, column=1)

label_sexo.grid(row=3, column=0, sticky="E")
radio_mulher.grid(row=3, column=1, sticky="W")
radio_homem.grid(row=3, column=1, sticky="E")

label_proposito.grid(row=4, column=0, sticky="E")

#MACRO NUTRIENTES
radio_perder.grid(row=4, column=1, sticky="W",columnspan=10)
radio_manter.grid(row=4, column=1,pady=1,columnspan=2)
radio_calculo.grid(row=4, column=2, columnspan=1)
#---------------------------
#ROTINA DE EXERCECICIOS
# ROTINA DE EXERCÍCIOS
button_exercicio_leve.grid(row=1, column=8, columnspan=2, sticky='E', padx=(0, 50))
button_exercicio_medio.grid(row=2, column=8, columnspan=2, sticky='E', padx=(0, 50))
button_exercicio_pesado.grid(row=3, column=8, columnspan=2, sticky='E', padx=(0, 50))
# ---------------------------

button_calcular_tmb.grid(row=6, column=0, columnspan=2, padx=(50, 0))
button_calcular_necessidades.grid(row=7, column=0, columnspan=2, padx=(50, 0))
# MANTER/PERDER = PESO
button_maispeso.grid(row=6, column=8, columnspan=2, sticky='E', padx=(0, 50))
button_manterpeso.grid(row=7, column=8, columnspan=2, sticky='E', padx=(0, 50))
buttons_perderpeso.grid(row=8, column=8, columnspan=2, sticky='E', padx=(0, 50))
# -------------------------
#button_resultadofinal.grid (row=10, column=8, columnspan=2, sticky='E', padx=(0, 50))
#-------------------------

#label_resultadofinal.grid (row=14, column=0,columnspan=5)
label_resultado_tmb.grid(row=8, column=0, columnspan=5) #Button Resultado TMB
label_resultado_proteina.grid(row=9, column=0,columnspan=2)
label_resultado_carbo.grid(row=10, column=0,columnspan=2)
label_resultado_gordura.grid(row=11, column=0,columnspan=2)
label_resultado_mais_peso.grid (row=12, column=0, columnspan=5)
label_exercicios.grid (row=13, column=0,columnspan=5)
label_rotina.grid (row=0, column=8, columnspan=2, sticky='E', padx=(0, 70))
label_calorias.grid (row=5, column=8, columnspan=2, sticky='E', padx=(0, 70))

janela.mainloop()
