
#Mit eget sjove papirspil.py
def spil(): #har lavet en def funktion til mit spil, så hvis det virkelig skal blive til noget:

    color_picks = ('rød', 'grøn', 'blå', 'gul')
    number_picks = (1, 2, 3, 4, 5, 6, 7, 8)
    udsagn = {
          1: 'Du er en rose',
          2: 'Du er en sol',
          3: 'Du er en stjerne',
          4: 'Du er en måne',
          5: 'Du er en sky',
          6: 'Du er en regnbue', 
          7: 'Du er en snefnug',
          8: 'Du er en ildflue'
    }

    print('Tak for at deltage i mit sjove papirspil, lad os komme i gang!')
    print('Er du klar til at spille? skriv ja eller nej!')

    svar = input('ja/nej: ')

    while svar != 'ja' and svar != 'nej':
                print('Det er ikke et gyldigt svar, prøv igen!')
                svar = input('ja/nej: ')

    print('Vi starter om du er klar eller ej!')

    picked_color = input('Vælg en farve mellem (rød, grøn, blå, gul): ')
    while picked_color not in color_picks:
        print('Det er en ugyldig farve, prøv igen!')
        picked_color = input('Vælg en farve mellem (rød, grøn, blå, gul): ')

    print('Du har valgt farven:', picked_color, 'og nu skal du vælge et tal mellem 1 og 8!')

    
    while True:
          try:
                picked_number = int(input('Vælg et tal mellem 1 og 8: '))
                if 1 <= picked_number <= 8:
                      break
                else:
                        print('Det er ikke et gyldigt tal, prøv igen!')
          except ValueError:
                print('Det er ikke et gyldigt tal, prøv igen!')
    
    while picked_number not in number_picks:
        print('Det er et ugyldigt tal, prøv igen!')
        picked_number = int(input('Vælg et tal mellem 1 og 8: '))

    print('Du har valgt tallet:', picked_number, 'og farven:', picked_color, ' lad os se hvad  det siger om dig!')

    print('Det siger', udsagn[picked_number])
spil()#kalder funktionen spil() for at starte spillet




    
    

    
