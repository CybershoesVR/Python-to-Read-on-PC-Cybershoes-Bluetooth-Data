import pygame
import sys

def main():
    # pygame initialisieren
    pygame.init()
    pygame.joystick.init()

    # Nach dem Joystick mit Namen "Cybershoes2" suchen
    joystick = None
    for i in range(pygame.joystick.get_count()):
        j = pygame.joystick.Joystick(i)
        j.init()
        print(f"Gefundener Controller #{i}: {j.get_name()}")
        if j.get_name() ==  "8 axis 16 button device with hat switch": #"Cybershoes2":
            joystick = j
            break

    if joystick is None:
        print("Controller 'Cybershoes2' nicht gefunden.")
        pygame.quit()
        sys.exit(1)

    print("✔ Gefunden:", joystick.get_name())
    print(f"Anzahl Achsen: {joystick.get_numaxes()}")
    print(f"Anzahl Buttons: {joystick.get_numbuttons()}")

    # Standard‑Belegung: Achse 0 = X, Achse 1 = Y, Button 9 = Stick-Click
    AXIS_X = 0
    AXIS_Y = 1
    BUTTON_STICK = 13

    clock = pygame.time.Clock()
    try:
        while True:
            # Event‑Pump, damit pygame den Joystick aktualisiert
            pygame.event.pump()

            # Linken Stick auslesen
            x = joystick.get_axis(AXIS_X)
            y = -joystick.get_axis(AXIS_Y)
            stick_pressed = joystick.get_button(BUTTON_STICK)

            # Ausgabe
            print(f"X = {x:+.3f}, Y = {y:+.3f}, StickPressed = {stick_pressed}")

            # 30 Hz Abtastrate
            clock.tick(30)

    except KeyboardInterrupt:
        print("\nBeendet per STRG+C")

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
