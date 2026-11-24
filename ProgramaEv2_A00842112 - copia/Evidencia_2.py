import PySimpleGUI as sg
import csv
import pandas as pd
import webbrowser as wb

def est_1():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[0].mean()
    return valor
def est_2():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[1].mean()
    return valor
def est_3():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[2].mean()
    return valor
def est_4():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[3].mean()
    return valor
def est_5():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[4].mean()
    return valor

def est_6():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Ene"].sum()
    return valor
def est_7():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Feb"].sum()
    return valor
def est_8():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Mar"].sum()
    return valor
def est_9():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Abr"].sum()
    return valor
def est_10():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["May"].sum()
    return valor
def est_11():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Jun"].sum()
    return valor
def est_12():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df["Jul"].sum()
    return valor
def est_13():
    valor= est_6() + est_7() + est_8() + est_9() + est_10() + est_11() + est_12()
    return valor
def est_14():
    df = pd.read_csv("Evidencia_2.csv")
    valor= df.iloc[4].count()
    return valor
def est_15():
    valor= est_13()/est_14()
    return valor
    
def base1():
    df = pd.read_csv("Evidencia_datos.csv")
    valor1 = df["Victima de robo"].sum()
    valor2 = df["Victima de robo"].count()
    valor3= (valor1/valor2)*100
    return valor3
def base2():
    df = pd.read_csv("Evidencia_datos.csv")
    valor1 = df["Testigo de robo"].sum()
    valor2 = df["Testigo de robo"].count()
    valor3= (valor1/valor2)*100
    return valor3
def base3():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Percepciondia"].mode()
    valor1= int(valor)
    return valor1
def base4():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Percepcionnoche"].mode()
    valor1= int(valor)
    return valor1
def base5():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Genero"].mode()
    valor1= int(valor)
    return valor1
def base5_1():
    if base5 == "1":
        gen = "Masculino"
    else:
        gen = "Femenino"
    return gen
def base6():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Edad"].mode()
    valor1 = int(valor)
    return valor1
def base7():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Edad"].max()
    return valor
def base8():
    df = pd.read_csv("Evidencia_datos.csv")
    valor = df["Edad"].min()
    return valor
def base9():
    df = pd.read_csv("Evidencia_datos.csv")
    valor1 = df["Percepcionnoche"].sum()
    valor2 = df["Percepciondia"].sum()
    valor3 = df["Percepciondia"].count()
    valor4 = (valor1 + valor2)/2
    valor5 = valor4/valor3
    return valor5
    

