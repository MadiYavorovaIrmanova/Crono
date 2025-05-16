import asyncio
import reflex as rx # type: ignore

from rxconfig import config

#Crono 
class Temporizador(rx.State):
    segundos_restantes_exposición:  int = 180
    segundos_restantes_refutacion1: int = 240
    segundos_restantes_refutacion2: int = 240
    segundos_restantes_conclusion:  int = 180
    esta_activo_exposicion:  bool = False
    esta_activo_refutacion1: bool = False
    esta_activo_refutacion2: bool = False
    esta_activo_conclusion:  bool = False
    poner_cero_exposicion: str = "0"
    poner_cero_refutacion1: str = "0"
    poner_cero_refutacion2: str = "0"
    poner_cero_conclusion: str = "0"
    exposicion: bool = True
    refutacion1: bool = False
    refutacion2: bool = False
    conclusion: bool = False
    boton_exposicion = "Exposición"
    boton_refutacion1 = "Refutación 1"
    boton_refutacion2 = "Refutación 2"
    boton_conclusion = "Conclusión"
    boton_iniciar = "Iniciar"
    boton_detener = "Detener"
    boton_reiniciar = "Reiniciar"
    


    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_exposicion(self):
        async with self:
            self.esta_activo_exposicion = True
        while True:
            async with self:
                if not self.esta_activo_exposicion or self.segundos_restantes_exposicion <= 0:
                        return
                self.segundos_restantes_exposicion -= 1
                if self.segundos_restantes_exposicion%60 < 10:
                    self.poner_cero_exposicion = "0"
                else:
                     self.poner_cero_exposicion = ""    
            await asyncio.sleep(1)
    
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_refutacion1(self):
        async with self:
            self.esta_activo_refutacion1 = True
        while True:
            async with self:
                if not self.esta_activo_refutacion1 or self.segundos_restantes_refutacion1 <= 0:
                        return
                self.segundos_restantes_refutacion1 -= 1
                if self.segundos_restantes_refutacion1%60 < 10:
                    self.poner_cero_refutacion1 = "0"
                else:
                     self.poner_cero_refutacion1 = ""    
            await asyncio.sleep(1)

    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_refutacion2(self):
        async with self:
            self.esta_activo_refutacion2 = True
        while True:
            async with self:
                if not self.esta_activo_refutacion2 or self.segundos_restantes_refutacion2 <= 0:
                        return
                self.segundos_restantes_refutacion2 -= 1
                if self.segundos_restantes_refutacion2%60 < 10:
                    self.poner_cero_refutacion2 = "0"
                else:
                     self.poner_cero_refutacion2 = ""
            await asyncio.sleep(1)

    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_conclusion(self):
        async with self:
            self.esta_activo_conclusion = True
        while True:
            async with self:
                if not self.esta_activo_conclusion or self.segundos_restantes_conclusion <= 0:
                        return
                self.segundos_restantes_conclusion -= 1
                if self.segundos_restantes_conclusion%60 < 10:
                    self.poner_cero_conclusion = "0"
                else:
                     self.poner_cero_conclusion = ""
            await asyncio.sleep(1)     
    
    

    @rx.event
    def detener(self):
        if self.exposicion:
            self.esta_activo_exposicion = False
        if self.refutacion1:
            self.esta_activo_refutacion1 = False
        if self.refutacion2:
            self.esta_activo_refutacion2 = False
        if self.conclusion:
            self.esta_activo_conclusion = False

    @rx.event
    def reiniciar(self):
        if self.exposicion:
            self.segundos_restantes_exposicion = 180
            self.esta_activo_exposicion = False
            self.poner_cero_exposicion = "0"
        if self.refutacion1:
            self.segundos_restantes_refutacion1 = 240
            self.esta_activo_refutacion1 = False
            self.poner_cero_refutacion1 = "0"
        if self.refutacion2:
            self.segundos_restantes_refutacion2 = 240
            self.esta_activo_refutacion2 = False
            self.poner_cero_refutacion2 = "0"
        if self.conclusion:
            self.segundos_restantes_conclusion = 180
            self.esta_activo_conclusion = False
            self.poner_cero_conclusion = "0"
    
    @rx.event
    def exposicion_activo(self):
        self.exposicion=True
        self.refutacion1= False
        self.refutacion2= False
        self.conclusion= False

    @rx.event
    def refutacion1_activo(self):
        self.exposicion=False
        self.refutacion1= True
        self.refutacion2= False
        self.conclusion= False
    
    @rx.event
    def refutacion2_activo(self):
        self.exposicion=False
        self.refutacion1= False
        self.refutacion2= True
        self.conclusion= False

    @rx.event
    def conclusion_activo(self):
        self.exposicion=False
        self.refutacion1= False
        self.refutacion2= False
        self.conclusion= True
    
    @rx.event
    def Castellano(self):
        self.boton_exposicion = "Exposición"
        self.boton_refutacion1 = "Refutación 1"
        self.boton_refutacion2 = "Refutación 2"
        self.boton_conclusion = "Conclusión"
        self.boton_iniciar = "Iniciar"
        self.boton_detener = "Detener"
        self.boton_reiniciar = "Reiniciar"

    @rx.event
    def Valenciano(self):
        self.boton_exposicion = "Exposició"
        self.boton_refutacion1 = "Refutació 1"
        self.boton_refutacion2 = "Refutació 2"
        self.boton_conclusion = "Conclusió"
        self.boton_iniciar = "Iniciar"
        self.boton_detener = "Aturar"
        self.boton_reiniciar = "Reiniciar"





