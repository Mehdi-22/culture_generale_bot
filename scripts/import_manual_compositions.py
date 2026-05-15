#!/usr/bin/env python3
"""
Import manuel des compositions recuperees depuis Telegram.
Usage : python3 scripts/import_manual_compositions.py
A executer depuis la racine du projet (ou le dossier data/ est present).
"""

import re
from pathlib import Path
from datetime import datetime

ARCHIVE_FILE = Path("data/compositions.md")

COMPOSITIONS = [
    # -----------------------------------------------------------------------
    # COMPOSITION 1 — Chine / Iran / Trump a Pekin
    # PARTIELLE : §1-§9 (Partie 1/3) manquants — a completer
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-15 10:02",
        "title": "La position de la Chine face a la crise iranienne et la visite de Trump a Pekin",
        "source": "[source inconnue - Partie 1/3 manquante]",
        "url": "",
        "note": "Composition partielle : §1 a §9 non recuperes (Partie 1/3 absente).",
        "composition": """\
[§1 a §9 manquants — coller la Partie 1/3 ici]

**§10 - ID2**
Outre les fondements stratégiques sino-iraniens, les tentatives de coercition américaine sur Pékin, conjuguées aux contradictions de la diplomatie trumpienne et aux limites objectives de cette pression, constituent l'essentiel des dynamiques de friction entre Washington et Pékin.

**§11 - IS21**
Assurément, Donald Trump tente d'utiliser sa visite à Pékin comme levier de pression sur Xi Jinping. À cet égard, Washington cherche à dissuader la Chine de soutenir diplomatiquement et économiquement Téhéran. La menace de sanctions secondaires ciblant les entreprises chinoises commercant avec l'Iran est révélatrice à ce sujet.

**§12 - IS22**
De même, la Chine perçoit cette pression américaine comme une ingérence inacceptable dans ses choix souverains. Dans ce même ordre d'idée, Pékin a systématiquement opposé son droit de veto aux résolutions anti-iraniennes au Conseil de Sécurité de l'ONU. À en croire les déclarations officielles du ministère des Affaires étrangères chinois, Pékin refuse toute conditionnalité imposée de l'extérieur.

**§13 - IS23**
De surcroît, la crédibilité de la pression américaine est affaiblie par les propres contradictions de la politique trumpienne. À ce titre, les guerres commerciales simultanées menées par Trump contre la Chine réduisent sa capacité à obtenir des concessions sur l'Iran. La gestion erratique de la diplomatie américaine sous Trump illustre parfaitement ce constat.

**§14 - Conclusion P2 + transition**
Dès lors, les pressions américaines sur la Chine concernant l'Iran se heurtent à des intérêts stratégiques profonds et à une détermination souveraine de Pékin à protéger ses partenariats. Ces constats nous amènent à examiner les leviers diplomatiques concrets dont dispose la Chine pour gérer cette crise.

**§15 - ID3**
Outre les fondements stratégiques sino-iraniens et les pressions américaines et leurs limites, la diplomatie de médiation, l'instrumentalisation des institutions multilatérales et la dissuasion économique restent des leviers à même de permettre à Pékin de préserver ses intérêts tout en évitant l'escalade.

**§16 - IS31**
Effectivement, la Chine peut s'ériger en médiateur crédible entre l'Iran et ses adversaires pour valoriser son statut mondial. Dans ce même registre, Pékin dispose d'une crédibilité unique auprès de Téhéran qu'aucune autre puissance ne possède. Comme c'est le cas de la médiation sino-saoudienne de 2023 qui avait abouti au rapprochement entre Riyad et Téhéran.

**§17 - IS32**
Aussi, la Chine peut utiliser les enceintes multilatérales pour diluer la pression américaine et légitimer sa posture. À ce propos, les BRICS et l'OCS offrent à Pékin des plateformes alternatives aux institutions dominées par l'Occident. Le sommet des BRICS de 2024 en témoigne éloquemment, où la solidarité entre membres face aux sanctions unilatérales fut réaffirmée.

**§18 - IS33**
Enfin, la Chine peut brandir l'arme économique pour décourager toute escalade militaire menaçant ses routes d'approvisionnement. En effet, une instabilité prolongée au Moyen-Orient menacerait directement les intérêts chinois dans la région. La présence croissante de la marine chinoise dans le golfe Persique constitue une aubaine à ce sujet pour signaler cette détermination.

**§19 - Conclusion P3 SANS transition**
Ainsi, la Chine dispose d'une palette diplomatique, institutionnelle et sécuritaire suffisamment diversifiée pour naviguer avec habileté dans la crise iranienne, sans sacrifier ses intérêts vitaux ni provoquer une rupture frontale avec Washington.

**§20 - Reformulation IM**
En définitive, si la Chine maintient officiellement une neutralité dans la guerre d'Iran, la réalité de ses intérêts énergétiques, de ses ambitions infrastructurelles via la Route de la Soie et de sa convergence idéologique avec Téhéran oriente sa diplomatie vers une protection implicite de l'Iran. La visite de Trump à Pékin et ses tentatives de pression se heurtent à la détermination souveraine de Xi Jinping. La Chine, armée de ses leviers de médiation et de ses alliances multilatérales, entend préserver son partenariat stratégique avec Téhéran tout en évitant une escalade directe avec les États-Unis.

**§21 - Ouverture**
Par ailleurs, l'émergence d'un monde multipolaire où la Chine joue un rôle de puissance stabilisatrice alternative pourrait redéfinir durablement les équilibres au Moyen-Orient, offrant aux nations de la région des partenariats stratégiques diversifiés et moins conditionnés par les exigences de Washington.""",
    },

    # -----------------------------------------------------------------------
    # COMPOSITION 2 — Chine / Afrique / levee barrieres douanieres
    # COMPLETE (3/3 parties recuperees)
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-15 10:20",
        "title": "Levée des barrières douanières par la Chine au profit des pays africains : un instrument stratégique pour Pékin ?",
        "source": "IRIS",
        "url": "https://www.iris-france.org/levee-des-barrieres-douanieres-par-la-chine-au-profit-des-pays-africains-un-instrument-strategique-pour-pekin/",
        "note": "",
        "composition": """\
**Limites** : Présent / futur proche · Sino-africain (53 pays) · Économique et géostratégique

**§1 - PRÉAMBULE**
Le commerce international constitue depuis des siècles un vecteur de puissance et d'influence entre les nations. Les relations commerciales entre la Chine et l'Afrique ont connu une transformation spectaculaire depuis les années 2000. La Chine est devenue le premier partenaire commercial du continent africain, avec des échanges dépassant les 280 milliards de dollars annuels. Dans ce cadre, la décision de Pékin de supprimer les droits de douane sur les produits de 53 pays africains, à compter du 1er mai 2026, revêt une portée considérable. Cette initiative intervient dans un contexte mondial marqué par des guerres tarifaires, une crise du multilatéralisme et une compétition accrue pour les ressources critiques. Ce constat interpelle une profonde réflexion quant à la nature réelle de cette mesure et ses implications pour les équilibres géoéconomiques mondiaux.

**§2 - QUESTION POSÉE**
Il serait judicieux de s'interroger sur la véritable nature de la levée des barrières douanières chinoises au profit des pays africains, à savoir si cette mesure constitue un geste de solidarité commerciale ou un instrument stratégique au service des ambitions de Pékin sur le continent africain et dans l'arène internationale.

**§3 - IDÉE MAÎTRESSE**
Bien que la suppression des droits de douane chinois représente une opportunité économique tangible pour les pays africains, il n'en demeure pas moins que cette mesure s'inscrit dans une logique stratégique globale visant à consolider l'influence de Pékin sur le continent et à remodeler les équilibres commerciaux mondiaux à son avantage.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les fondements économiques et les opportunités offertes aux pays africains, les objectifs stratégiques poursuivis par la Chine à travers cette mesure et les défis que les États africains doivent relever pour éviter une relation commerciale déséquilibrée.

**§5 - ID1**
Les gains en matière d'accès au marché chinois, conjugués à la facilitation procédurale et à l'élargissement du spectre des produits concernés, sont autant d'atouts significatifs qui constituent le socle des opportunités économiques réelles offertes aux pays africains.

**§6 - IS11**
De prime abord, la levée des droits de douane ouvre aux pays africains un marché de 1,4 milliard de consommateurs. À ce propos, près de 97 % des lignes douanières sont désormais exemptées pour les pays à revenu intermédiaire. L'accession du Maroc et d'autres pays d'Afrique du Nord à ce dispositif en constitue un exemple éloquent, leur permettant de cibler un marché colossal pour leurs produits agricoles et manufacturés.

**§7 - IS12**
Par ailleurs, la mise en place d'un « canal vert » facilite les procédures douanières et réduit les délais d'acheminement des marchandises. Dans ce cadre, cette facilitation procédurale représente un avantage concret pour les exportateurs africains, souvent pénalisés par des lourdeurs administratives. À titre d'illustration, les exportateurs de produits agricoles périssables, comme les agrumes marocains ou les fruits tropicaux ivoiriens, bénéficieront directement de cette accélération des procédures.

**§8 - IS13**
De surcroît, cette mesure élargit les bénéfices, jusqu'ici réservés aux seuls pays les moins avancés, aux États à revenu intermédiaire. En effet, depuis le 1er décembre 2024, les 33 pays les moins avancés africains bénéficiaient déjà du tarif zéro sur l'intégralité de leurs lignes. L'inclusion des pays à revenu intermédiaire vient corroborer cette analyse en témoignant d'une volonté de Pékin d'élargir son réseau d'influence à l'ensemble du continent.

**§9 - Conclusion P1 + transition**
Partant, la levée des barrières douanières chinoises offre des opportunités commerciales réelles et mesurables aux pays africains, en termes d'accès au marché, de facilitation procédurale et d'élargissement du champ des bénéficiaires. Il en est de même pour les objectifs stratégiques que la Chine entend poursuivre à travers cette initiative apparemment généreuse.

**§10 - ID2**
Outre les opportunités commerciales offertes aux pays africains, les ambitions géopolitiques chinoises conjuguées aux impératifs de la guerre tarifaire mondiale et à la course aux ressources critiques constituent l'essentiel des motivations stratégiques de Pékin derrière cette mesure.

**§11 - IS21**
Assurément, la Chine cherche à contrebalancer les effets des guerres tarifaires imposées par les États-Unis en consolidant ses alliances commerciales avec l'Afrique. À cet égard, la mesure a été annoncée par le président Xi Jinping en marge du 39e sommet de l'Union africaine, en février 2025, signal diplomatique fort. Cette temporalité est révélatrice à ce sujet : Pékin choisit l'Afrique comme partenaire privilégié face aux pressions occidentales.

**§12 - IS22**
De même, la Chine aspire à sécuriser son approvisionnement en ressources critiques indispensables à sa transition énergétique et numérique. Dans ce même ordre d'idée, l'Afrique détient plus de 30 % des réserves mondiales de minéraux stratégiques, dont le cobalt, le lithium et les terres rares. À en croire les analyses de l'IRIS, l'exemption douanière constitue une incitation à exporter davantage ces matières premières vers la Chine, renforçant ainsi la dépendance africaine à l'égard de Pékin.

**§13 - IS23**
De surcroît, la Chine poursuit l'objectif d'accélérer la dédollarisation des échanges commerciaux via son système de paiement CIPS. À ce titre, l'intégration croissante des économies africaines dans l'orbite commerciale chinoise favorise l'utilisation du yuan dans les transactions bilatérales. L'exemple du Nigeria et de l'Égypte, qui ont déjà conclu des accords de swap monétaire avec la Chine, illustre parfaitement ce constat.

**§14 - Conclusion P2 + transition**
Dès lors, la levée des barrières douanières chinoises répond à une logique stratégique multidimensionnelle, articulant contre-offensive tarifaire, sécurisation des ressources et promotion du yuan. Ces constats nous amènent à examiner les défis que les pays africains doivent impérativement relever pour ne pas se laisser enfermer dans une relation commerciale asymétrique.

**§15 - ID3**
Outre les opportunités commerciales et les ambitions stratégiques chinoises, le renforcement des capacités exportatrices africaines, la protection des marchés locaux et la diversification des partenariats restent des leviers à même de garantir une intégration souveraine et équilibrée dans ce nouveau dispositif commercial.

**§16 - IS31**
Effectivement, les pays africains doivent impérativement développer leur capacité à transformer localement leurs matières premières avant exportation. Dans ce même registre, exporter des produits manufacturés plutôt que des matières premières brutes permet de capter davantage de valeur ajoutée. Comme c'est le cas du Maroc, qui a investi massivement dans sa filière phosphatique pour exporter des engrais transformés plutôt que du minerai brut, modèle que d'autres pays africains pourraient utilement suivre.

**§17 - IS32**
Aussi, les États africains doivent renforcer leurs mécanismes de protection des marchés intérieurs contre d'éventuelles importations chinoises déguisées. À ce propos, le risque de voir des produits chinois transiter via des pays africains pour contourner des droits de douane tiers est réel et documenté. L'expérience des textiles africains, largement concurrencés par les importations chinoises à bas coût, en témoigne éloquemment.

**§18 - IS33**
Enfin, la diversification des partenariats commerciaux constitue une garantie indispensable contre la dépendance excessive envers Pékin. En effet, les accords de libre-échange avec l'Union européenne, les États-Unis ou d'autres puissances émergentes offrent des alternatives crédibles. La Zone de Libre-Échange Continentale Africaine (ZLECAf) constitue une aubaine à ce sujet, en offrant aux pays africains un levier collectif pour négocier en position de force avec la Chine et les autres partenaires.

**§19 - Conclusion P3 SANS transition**
Ainsi, les pays africains disposent de leviers concrets pour transformer cette opportunité commerciale en véritable vecteur de développement souverain, à condition de renforcer leurs capacités productives, de protéger leurs marchés et de diversifier leurs alliances économiques.

**§20 - Reformulation de l'idée maîtresse**
En définitive, la suppression des droits de douane chinois sur les produits de 53 pays africains offre des opportunités commerciales réelles, notamment un accès élargi à un marché de 1,4 milliard de consommateurs et une facilitation procédurale bienvenue. Toutefois, cette mesure s'inscrit dans une stratégie globale de Pékin visant à contrebalancer les pressions tarifaires américaines, à sécuriser ses approvisionnements en ressources critiques et à promouvoir l'usage du yuan. Pour que les pays africains tirent pleinement profit de cette initiative sans tomber dans une dépendance accrue, ils devront impérativement développer leur industrie de transformation, protéger leurs marchés intérieurs et s'appuyer sur des cadres collectifs comme la ZLECAf pour préserver leur souveraineté économique.

**§21 - Ouverture**
Par ailleurs, l'évolution de ce partenariat sino-africain s'inscrira inévitablement dans la recomposition plus large de l'ordre économique mondial, où les pays du Sud global cherchent à affirmer leur autonomie stratégique face aux grandes puissances, ouvrant ainsi la voie à de nouveaux modèles de coopération Sud-Sud fondés sur la réciprocité et le respect des souverainetés nationales.""",
    },
]


