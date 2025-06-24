#Início 
import ttkbootstrap as ttkb
from interface import AppToDo

if __name__ == "__main__":
    app = ttkb.Window(themename="darkly")  # Ou outro tema como: litera, solar, cyborg...
    AppToDo(app)
    app.mainloop()
