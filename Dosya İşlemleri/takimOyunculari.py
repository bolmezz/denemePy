def bilgiler(satir, fener, gs, bjk):
    isim = satir[0]
    takim = satir[1]

    if takim == "Fenerbahçe":
        bilgi = isim + " -----> " + takim + "\n"
        fener.append(bilgi)
    elif takim == "Galatasaray":
        bilgi = isim + " -----> " + takim + "\n"
        gs.append(bilgi)
    elif takim == "Beşiktaş":
        bilgi = isim + " -----> " + takim + "\n"
        bjk.append(bilgi)


with open("oyuncular", "r", encoding="utf-8") as file:
    lines = file.readlines()
    fener = list()
    gs = list()
    bjk = list()

    for i in lines:
        i = i[:-1]
        satir = i.split(",")
        bilgiler(satir, fener, gs, bjk)

    with open("fb.txt", "w", encoding="utf-8") as fileFB:
        fileFB.writelines(fener)
    with open("gs.txt", "w", encoding="utf-8") as fileGS:
        fileGS.writelines(gs)
    with open("bjk.txt", "w", encoding="utf-8") as fileBJK:
        fileBJK.writelines(bjk)
