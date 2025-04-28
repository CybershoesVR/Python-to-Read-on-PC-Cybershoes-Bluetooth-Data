Upon rapid acceleration, the "Stick Pressed" signal briefly registers as True five times.
If you quickly press the button on the white receiver four times in succession, the receiver switches modes:
In this mode, "Stick Pressed" remains continuously True as long as fast movement is detected.

Regarding Tested Python Libraries:

💡 Summary:
| Topic                         | Possible via pygame? | Possible via PyQt5 Bluetooth? |
|-------------------------------|-----------------------|-------------------------------|
| See controller name           | ✅                     | ✅                             |
| See MAC address               | ❌                     | ✅                             |
| Controller numbering (0,1,2…) | ✅                     | ❌                             |
| Identify uniquely via MAC     | ❌                     | ✅                             |

The controller name in pygame:

"8 axis 16 button device with hat switch"

...unfortunately not "Cybershoes". PyQt5 correctly detects the name "Cybershoes2" and assigns the MAC address, but it does **not** read out Gamepad XY values. :)

**Conclusion:**  
If multiple gamepads are connected that all have the name "8 axis 16 button device with hat switch", you have to implement a selection check to pick the right one.  
Pygame numbers the controllers in the order they were connected.

![test BT](https://github.com/user-attachments/assets/6d136b17-43b7-4d4f-ba8e-2cd844866b04)

Stick pressed ist 5x als True, wenn man startet sehr schnell zu laufen.
Wenn man am weißen Receiver den Button 4x schnell hintereinander drückt, dann ändert sich das Verhalten des Receivers und Stick Pressed bleibt solange True, wie man schnell läuft.

💡 Zusammenfassung:
| Thema                        | Geht über pygame? | Geht über PyQt5 Bluetooth? |
|-------------------------------|-------------------|----------------------------|
| Name des Controllers sehen    | ✅                 | ✅                        |
| MAC-Adresse sehen             | ❌                 | ✅                        |
| Controller Nummern (0,1,2…)    | ✅                 | ❌                        |
| Eindeutig per MAC zuordnen     | ❌                 | ✅                        |

Der Name des Controllers in pygame:

"8 axis 16 button device with hat switch"

...leider nicht Cybershoes. PyQt5 erkennt den richtigen Namen "Cybershoes2" und ordnet die MAC Adresse zu, aber liest keine Gamepad xy Werte aus :)

Fazit: wenn mehrere Gamepads angeschlossen sind die den Namen tragen: "8 axis 16 button device with hat switch", muss man eine Abfrage machen um den richtigen auszuwählen. Pygame nummeriert die controller durch, in der Reihenfolge in der sie angeschlossen wurden.
