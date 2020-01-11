DATEI = "Popeliniere_Daira_pl.txt"
stopwords=['peut-être', 'bien-loin', 'peut-être', 'de-là', 'dès-lors', 'bien-tôt', 'long-temps', 'bien-tôt', 'tout-à-coup', 'détourne-toi', 'laiſſe-moi', 'écriai-je', 'toi-même', 'moi-même', 'ſoit-il', 'laiſſe-moi', 'écriai-je', 'tout-à-coup', 'long-temps', 'moi-même', 'Croirez-vous', 'ſur-tout', 'juſques-là', 'moi-même', 'dis-je', 'vois-je', 'écriai-je', 'eſt-il', 'continua-t', 'aurai-je', 'Dois-je', 'moi-même', 'bien-tôt', 'entre-coupée', 'bien-tôt', 'écria-t', 'long-temps', 'dit-il', 'écriai-je', 'vous-même', 'Ecoutez-moi', 'fut-elle', 'répondis-je', 'au-delà', 'moi-même', 'oſai-je', 'moi-même', 'lui-meme', 'dit-elle', 'peut-être', 'vous-même', 'celui-là', 'dit-elle', 'criai-je', 'a-t-il', 'prochez-vous', 'vous-même', 'vous-même', 'par-tout', 'moi-même', 'moi-même', 'criai-je', 'dra-t-elle', 'peut-être', 'relevez-la', 'portez-lui', 'au-delà', 'long-temps', 'tout-à-coup', 'apprends-lui', 'ſur-tout', 'dit-il', 'ici-même', 'dis-je', 'dites-vous', 'continuai-je', 'laiſſez-moi', 'lui-même', 'ques-là', 'moi-même', 'eut-il', 'moi-même', 'lui-même', 'lui-même', 'lui-même', 'Rendez-moi', 'dit-il', 'ajouta-t', 'moi-même', 'long-temps', 'dit-il', 'trop-tôt', 'peut-être', 'vous-même', 'devins-je', 'reprit-il', 'vous-même', 'lui-même', 'étois-je', 'juſques-là', 'tout-à-coup', 'pouvois-je', 'vois-je', 'moment-là', 'auſſi-bien', 'ai-je', 'premiers-là', 'small-cap', 'dira-t', 'prendra-t', 'moi-même', 'ſur-tout', 'peut-être', 'diſois-je', 'moi-même', 'tout-à-la-fois', 'tout-à-fait', 'avoit-on', 'écriai-je', 'tirez-vous', 'moi-même', 'tout-à-coup', 'dis-je', 'reprit-il', 'toi-même', 'écria-t-il', 'peut-être', 'écria-t-il', 'êtes-vous', 'ceſſera-t-il', 'Avez-vous', 'toit-il', 'tout-à-fait', 'long-temps', 'tinua-t-il', 'moi-même', 'à-coup', 'long-temps', 'vous-même', 'Voyez-moi', 'écriai-je', 'ci-devant', 'ſuffiſent-ils', 'diſois-je', 'eſt-ce', 'eſt-ce', 'demie-voix', 'reprit-il', 'juſques-là', 'repréſentera-t-on', 'peu-à-peu', 'dis-je', 'ſoi-même', 'peut-être', 'Détournons-nous', 'elle-même', 'au-travers', 'dis-je', 'peut-être', 'peut-être', 'moi-même', 'moi-même', 'continua-t-il', 'tout-puiſſant', 'peut-être', 'auſſi-tôt', 'peu-à-peu', 'très-peu', 'par-tout', 'lui-même', 'moi-même', 'tinua-t-il', 'étois-je', 'pouvois-je', 'elle-même', 'dis-je', 'ajoutai-je', 'bien-tôt', 'lui-même', 'dis-je', 'vous-même', 'réſous-tu', 'reſte-t-il', 'toi-même', 'au-delà', 'vous-même', 'entendez-moi', 'entends-je', 'Eſt-ce', 'devient-il', 'diſois-je', 'au-delà', 'ſentis-je', 'tout-à-coup', 'au-deſſus', 'moi-même', 'auſſi-tôt', 'peut-être', 'tout-à-coup', 'non-ſeulement', 'eux-mêmes', 'repetoient-ils', 'au-dedans', 'tout-puiſſans', 'au-dedans', 'moi-mê', 'continua-t-il', 'dit-il', 'écoute-moi', 'fallût-il', 'écriai-je', 'frappe-moi', 'tout-à', 'tout-à-coup', 'tout-à-coup', 'moi-même', 'lui-même', 'dois-tu', 'peut-être', 'moi-même', 'dit-il', 'lui-même', 'Rends-moi', 'rends-moi', 'Vois-moi', 'tout-à-coup', 'moi-même', 'par-là', 'au-delà', 'eus-je', 'tout-à-coup', 'Apprenez-moi', 'pouvons-nous', 'tout-puiſſant', 'celui-ci', 'peu-à-peu', 'lui-même', 'toi-même', 'lui-même', 'dit-il', 'long-temps', 'lui-même', 'long-temps', 'diſoit-il', 'lui-même', 'moi-même', 'dit-il', 'eut-il', 'au-travers', 'bien-tôt', 'dit-il', 'continua-t-il', 'répondis-je', 'vis-à-vis', 'ment-là', 'continua-t-il', 'tez-moi', 'faites-moi', 'tout-à-coup', 'aurois-je', 'aurois-je', 'moi-même', 'dis-je', 'dites-moi', 'long-temps', 'lui-même', 'moi-même', 'écriai-je', 'reprit-il', 'dit-il', 'repris-je', 'écriai-je', 'peut-être', 'peut-être', 'au-delà', 'dit-il', 'moi-même', 'avez-vous', 'reprit-il', 'dit-il', 'reprit-il', 'peut-être', 'jugeroit-on', 'continua-t-il', 'écria-t-il', 'peut-il', 'peuvent-elles', 'long-temps', 'nua-t-il', 'prenez-moi', 'tout-puiſſant', 'vous-même', 'continua-t-il', 'au-deſſus', 'moi-mê', 'ſuis-je', 'dois-je', 'ſois-je', 'effraye-t', 'puis-je', 'croit-on', 'écriois-je', 'obtiendrai-je', 'peu-à-peu', 'celui-ci', 'écria-t', 'peut-être', 'écriai-je', 'écria-t-il', 'tout-à-coup', 'put-elle', 'écria-t-elle', 'retrouvai-je', 'va-t-il', 'par-tout', 'écria-t-il', 'moi-même', 'bien-tôt', 'ſur-tout', 'au-deſſus', 'peut-elle', 'eſt-elle', 'tout-à-coup', 'beau-Pere', 'écriai-je', 'Penſes-tu', 'criai-je', 'Auſſi-tôt', 'tout-à-coup', 'bien-tôt', 'eut-il', 'peu-près', 'Juſques-là', 'écriai-je', 'Ecoute-moi', 'prit-il', 'peut-être', 'auſſi-tôt', 'devoit-il', 'voit-il', 'pouvoit-il', 'criai-je', 'lui-mê', 'dit-il', 'prépare-lui', 'peut-être', 'ſur-tout', 'eut-il', 'Auſſi-tôt', 'dérobe-la', 'lui-mê', 'dit-il', 'tout-à-coup', 'au-deſſus', 'écriai-je', 'écriai-je', 'lance-la', 'viens-tu', 'viens-tu', 'roſe-la', 'bien-tôt', 'lui-même', 'écriai-je', 'écriai-je', 'dis-je', 'à-peu', 'bien-tôt', 'reprit-il', 'long-temps', 'répondis-je', 'moi-même', 'Emir-Saheb', 'bien-tôt', 'non-ſeulement', 'lui-même', 'dis-je', 'apprends-moi', 'dit-il', 'reprit-il', 'dit-il', 'fut-là', 'Emir-Saheb', 'moi-même', 'Souviens-toi', 'long-temps', 'bien-tôt', 'au-devant', 'moi-même', 'celui-là', 'bien-tôt', 'arriva-t-il', 'Aly-Oglou', 'Capigi-Bachi', 'dit-il', 'Emir-Saheb', 'dis-je', 'écriai-je', 'dis-je', 'tout-à', 'Capigi-Ba', 'elle-même', 'lui-même', 'ci-devant', 'par-tout', 'tout-à-coup', 'moi-même', 'vois-je', 'dirai-je', 'daigna-t-il', 'dit-il', 'reprit-il', 'elle-même', 'dit-il', 'dit-il', 'toi-même', 'ſur-tout', 'long-temps', 'lui-même', 'bien-tôt', 'lui-même', 'tout-à-coup', 'tout-à-coup', 'dès-lors', 'lui-même', 'eſt-ce', 'lui-même', 'écriai-je', 'par-tout', 'lui-même', 'ni-même', 'moment-là', 'auſſi-tôt', 'long-temps', 'êtes-vous', 'peut-être', 'tout-à-coup', 'long-temps', 'dit-il', 'ſions-nous', 'écriai-je', 'reprit-il', 'écriai-je', 'arriverons-nous', 'Seconde-moi', 'dis-je', 'moi-même', 'tout-à', 'au-travers', 'moi-même', 'lui-même', 'dit-il', 'tout-puiſſant', 'demie-journée', 'de-là', 'peu-à-peu', 'écriai-je', 'diſois-je', 'moi-même', 'pourroit-il', 'lui-même', 'criai-je', 'irois-je', 'moi-mê', 'à-demi', 'au-travers', 'très-baſſe', 'enveloppez-moi', 'écriai-je', 'ſuis-je', 'ai-je', 'Eſt-ce', 'fais-tu', 'criai-je', 'retire-toi', 'dis-je', 'lui-même', 'dit-il', 'dès-à-préſent', 'tout-à-coup', 'écriai-je', 'Paſſez-y', 'dit-elle', 'répliquai-je', 'dit-elle', 'elle-même', 'penſes-tu', 'parles-tu', 'aurai-je', 'puis-je', 'lui-même', 'ajouta-t', 'dit-il', 'elle-mê', 'diſoit-elle', 'pourra-t-il', 'Quitte-moi', 'expoſe-lui', 'dis-moi', 'puis-je', 'lui-même', 'peut-être', 'pardonneroit-il', 'écriai-je', 'par-tout', 'bien-tôt', 'auſſi-tôt', 'de-là', 'lui-même', 'auſſi-tôt', 'très-grand', 'long-temps', 'tout-à-coup', 'eſt-ce', 'criai-je', 'moi-même', 'écria-t-elle', 'trouvai-je', 'écria-t-il', 'moi-même', 'offres-tu', 'pourrois-je', 'bien-tôt', 'long-temps', 'écria-t-il', 'puis-je', 'veillai-je', 'moi-même', 'eût-il', 'dit-il', 'au-deſſus', 'perce-moi', 'au-deſſous', 'long-temps', 'ques-unes', 'Venez-en', 'obtenez-en', 'au-deſſus', 'continua-t', 'tout-à-coup', 'ſçais-je']