def main():
    if not ARCHIVE_FILE.exists():
        ARCHIVE_FILE.parent.mkdir(exist_ok=True)
        ARCHIVE_FILE.write_text("# Archive des Compositions CEM-CG\n", encoding="utf-8")

    existing_titles: set[str] = set()
    content = ARCHIVE_FILE.read_text(encoding="utf-8")
    for match in re.finditer(r"^## .+? — (.+)$", content, re.MULTILINE):
        existing_titles.add(match.group(1).strip())

    added = 0
    with ARCHIVE_FILE.open("a", encoding="utf-8") as f:
        for comp in COMPOSITIONS:
            title = comp["title"]
            if title in existing_titles:
                print(f"  (deja present) {title[:80]}")
                continue

            note_line = f"\n> ⚠️ {comp['note']}\n" if comp["note"] else ""
            entry = (
                f"\n---\n\n"
                f"## {comp['date']} — {title}\n"
                f"**Source** : {comp['source']}\n"
                f"**URL** : {comp['url']}\n"
                f"{note_line}\n"
                f"{comp['composition']}\n"
            )
            f.write(entry)
            existing_titles.add(title)
            added += 1
            print(f"  + {title[:80]}")

    print(f"\n{added} composition(s) ajoutee(s) dans {ARCHIVE_FILE}")


if __name__ == "__main__":
    main()
