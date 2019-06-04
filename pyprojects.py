from lang import fr_lang, ge_lang, sp_lang

rawtext = "Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987), conocido como Leo Messi, es un futbolista argentino11 que juega como delantero en el Fútbol Club Barcelona y en la selección argentina, de la que es capitán. Considerado con frecuencia el mejor jugador del mundo y calificado en el ámbito deportivo como el más grande de todos los tiempos, Messi es el único futbolista en la historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de ellos en forma consecutiva– y el primero en recibir tres Botas de Oro. Con el Barcelona ha ganado siete títulos de La Liga y cuatro de la Liga de Campeones de la UEFA, así como tres títulos de la Copa del Rey. Goleador prolífico, ostenta los récords por más goles en la historia de La Liga (308), en una temporada de La Liga (50), en un año calendario (91), en un partido de la Liga de Campeones (cinco) y en más temporadas de la Liga de Campeones (cinco)."
text = rawtext.split(" ")

sp_lang = set(sp_lang)
ge_lang = set(ge_lang)
fr_lang = set(fr_lang)

sp_lang = list(sp_lang.intersection(text))
ge_lang = list(ge_lang.intersection(text))
fr_lang = list(fr_lang.intersection(text))

if len(sp_lang) > (len(ge_lang) and len(fr_lang)):
    print("The text is in spanish")
elif len(ge_lang) > (len(sp_lang) and len(fr_lang)):
    print("The text is in german")
elif len(fr_lang) > (len(ge_lang) and len(sp_lang)):
    print("The text is in french")