def zeilen_einlesen():
    with open(DATEI, 'r', encoding='utf8') as file:
        inhalt = file.readlines()
    inhalt_ = [zeile.strip() for zeile in inhalt]
    return inhalt_


def auswertung(inhalt):
    zeilen_neu = []
    durchlauf = False
    for zeilennummer, zeile in enumerate(inhalt):
        if durchlauf:
            pos_erstes_wort = inhalt[zeilennummer].find(" ")
            zeile = zeile[pos_erstes_wort+1:]
        try:
            if zeile[-1] == "-":
                pos_erstes_wort = inhalt[zeilennummer + 1].find(" ")
                erstes_wort = inhalt[zeilennummer + 1][:pos_erstes_wort]
                if erstes_wort not in stopwords:
                    zeile = zeile[:-1]
                    zeile += erstes_wort + "|"
                    durchlauf = True
                else:
                    durchlauf = False
            else:
                durchlauf = False
            zeilen_neu.append(zeile)
        except IndexError:
            pass
    return zeilen_neu


def ausgabe(inhalt):
    lines=[]
    for line in inhalt:
        lines.append(line)
    text = '\n'.join(lines)
    with open('plaintext_Popeliniere_Daira_1.txt', "w", encoding='utf8') as pl:
        pl.write(text)
        pl.close()
        print(text)




def main():
    inhalt = zeilen_einlesen()
    inhalt_neu = auswertung(inhalt)
    ausgabe(inhalt_neu)


if __name__ == "__main__":
    main()