def index() -> rx.Component:
# Welcome Page (Index)
    return rx.vstack(
        rx.hstack(  
            rx.image(src="Salesianos-Elche.jpg", width="150px", height="auto"),
            rx.button("Castellano", on_click=Temporizador.Castellano, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
            rx.button("Valenciano", on_click=Temporizador.Valenciano, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
            width="100%",
            top="10px",
            left="20px",
            align="start",
            padding="20px",
            justify="start",
        
        ),            
        rx.hstack(
            rx.cond(
                Temporizador.exposicion,
                rx.button(Temporizador.boton_exposicion, on_click=Temporizador.exposicion, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
                rx.button(Temporizador.boton_exposicion, on_click=Temporizador.exposicion, style={"background-color": "#cf2e2e", "color": "white"}),
            ),
            rx.cond(
                Temporizador.refutacion1,
                rx.button(Temporizador.boton_refutacion1, on_click=Temporizador.refutacion1, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
                rx.button(Temporizador.boton_refutacion1, on_click=Temporizador.refutacion1, style={"background-color": "#cf2e2e", "color": "white"}),
            ),
            rx.cond(
                Temporizador.refutacion2,
                rx.button(Temporizador.boton_refutacion2, on_click=Temporizador.refutacion2, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
                rx.button(Temporizador.boton_refutacion2, on_click=Temporizador.refutacion2, style={"background-color": "#cf2e2e", "color": "white"}),
            ),
            rx.cond(
                Temporizador.conclusion,
                rx.button(Temporizador.boton_conclusion, on_click=Temporizador.conclusion, style={"background-color":"white","color":"#cf2e2e","border":"2px  solid #cf2e2e","border-radius": "6px",}),
                rx.button(Temporizador.boton_conclusion, on_click=Temporizador.conclusion, style={"background-color": "#cf2e2e", "color": "white"}),
            ),
            #rx.heading(f"{Temporizador.exposicion} {Temporizador.refutacion1} {Temporizador.refutacion2} {Temporizador.conclusion}",size="9"),
            width="100%",
            margin="4px",
            align="center",
            padding="50px",
            height="100vh",
            justify="center",
             ),
#Caja 1
        
        rx.hstack(
            rx.cond(
                Temporizador.exposicion,
                rx.heading(f"0{Temporizador.segundos_restantes_exposicion//60} : {Temporizador.poner_cero_exposicion}{Temporizador.segundos_restantes_exposicion%60}",font_size="10em",font_family="Currier"),
                rx.cond(
                    Temporizador.refutacion1,
                    rx.heading(f"0{Temporizador.segundos_restantes_refutacion1//60} : {Temporizador.poner_cero_refutacion1}{Temporizador.segundos_restantes_refutacion1%60}",font_size="10em",font_family="Currier"),
                    rx.cond(
                        Temporizador.refutacion2,
                        rx.heading(f"0{Temporizador.segundos_restantes_refutacion2//60} : {Temporizador.poner_cero_refutacion2}{Temporizador.segundos_restantes_refutacion2%60}",font_size="10em",font_family="Currier"),
                        rx.cond(
                            Temporizador.conclusion,
                            rx.heading(f"0{Temporizador.segundos_restantes_conclusion//60} : {Temporizador.poner_cero_conclusion}{Temporizador.segundos_restantes_conclusion%60}",font_size="10em",font_family="Currier"),
                        ),
                    ),
                ),
            ),
            width="100%",
            margin="4px",
            align="center",
            justify="center",
            padding="100px",
            height="100vh",
        ),
        rx.hstack(    
            rx.cond(
            Temporizador.exposicion,
            rx.hstack(
                rx.cond(
                    Temporizador.esta_activo_exposicion,
                    rx.button(Temporizador.boton_detener, on_click=Temporizador.detener, style={
                        "background-color": "white",
                        "color": "#cf2e2e",
                        "border": "2px  solid #cf2e2e",
                        "border-radius": "6px",}
                    ),
                    rx.button(Temporizador.boton_iniciar, on_click=Temporizador.iniciar_cuenta_regresiva_exposicion, style={
                        "background-color": "white",
                        "color": "#cf2e2e",
                        "border": "2px  solid #cf2e2e",
                        "border-radius": "6px",},
                    ),
                    
                ),
                rx.button(Temporizador.boton_reiniciar, on_click=Temporizador.reiniciar, style={
                    "background-color": "white",
                    "color": "#cf2e2e",
                    "border": "2px  solid #cf2e2e",
                    "border-radius": "6px",}
                ),
            
            border_radius="2px",
            width="400px",
            margin="4px",
            padding="100px"
            ),
            rx.cond(
                Temporizador.refutacion1,
                rx.hstack(
                    rx.button(Temporizador.boton_iniciar, on_click=Temporizador.iniciar_cuenta_regresiva_refutacion1, style={
                        "background-color": "white",
                        "color": "#cf2e2e",
                        "border": "2px  solid #cf2e2e",
                        "border-radius": "6px",},
                    ),
                    rx.button(Temporizador.boton_detener, on_click=Temporizador.detener, style={
                        "background-color": "white",
                        "color": "#cf2e2e",
                        "border": "2px  solid #cf2e2e",
                        "border-radius": "6px",}
                    ),
                    rx.button(Temporizador.boton_reiniciar, on_click=Temporizador.reiniciar, style={
                        "background-color": "white",
                        "color": "#cf2e2e",
                        "border": "2px  solid #cf2e2e",
                        "border-radius": "6px",}
                    ),
                border_radius="2px",
                width="400px",
                margin="4px",
                height="100vh",
                padding="4px",
                ),
                rx.cond(
                    Temporizador.refutacion2,
                    rx.hstack(
                        rx.button(Temporizador.boton_iniciar, on_click=Temporizador.iniciar_cuenta_regresiva_refutacion2, style={
                            "background-color": "white",
                            "color": "#cf2e2e",
                            "border": "2px  solid #cf2e2e",
                            "border-radius": "6px",},
                        ),
                        rx.button(Temporizador.boton_detener, on_click=Temporizador.detener, style={
                            "background-color": "white",
                            "color": "#cf2e2e",
                            "border": "2px  solid #cf2e2e",
                            "border-radius": "6px",}
                        ),
                        rx.button(Temporizador.boton_reiniciar, on_click=Temporizador.reiniciar, style={
                            "background-color": "white",
                            "color": "#cf2e2e",
                            "border": "2px  solid #cf2e2e",
                            "border-radius": "6px",}
                        ),
                    border_radius="2px",
                    width="400px",
                    margin="4px",
                    padding="4px"
                    ),
                    rx.cond(
                        Temporizador.conclusion,
                        rx.hstack(
                            rx.button(Temporizador.boton_iniciar, on_click=Temporizador.iniciar_cuenta_regresiva_conclusion, style={
                                "background-color": "white",
                                "color": "#cf2e2e",
                                "border": "2px  solid #cf2e2e",
                                "border-radius": "6px",},
                            ),
                            rx.button(Temporizador.boton_detener, on_click=Temporizador.detener, style={
                                "background-color": "white",
                                "color": "#cf2e2e",
                                "border": "2px  solid #cf2e2e",
                                "border-radius": "6px",}
                            ),
                            rx.button(Temporizador.boton_reiniciar, on_click=Temporizador.reiniciar, style={
                                "background-color": "white",
                                "color": "#cf2e2e",
                                "border": "2px  solid #cf2e2e",
                                "border-radius": "6px",}
                            ),
                        border_radius="2px",
                        width="400px",
                        margin="4px",
                        padding="4px"
                        ),
                    ),
                ),
            ),
        ),
        
        ),
        rx.hstack(
            rx.image(src="somos-futuro-principal.png", width="200px", height="auto"),
            width="100%",
            align="end",
            justify="end",
            
        ),
        align="center", background_color="#ff5062", padding="20px", width="100%", height="100vh",
    )

app = rx.App()
app.add_page(index)