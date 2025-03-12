import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):
    # width and height of components
    w = (width - margins["Left"] - margins["Right"] - 5 * gap) / 6
    h = height - margins["Top"] - margins["Bottom"]

    # draw path
    y=[margins["Top"]+(signal+1)*h/27 for signal in path]
    x=[width-margins["Right"]-w/2] # keyboard
    for i in [4, 3, 2, 1, 0]: # forward pass
        x.append(margins["Left"] + i * (w + gap) + w * 3/4)
        x.append(margins["Left"] + i * (w + gap) + w * 1/4)
    x.append(margins["Left"] + w * 3/4)  # reflector
    for i in [1, 2, 3, 4]: # backward pass
        x.append(margins["Left"] + i * (w + gap) + w * 1/4)
        x.append(margins["Left"] + i * (w + gap) + w * 3/4)
    x.append(width - margins["Right"] - w / 2) # lamp board


    # draw the path
    if len(path)>0:
        for i in range(1, 21):
            if i<10:
                color = "#43aa8b"
            elif i<12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i - 1], y[i - 1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # base coordinates
    x=margins["Left"]
    y=margins["Top"]

    # draw enigma components
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x+=w+gap

    # add name
    names=["Reflector", "Left", "Middle", "Right", "Plugborad", "Key/Lamp"]
    y= margins["Top"]*0.8
    for i in range(1, 6):
        x = margins["Left"] + w / 2 + i*(w+gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center=(x,y))
        screen.blit(title, text_box)