def intro():
    txt_int = sg.Text("""La colonia Tecnológico, ubicada en la ciudad de Monterrey, es conocida como el área estudiantil y universitaria principal de esta ciudad
y se caracteriza por la constante circulación de estudiantes, profesores y otras personas vinculadas al ámbito educativo. 
Según datos proporcionados por la Fiscalía General de Justicia del estado Nuevo León, en las cifras del último período publicadas por la misma (Enero - Julio 2024),
la tasa de robos fue de un total de 1,587 casos y adicionalmente se reporta que los casos de inseguridad, robos y delincuencia no han disminuido significativamente en los últimos años.
Teniendo en cuenta las cifras proporcionadas y analizando la situación hemos identificado una posible riesgo o estado de vulnerabilidad en los estudiantes
frente a la inseguridad de la ciudad, y mas específicamente de la colonia.  Por ende deseamos recolectar información especifica sobre la tasa de inseguridad en la colonia tecnológico y las experiencias de los estudiantes frente a esta situación.""")
    btn_int = sg.Button("Salir de la ventana de introducción", key = "BTN1")
    btn_vid = sg.Button("Ver propuesta", key = "BTN2")
    layout=[[txt_int],[btn_int,btn_vid]]
    window= sg.Window("Introducción", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BTN1":
            window.close()
        if event == "BTN2":
            intro = "https://drive.google.com/file/d/12N1iNBgbvGRIyEUQYRw_S-8cy245jDCd/view?usp=sharing "
            wb.open_new_tab(intro)
            

def estadisticas():
    df = pd.read_csv("Evidencia_2.csv")
    est1= df.max().max()
    est2 = est_1()
    est3 = est_2()
    est4 = est_3()
    est5 = est_4()
    est6 = est_5()
    
    est7 = est_6()
    est8 = est_7()
    est9 = est_8()
    est10 = est_9()
    est11= est_10()
    est12= est_11()
    est13= est_12()
    est14= est_15()
    txt_est1= sg.Text(f"El Número máximo de robos totales es de: {est1:.0f}")
    txt_est2= sg.Text(f"El promedio de robos a casa habitación es de: {est2:.0f}")
    txt_est3= sg.Text(f"El promedio de robos a negocios es de: {est3:.0f}")
    txt_est4= sg.Text(f"El promedio de robos a persona es de: {est4:.0f}")
    txt_est5= sg.Text(f"El promedio de robos de vehículos es de: {est5:.0f}")
    txt_est6= sg.Text(f"El promedio de robos simples es de: {est6:.0f}")
    txt_est7= sg.Text(f"El total de robos en enero fue de: {est7:.0f}")
    txt_est8= sg.Text(f"El total de robos en febrero fue de: {est8:.0f}")
    txt_est9= sg.Text(f"El total de robos en marzo fue de: {est9:.0f}")
    txt_est10= sg.Text(f"El total de robos en abril fue de: {est10:.0f}")
    txt_est11= sg.Text(f"El total de robos en mayo fue de: {est11:.0f}")
    txt_est12= sg.Text(f"El total de robos en junio fue de: {est12:.0f}")
    txt_est13= sg.Text(f"El total de robos en julio fue de: {est13:.0f}")
    txt_est14= sg.Text(f"El promedio mensual de robos en Monterrey durante 2024 es: {est14:.0f}")
    btn2 = sg.Button("Salir de estadísticas", key= "BTN2")
    layout = [[txt_est1],[txt_est2],[txt_est3],[txt_est4],[txt_est5],[txt_est6],
              [txt_est7],[txt_est8],[txt_est9],[txt_est10],[txt_est11],[txt_est12],[txt_est13],[txt_est14],
              [btn2]]
    window= sg.Window("Estadísticas", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BTN2":
            window.close()
            
def estadistica2():
    est1= base1()
    est2= base2()
    est3= base3()
    est4= base4()
    est5= base5_1()
    est6= base6()
    est7= base7()
    est8= base8()
    est9= base9()
    txt = sg.Text("Las estadisticas recopiladas de nuestra base de datos son:")
    txt1= sg.Text(f"El porcentaje de victimas de robo en el distrito tec es de: {est1:.2f}%")
    txt2= sg.Text(f"El porcentaje de testigos de robo en el distrito tec es de: {est2:.2f}%")
    txt3= sg.Text(f"La moda del sentimiento de inseguridad en horario diurno es de: {est3}")
    txt4= sg.Text(f"La moda del sentimiento de inseguridad en horario nocturno es de: {est4}")
    txt5= sg.Text(f"El sentimiento de inseguridad en promedio de ambos turnos en el distrito tec es de: {est9:.2f}")
    txt6= sg.Text(f"Partiparon personas desde {est8} años hasta {est7} años")
    txt7= sg.Text(f"Teniendo mayor particpación de estudiantes de {est6} años, del género {est5}.")
    btn1 = sg.Button("Salir de las estadísticas", key = "BTN1")
    
    layout = [[txt],
              [txt1],[txt2],[txt3],[txt4],[txt5],[txt6],[txt7],
              [btn1]]
    window= sg.Window("Estadísticas recopiladas por nuestro formulario", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BTN1":
            window.close()
            
def encuesta():
    txt1= sg.Text("Ayudanos a contestar este formulario")
    txt2 = sg.Text("Género(1:Hombre, 2:Mujer, 3:Otros):")
    opciones = ("1","2","3")
    cb1 = sg.Combo(opciones, key= "CMB1")
    txt3= sg.Text("Edad:")
    inp1= sg.Input("", key="INP1")
    txt10 = sg.Text("Rol en la comunidad (1:Estudiante, 2:Profesor, 3:Residente):")
    cb2 = sg.Combo(opciones, key= "CMB2")
    
    txt4 = sg.Text("¿Vives en la zona tec?:")
    rad1= sg.Radio("Sí", group_id="Radio", key= "RADIO1" )
    rad2= sg.Radio("No", group_id="Radio", key= "RADIO2" )
    
    txt5= sg.Text("Percepción de inseguridad en la zona tec de 6am-6pm (0 muy bajo, 5 muy alto)")
    per_in1= sg.Slider(range=(0,5), orientation="horizontal", enable_events= True, key= "SLD1")
    txt6= sg.Text("Percepción de inseguridad en la zona tec 7pm-5am (0 muy bajo, 5 muy alto)")
    per_in2= sg.Slider(range=(0,5), orientation="horizontal", enable_events= True, key= "SLD2")
    txt7 = sg.Text("¿Has sufrido de robo el último año en la zona tec?:")
    rad3= sg.Radio("Sí", group_id="Radio1", key= "RAD1" )
    rad4= sg.Radio("No", group_id="Radio1", key= "RAD2" )
    txt8 = sg.Text("¿Has sido testigo de algún robo el último año en la zona tec?:")
    rad5= sg.Radio("Sí", group_id="Radio2", key= "RAD3" )
    rad6= sg.Radio("No", group_id="Radio2", key= "RAD4" )
    opciones2= ("N/A","ROBO A CASA HABITACION", "ROBO A NEGOCIO","ROBO A PERSONA","ROBO DE VEHICULO","ROBO SIMPLE")
    txt9 = sg.Text("Categoría del robo:")
    cb3 = sg.Combo(opciones2, key= "CMB3")
    btn1= sg.Button ("Guardar Datos", key="BTNDATOS")
    btn2= sg.Button ("Salir", key = "BTNSALIR")
    
    layout = [[txt1],
              [txt2, cb1],
              [txt3, inp1],
              [txt10,cb2],
              [txt4, rad1, rad2],
              [txt5, per_in1],
              [txt6, per_in2],
              [txt7, rad3, rad4],
              [txt8,rad5,rad6],
              [txt9,cb3],
              [btn1, btn2]]
    
    window = sg.Window("Formulario", layout, resizable = True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "BTNDATOS":
            Vent= sg.popup("Sus datos se han guardado con éxito.", title = "Guardado")
            valor1= int(values["CMB1"])
            valor2= int(values["INP1"])
            valor3= int(values["CMB2"])
            valor4= values["RADIO1"]
            valor5= int(values["SLD1"])
            valor6= int(values["SLD2"])
            valor7= values["RAD1"]
            valor8= values["RAD3"]
            valor9= values["CMB3"]
            
            if valor4 == True:
                valor4 = 1
            else:
                valor4 = 2
            if valor7 == True:
                valor7 = 1
            else:
                valor7 = 2
            if valor8 == True:
                valor8 = 1
            else:
                valor8 = 2
            
            nom_arch = "Evidencia_datos.csv"
            arch = open(nom_arch, mode = "a", newline= "")
            w_arch = csv.writer(arch, delimiter = ",")
        
            if arch.tell() == 0:
                w_arch.writerow(["Género","Edad","Rol","Vive en zona Tec","Percepción de día","Percepción de noche","Victima de robo","Testigo de robo","Categoría"])

            valores = [valor1, valor2, valor3,valor4,valor5,valor6,valor7,valor8,valor9]
            w_arch.writerow(valores)
            arch.close()
        if event == "BTNSALIR":
            window.close()


def estadisticasbd():
    # Ventana de inicio de sesión
    def ventana_login():
        # Etiquetas
        txt1 = sg.Text("Contraseña:")
        # Entradas
        inp1 = sg.Input("", key="inp_contraseña", password_char="*")
        # Imagen
        
        img = sg.Image(filename="imseg.png")

        # Botones
        btn1 = sg.Button("Entrar", key="btn_entrar")
        btn2 = sg.Button("Volver", key="btn_cerrar")

        # Layout de la ventana
        layout = [
            [txt1, inp1],
            [img],
            [btn1, btn2]
        ]

        # Crear la ventana
        window = sg.Window('Inicio de Sesión', layout, size=(400,400), resizable=True, grab_anywhere=True)

        # Bucle principal de eventos
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'btn_cerrar':
                break
            
            if event == 'btn_entrar':
                contraseña = values['inp_contraseña']
                
                # Determinar si la contraseña es correcta
                if contraseña == "tecmty":
                    window.close()
                    ventana_menu_principal()
                else:
                    sg.popup("Incorrecto, vuelve a intentarlo.", title = "Incorrecto")
        
        window.close()

    # Ventana del menú principal
    def ventana_menu_principal():
        
        
        # Imágenes para los botones
        btn1 = sg.Button("Introducción", key="btn1")
        btn2 = sg.Button("Estadísticas", key="btn2")
        btn3 = sg.Button("Formulario", key="btn3")
        btn4 = sg.Button("Saber más...", key="btn4")
        btn5 = sg.Button("Estadísticas de la recolección de datos", key = "btn5")
        btn6 = sg.Button("Ver video explicación César Leal", key= "btn6")
        im1= sg.Image(filename="Im4.png",key="IM1")
        im2= sg.Image(filename="Im1.png",key="IM2")
        im3= sg.Image(filename="Im2.png",key="IM3")
        im4= sg.Image(filename="Im3.png",key="IM4")
        im5 = sg.Image(filename="Im5.png",key="IM5")

        # Botones adicionales
        btn_mapa_ayuda = sg.Button("Mapa de ayuda", button_color=('white', 'gray'), key="btn_mapa_ayuda", size=(30, 2))
        btn_salir = sg.Button("Salir", button_color=('red','gray'), key="btn_salir", size=(25, 2))

        # Layout de la ventana del menú principal
        layout = [[im1, im2, im3,im5, im4],
            [btn1, btn2, btn3, btn5, btn4],
            [btn_mapa_ayuda, btn_salir]]

        # Crear la ventana
        window = sg.Window('Menú Principal', layout, size=(1300, 500), resizable=True, grab_anywhere=True, element_justification='center')

          # Bucle principal de eventos
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "btn_salir":
                break

            # Aquí puedes manejar eventos de los botones
            if event == "btn1":
                intro()

            if event == "btn2":
                estadisticas()

            if event == "btn3":
                encuesta()
                
            if event == "btn4":
                video = "https://youtu.be/QO8sc2-LAzA?si=XwkBg4Hf31PEvWja"
                wb.open_new_tab(video)
                
            if event == "btn5":
                estadistica2()
                
            elif event == "btn_mapa_ayuda":
                url = "https://maps.app.goo.gl/DP57pU2rNtBFfAE67"
                wb.open_new_tab(url)
            elif event == "btn6":
                url = "https://youtu.be/rf5VjDke1YM"
                wb.open_new_tab(url)

            
        window.close()

    # Llamar a la ventana de inicio de sesión
    ventana_login()

# Llamar a la función principal
estadisticasbd()