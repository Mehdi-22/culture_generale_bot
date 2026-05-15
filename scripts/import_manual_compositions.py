#!/usr/bin/env python3
"""
Import manuel des compositions recuperees depuis Telegram.
Usage : python3 scripts/import_manual_compositions.py
A executer depuis la racine du projet (ou le dossier data/ est present).
"""

import re
from pathlib import Path

ARCHIVE_FILE = Path("data/compositions.md")

COMPOSITIONS = [
    # -----------------------------------------------------------------------
    # COMPOSITION 1 — Sante mondiale / politique etrangere americaine
    # Source : IRIS — Genere le 15/05/2026 10:01 — COMPLETE
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-15 10:01",
        "title": "La santé mondiale, nouvelle arme de la politique étrangère américaine",
        "source": "IRIS",
        "url": "https://www.iris-france.org/la-sante-mondiale-nouvelle-arme-de-la-politique-etrangere-americaine/",
        "composition": """\
**Limites** : Post-2025 (AfGHS sept. 2025) · Mondial / focus Afrique · Politique étrangère, sanitaire, géopolitique

**§1 - PRÉAMBULE**
La coopération sanitaire internationale est un pilier de la diplomatie contemporaine. Depuis la création de l'Organisation Mondiale de la Santé en 1948, les États ont utilisé l'aide médicale comme levier d'influence. Les grandes puissances ont financé la lutte contre le VIH/SIDA, le paludisme et la tuberculose. Ces engagements ont toujours mêlé solidarité humanitaire et calcul géopolitique. L'aide en santé a donc oscillé, historiquement, entre générosité affichée et intérêt national dissimulé. Aujourd'hui, avec la publication de l'America First Global Health Strategy en septembre 2025, cette tension prend une dimension inédite. Les États-Unis assument désormais, sans ambiguïté, que leur aide sanitaire est un instrument stratégique. Ce bouleversement de l'ordre sanitaire mondial interpelle une profonde réflexion quant à ses implications géopolitiques, humanitaires et stratégiques pour les nations en développement.

**§2 - QUESTION POSÉE**
Face à cette recomposition radicale de la diplomatie sanitaire américaine, il serait judicieux de s'interroger sur la nature véritable de la santé mondiale en tant que nouvel instrument de la politique étrangère des États-Unis, ses mécanismes d'action, ses enjeux pour les pays récipiendaires, et les perspectives qu'elle ouvre notamment pour le continent africain.

**§3 - IDÉE MAÎTRESSE**
Bien que la coopération sanitaire internationale ait toujours intégré des considérations géopolitiques implicites, il n'en demeure pas moins que l'America First Global Health Strategy marque une rupture stratégique majeure en instrumentalisant ouvertement la santé mondiale comme vecteur de puissance américaine et en redessinant les équilibres géopolitiques sanitaires au détriment des nations les plus vulnérables.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les fondements doctrinaux et mécanismes de la stratégie sanitaire américaine, les enjeux géopolitiques et sanitaires pour les pays en développement, et les leviers d'adaptation et de résilience dont disposent les nations africaines et leurs partenaires.

**§5 - ID1**
Les postulats souverainistes de l'AfGHS, conjugués aux mécanismes de conditionnalité bilatérale et à la réorientation des financements multilatéraux, sont autant de marqueurs idéologiques qui constituent le socle doctrinal d'une diplomatie sanitaire assumée.

**§6 - IS11**
De prime abord, la stratégie américaine rompt avec le multilatéralisme sanitaire traditionnel. À ce propos, l'AfGHS publiée en septembre 2025 place explicitement les mots « intérêt national » et « America First » au cœur du document officiel. Le retrait américain de l'OMS constitue un exemple éloquent de cette rupture avec les normes collectives établies.

**§7 - IS12**
Par ailleurs, la conditionnalité bilatérale devient le nouveau langage de l'aide sanitaire américaine. Dans ce cadre, Washington subordonne désormais ses financements à des accords bilatéraux alignés sur ses propres intérêts diplomatiques et économiques. À titre d'illustration, les pays récipiendaires en Afrique subsaharienne doivent désormais négocier directement avec des agences américaines sous tutelle politique étroite.

**§8 - IS13**
De surcroît, la réorientation des flux financiers multilatéraux amplifie cette transformation doctrinale. En effet, les États-Unis ont historiquement contribué à hauteur de 30% du budget du Fonds mondial de lutte contre le SIDA, la tuberculose et le paludisme. La remise en cause de ces contributions par l'administration Trump vient corroborer cette analyse d'une santé mondiale délibérément instrumentalisée.

**§9 - Conclusion P1 + transition**
Partant, la stratégie sanitaire américaine repose sur une doctrine souverainiste explicite, des mécanismes bilatéraux contraignants et un désinvestissement multilatéral calculé. Il en est de même pour les enjeux géopolitiques et sanitaires que cette stratégie génère pour les pays en développement.

**§10 - ID2**
Outre les fondements doctrinaux de l'AfGHS, les vulnérabilités épidémiologiques accrues, conjuguées aux reconfigurations des alliances diplomatiques sanitaires et aux risques de dépendance normative, constituent l'essentiel des enjeux géopolitiques et sanitaires pour les nations en développement.

**§11 - IS21**
Assurément, le retrait américain fragilise les systèmes de santé des pays les plus dépendants de l'aide extérieure. À cet égard, vingt-huit pays africains tirent plus de 50% de leur budget santé de financements extérieurs, dont une part significative américaine. Le Rwanda et l'Ouganda, historiquement soutenus par le PEPFAR, sont révélateurs à ce sujet de cette dépendance structurelle dangereuse.

**§12 - IS22**
De même, la recomposition des alliances diplomatiques sanitaires ouvre un espace d'influence pour des puissances concurrentes. Dans ce même ordre d'idées, la Chine et la Russie ont accéléré leur diplomatie vaccinale et sanitaire vers l'Afrique depuis 2020. À en croire les rapports de l'Union Africaine, Pékin a signé plus de quarante accords sanitaires bilatéraux avec des États africains entre 2021 et 2024.

**§13 - IS23**
De surcroît, l'imposition de normes américaines unilatérales constitue un risque de dépendance normative pour les pays récipiendaires. À ce titre, l'AfGHS conditionne l'aide à l'adoption de standards sanitaires, commerciaux et réglementaires favorables aux intérêts américains. L'expérience des politiques d'ajustement structurel de la Banque mondiale dans les années 1980 illustre parfaitement ce constat d'une aide porteuse de conditionnalités aliénantes.

**§14 - Conclusion P2 + transition**
Dès lors, la stratégie sanitaire américaine génère des vulnérabilités épidémiologiques, des reconfigurations d'alliances et des risques normatifs majeurs pour les pays en développement. Ces constats nous amènent à examiner les leviers d'adaptation et de résilience dont disposent les nations africaines et leurs partenaires stratégiques.

**§15 - ID3**
Outre les fondements doctrinaux de l'AfGHS et ses enjeux géopolitiques, le renforcement de la souveraineté sanitaire africaine, la diversification des partenariats stratégiques et la montée en puissance des institutions sanitaires régionales restent des leviers à même de construire une résilience durable face à cette recomposition de l'ordre sanitaire mondial.

**§16 - IS31**
Effectivement, le renforcement de la souveraineté sanitaire africaine est une réponse structurelle incontournable. Dans ce même registre, l'objectif de produire 60% des besoins vaccinaux africains sur le continent d'ici 2040 constitue une priorité stratégique de l'Union Africaine. Comme c'est le cas du complexe industriel pharmaceutique du Maroc, notamment l'Institut Pasteur du Maroc et Sothema, qui incarnent cette dynamique de souveraineté sanitaire africaine.

**§17 - IS32**
Aussi, la diversification des partenariats sanitaires permet de réduire la dépendance envers un seul bailleur de fonds. À ce propos, le Maroc, l'Union Européenne et les institutions du Golfe développent des cadres de coopération sanitaire alternatifs avec les pays africains. Le partenariat sanitaire Maroc-Afrique subsaharienne, porté par la vision royale de coopération Sud-Sud, en témoigne éloquemment.

**§18 - IS33**
Enfin, la consolidation des institutions sanitaires régionales africaines offre un cadre collectif de résistance. En effet, le Centre Africain de Prévention et de Contrôle des Maladies (Africa CDC), créé en 2017, monte en puissance dans la coordination des réponses épidémiques continentales. La gestion par Africa CDC de l'épidémie de mpox en 2024 constitue une aubaine à ce sujet pour démontrer la capacité africaine d'autonomie sanitaire croissante.

**§19 - Conclusion P3 SANS transition**
Ainsi, la souveraineté sanitaire industrielle, la diversification des partenariats et le renforcement des institutions régionales africaines forment un triptyque de résilience capable de contrebalancer les effets déstabilisateurs de la nouvelle doctrine sanitaire américaine.

**§20 - Reformulation de l'idée maîtresse**
En définitive, bien que la coopération sanitaire internationale ait toujours intégré des dimensions géopolitiques implicites, l'America First Global Health Strategy de septembre 2025 marque une rupture doctrinale inédite. En assumant sans ambiguïté que l'aide sanitaire est un instrument stratégique, les États-Unis fragilisent les systèmes de santé de vingt-huit pays africains fortement dépendants, reconfigurent les alliances diplomatiques au profit de la Chine et de la Russie, et imposent des conditionnalités normatives aliénantes. Face à ces défis, la souveraineté sanitaire industrielle — incarnée par des acteurs comme le Maroc —, la diversification des partenariats et la montée en puissance d'Africa CDC constituent des réponses structurelles à même de préserver l'autonomie sanitaire du continent africain.

**§21 - Ouverture**
Par ailleurs, cette recomposition de l'ordre sanitaire mondial pourrait accélérer l'émergence d'une architecture sanitaire multipolaire, dans laquelle le Maroc, fort de ses capacités industrielles pharmaceutiques et de sa vision de coopération Sud-Sud portée par Sa Majesté le Roi Mohammed VI, serait appelé à jouer un rôle de pivot stratégique entre l'Afrique, l'Europe et le monde arabe dans la gouvernance sanitaire internationale du XXIe siècle.""",
    },

    # -----------------------------------------------------------------------
    # COMPOSITION 2 — La Chine et la guerre d'Iran
    # Source : IRIS — Genere le 15/05/2026 10:02 — COMPLETE
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-15 10:02",
        "title": "La Chine et la guerre d'Iran",
        "source": "IRIS",
        "url": "https://www.iris-france.org/la-chine-et-la-guerre-diran/",
        "composition": """\
**Limites** : Présent / projection future · Triangle Chine-Iran-États-Unis · Politique, sécuritaire, économique

**§1 - PRÉAMBULE**
La relation sino-iranienne s'inscrit dans une longue tradition de coopération stratégique. Depuis des siècles, la Route de la Soie liait ces deux civilisations millénaires. Aujourd'hui, cette relation prend une dimension géopolitique nouvelle. Le conflit impliquant l'Iran bouleverse l'équilibre régional du Moyen-Orient. La Chine, première puissance asiatique, observe ce conflit avec un intérêt particulier. Sa dépendance aux hydrocarbures iraniens conditionne ses choix diplomatiques. Par ailleurs, la pression américaine incarnée par Donald Trump complexifie davantage cette équation. Ce constat interpelle une profonde réflexion quant à la nature réelle de la posture chinoise face à la guerre d'Iran.

**§2 - QUESTION POSÉE**
Il serait judicieux de s'interroger sur la capacité de la Chine à maintenir une posture d'équilibre entre ses intérêts stratégiques en Iran et les pressions exercées par Washington, dans un contexte de conflit armé aux répercussions mondiales.

**§3 - IDÉE MAÎTRESSE**
Bien que la Chine affiche une neutralité de façade dans la guerre d'Iran, il n'en demeure pas moins que ses intérêts économiques vitaux et ses ambitions géopolitiques mondiales orientent discrètement mais résolument sa diplomatie vers une protection implicite de Téhéran face aux pressions américaines.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les fondements stratégiques et économiques liant la Chine à l'Iran, les pressions américaines exercées sur Pékin et leurs limites, et enfin les leviers diplomatiques dont dispose la Chine pour naviguer dans cette crise.

**§5 - ID1**
Les intérêts énergétiques chinois en Iran, conjugués aux ambitions de la Route de la Soie et à la convergence idéologique anti-hégémonique, sont autant de déterminants structurels qui constituent le socle indéfectible de la relation sino-iranienne.

**§6 - IS11**
De prime abord, la Chine dépend significativement du pétrole iranien pour alimenter son économie. À ce propos, l'Iran représente l'une des principales sources d'approvisionnement énergétique de Pékin malgré les sanctions. L'accord de coopération de 25 ans signé en 2021 entre les deux pays en constitue un exemple éloquent.

**§7 - IS12**
Par ailleurs, l'Iran occupe une place centrale dans le projet chinois des Nouvelles Routes de la Soie. Dans ce cadre, Téhéran constitue un corridor terrestre et maritime stratégique vers l'Europe et l'Asie centrale. À titre d'illustration, les investissements chinois dans les ports et infrastructures iraniens atteignent des dizaines de milliards de dollars.

**§8 - IS13**
De surcroît, la Chine et l'Iran partagent une vision commune de résistance à l'hégémonie américaine. En effet, les deux nations convergent sur le rejet de l'ordre unipolaire dominé par Washington. L'adhésion de l'Iran à l'Organisation de Coopération de Shanghai en 2023 vient corroborer cette analyse.

**§9 - Conclusion P1 + transition**
Partant, la relation sino-iranienne repose sur des fondements économiques, infrastructurels et idéologiques solides qui dépassent la simple conjoncture conflictuelle. Il en est de même pour la compréhension des pressions américaines que Trump tente d'exercer sur Pékin.

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

**§20 - Reformulation de l'idée maîtresse**
En définitive, si la Chine maintient officiellement une neutralité dans la guerre d'Iran, la réalité de ses intérêts énergétiques, de ses ambitions infrastructurelles via la Route de la Soie et de sa convergence idéologique avec Téhéran oriente sa diplomatie vers une protection implicite de l'Iran. La visite de Trump à Pékin et ses tentatives de pression se heurtent à la détermination souveraine de Xi Jinping. La Chine, armée de ses leviers de médiation et de ses alliances multilatérales, entend préserver son partenariat stratégique avec Téhéran tout en évitant une escalade directe avec les États-Unis.

**§21 - Ouverture**
Par ailleurs, l'émergence d'un monde multipolaire où la Chine joue un rôle de puissance stabilisatrice alternative pourrait redéfinir durablement les équilibres au Moyen-Orient, offrant aux nations de la région des partenariats stratégiques diversifiés et moins conditionnés par les exigences de Washington.""",
    },

    # -----------------------------------------------------------------------
    # COMPOSITION 3 — Levee barrieres douanieres Chine / Afrique
    # Source : IRIS — Genere le 15/05/2026 10:20 — COMPLETE
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-15 10:20",
        "title": "Levée des barrières douanières par la Chine au profit des pays africains : un instrument stratégique pour Pékin ?",
        "source": "IRIS",
        "url": "https://www.iris-france.org/levee-des-barrieres-douanieres-par-la-chine-au-profit-des-pays-africains-un-instrument-strategique-pour-pekin/",
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

    # -----------------------------------------------------------------------
    # COMPOSITION 4 — Blocus du detroit d'Ormuz / Inde, Japon, Coree du Sud
    # Source : IRIS — Genere le 12/05/2026 21:43 — PARTIELLE
    # §1-§7 recuperes (Partie 1/3), §8-§16 manquants, §17-§21 recuperes
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-12 21:43",
        "title": "Les chaînes d'approvisionnement pétrolières asiatiques perturbées par le blocus du détroit d'Ormuz : perspectives pour l'Inde, le Japon et la Corée du Sud",
        "source": "IRIS",
        "url": "https://www.iris-france.org/les-chaines-dapprovisionnement-petrolieres-asiatiques-perturbees-par-le-blocus-du-detroit-dormuz-perspectives-pour-linde-le-japon-et-la-coree-du-sud/",
        "composition": """\
**Limites** : Depuis 28/02/2026 / moyen terme · Détroit d'Ormuz → Asie · Sécuritaire, économique, géopolitique

**§1 - PRÉAMBULE**
Le détroit d'Ormuz constitue l'une des voies maritimes les plus stratégiques au monde. Par ce goulet de quelques kilomètres transitent près de 20 % des approvisionnements pétroliers mondiaux. Depuis l'Antiquité, celui qui contrôle les passages maritimes contrôle les économies. Aujourd'hui, le blocus imposé par l'Iran à la suite de l'attaque américano-israélienne du 28 février 2026 rappelle cette vérité immuable. Les nations asiatiques, fortement dépendantes du pétrole du Golfe, se trouvent désormais face à une vulnérabilité énergétique majeure. Ce constat interpelle une profonde réflexion quant à la fragilité des chaînes d'approvisionnement pétrolières asiatiques face aux crises géopolitiques dans le Golfe Persique.

**§2 - QUESTION POSÉE**
Face à cette situation d'une gravité inédite, il serait judicieux de s'interroger sur les conséquences du blocus du détroit d'Ormuz sur les chaînes d'approvisionnement pétrolières de l'Inde, du Japon et de la Corée du Sud, ainsi que sur les stratégies d'adaptation que ces nations pourraient déployer.

**§3 - IDÉE MAÎTRESSE**
Bien que le blocus du détroit d'Ormuz constitue une menace sécuritaire immédiate pour les économies asiatiques, il n'en demeure pas moins qu'il révèle des vulnérabilités structurelles profondes et ouvre la voie à une recomposition durable des équilibres énergétiques et géopolitiques régionaux.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les impacts directs du blocus sur les approvisionnements énergétiques asiatiques, les enjeux géopolitiques et sécuritaires liés à la crise d'Ormuz, et les perspectives de résilience énergétique pour l'Inde, le Japon et la Corée du Sud.

**§5 - ID1**
Les ruptures d'approvisionnement en pétrole brut, conjuguées à la flambée des prix et à l'arrêt quasi total du trafic maritime, sont autant de chocs énergétiques qui constituent le premier vecteur de déstabilisation des économies asiatiques dépendantes du Golfe Persique.

**§6 - IS11**
De prime abord, la dépendance asiatique au pétrole du Golfe rend ces économies particulièrement vulnérables au blocus. À ce propos, l'Inde importe environ 60 % de son pétrole brut depuis la région du Golfe Persique. Le blocus d'Ormuz en constitue un exemple éloquent, paralysant directement les raffineries indiennes approvisionnées par voie maritime.

**§7 - IS12**
Par ailleurs, la fermeture du détroit provoque une flambée immédiate des prix du pétrole sur les marchés mondiaux. Dans ce cadre, les prix ont connu des hausses brutales affectant les économies importatrices nettes que sont le Japon et la Corée du Sud. À titre d'illustration, le Japon, dépourvu de ressources pétrolières propres, voit ses coûts énergétiques s'envoler, menaçant sa compétitivité industrielle.

> ⚠️ §8 à §16 manquants (fin Partie 1/3 et Partie 2/3 non recuperees).

**§17 - IS32**
Aussi, la mobilisation des réserves stratégiques nationales constitue un amortisseur immédiat face aux ruptures d'approvisionnement. À ce propos, le Japon dispose de réserves stratégiques couvrant environ 150 jours de consommation nationale, conformément aux engagements de l'Agence Internationale de l'Énergie. L'activation partielle de ces réserves par Tokyo en témoigne éloquemment, permettant de limiter les effets de la crise dans l'immédiat.

**§18 - IS33**
Enfin, la crise d'Ormuz pourrait constituer un accélérateur de la transition énergétique pour les économies asiatiques. En effet, la vulnérabilité énergétique révélée par le blocus renforce la légitimité des investissements massifs dans les énergies renouvelables et le nucléaire civil. La Corée du Sud, qui dispose d'une industrie nucléaire compétitive et d'un plan ambitieux d'expansion des énergies vertes, constitue une aubaine à ce sujet, pouvant convertir une contrainte géopolitique en opportunité de transformation énergétique durable.

**§19 - Conclusion P3 SANS transition**
Ainsi, face au blocus d'Ormuz, l'Inde, le Japon et la Corée du Sud disposent de plusieurs leviers de résilience complémentaires : diversification des fournisseurs, mobilisation des réserves stratégiques et accélération de la transition énergétique, constituant ensemble une réponse structurée à une crise d'une profondeur inédite.

**§20 - Reformulation de l'idée maîtresse**
En définitive, si le blocus du détroit d'Ormuz imposé par l'Iran depuis le 28 février 2026 constitue une menace sécuritaire et économique immédiate pour les chaînes d'approvisionnement pétrolières de l'Inde, du Japon et de la Corée du Sud, il n'en demeure pas moins qu'il met en lumière des vulnérabilités structurelles préexistantes liées à la dépendance énergétique vis-à-vis du Golfe Persique, tout en révélant les fractures géopolitiques profondes entre grandes puissances, et en ouvrant paradoxalement la voie à une recomposition durable des équilibres énergétiques régionaux au profit d'une plus grande résilience asiatique.

**§21 - Ouverture**
Par ailleurs, la crise d'Ormuz pourrait marquer un tournant historique dans la politique énergétique asiatique, accélérant non seulement la diversification des approvisionnements mais aussi l'émergence de nouvelles architectures de coopération régionale en matière de sécurité énergétique, dans lesquelles le Maroc, acteur atlantique et méditerranéen aux ressources énergétiques renouvelables considérables, pourrait trouver une place de choix comme fournisseur alternatif d'énergie verte vers les marchés asiatiques en quête de stabilité.""",
    },

    # -----------------------------------------------------------------------
    # COMPOSITION 5 — Ukraine / Poutine : gains territoriaux, guerre perdue
    # Source : IRIS — Genere le 12/05/2026 21:44 — COMPLETE
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-12 21:44",
        "title": "Ukraine – Poutine : gains territoriaux, guerre perdue",
        "source": "IRIS",
        "url": "https://www.iris-france.org/ukraine-poutine-gains-territoriaux-guerre-perdue/",
        "composition": """\
**Limites** : 2022-2025 / perspective immédiate · Mondial (Europe, Afrique, Asie centrale, MO) · Sécuritaire, politique, économique, géopolitique

**§1 - PRÉAMBULE**
La guerre en Ukraine, déclenchée en février 2022, constitue le conflit armé le plus intense en Europe depuis 1945. Elle oppose la Russie à l'Ukraine dans un affrontement qui dépasse largement le cadre bilatéral. Ce conflit mobilise des ressources humaines, économiques et technologiques considérables. Il reconfigure les équilibres géopolitiques mondiaux de manière profonde et durable. Les premières offensives russes visaient une victoire rapide et décisive. Or, trois ans après le début des hostilités, la réalité du terrain contredit les ambitions initiales du Kremlin. Vladimir Poutine déclare désormais que la guerre touche à sa fin. Cette déclaration, paradoxale au regard des pertes subies, interpelle une profonde réflexion quant à la nature réelle des gains et des pertes stratégiques de la Russie dans ce conflit.

**§2 - QUESTION POSÉE**
Face à ce tableau contrasté, il serait judicieux de s'interroger sur la signification véritable du bilan russe dans ce conflit : les gains territoriaux obtenus compensent-ils l'affaiblissement géopolitique, l'épuisement économique et l'isolement international croissant de la Russie ?

**§3 - IDÉE MAÎTRESSE**
Bien que la Russie ait enregistré des gains territoriaux en Crimée et dans le Donbass, il n'en demeure pas moins que l'épuisement militaire, l'affaiblissement géopolitique global et l'isolement international progressif du Kremlin révèlent un bilan stratégique fondamentalement négatif pour Moscou.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les facteurs de résistance ukrainienne et de maintien du soutien occidental, les signes manifestes d'affaiblissement stratégique de la Russie sur plusieurs théâtres, et les perspectives de sortie de crise dans un contexte de négociation incertaine.

**§5 - ID1**
Les capacités de résilience militaire ukrainiennes, conjuguées au maintien du soutien américain et à l'engagement financier massif de l'Europe, sont autant d'éléments déterminants qui constituent le socle de la résistance ukrainienne face à l'offensive russe.

**§6 - IS11**
De prime abord, l'Ukraine a considérablement renforcé sa capacité de production militaire nationale. À ce propos, Kiev a notamment développé une industrie de drones de combat très performante. La multiplication des frappes ukrainiennes en profondeur sur le territoire russe en constitue un exemple éloquent.

**§7 - IS12**
Par ailleurs, le soutien américain en renseignement s'est maintenu malgré l'arrivée de Donald Trump à la Maison-Blanche. Dans ce cadre, Washington a continué de fournir des données de ciblage et d'analyse stratégique à Kiev. À titre d'illustration, les frappes ukrainiennes précises contre des dépôts logistiques russes témoignent de cette coopération persistante.

**§8 - IS13**
De surcroît, l'Europe a assumé un rôle de financeur majeur de l'effort de guerre ukrainien. En effet, un prêt historique de 90 milliards d'euros a été accordé à Kiev pour soutenir son économie et son armée. Ce financement massif vient corroborer la détermination européenne à maintenir la pression sur Moscou.

**§9 - Conclusion P1 + transition**
Partant, la résistance ukrainienne repose sur une combinaison solide de capacités propres et de soutiens extérieurs qui ont contrecarré les calculs initiaux du Kremlin. Il en est de même pour l'affaiblissement progressif de la Russie sur ses autres théâtres d'influence.

**§10 - ID2**
Outre les facteurs de résistance ukrainienne, les revers diplomatiques conjugués aux échecs militaires sur d'autres fronts et à l'épuisement intérieur constituent l'essentiel des indicateurs d'un affaiblissement stratégique profond de la Russie.

**§11 - IS21**
Assurément, la mobilisation massive des ressources russes en Ukraine a privé Moscou de sa capacité à soutenir ses alliés ailleurs dans le monde. À cet égard, le régime de Bachar el-Assad en Syrie s'est effondré sans que la Russie puisse l'en empêcher. Cette chute est révélatrice de l'étirement dangereux des capacités militaires russes.

**§12 - IS22**
De même, l'influence russe en Afrique subsaharienne a subi des revers significatifs. Dans ce même ordre d'idée, le groupe Africa Corps a essuyé des défaites face au JNIM et au FLA au Mali. À en croire les analystes de l'IRIS, ces revers signalent une érosion nette de la présence russe sur le continent africain.

**§13 - IS23**
De surcroît, l'influence russe en Asie centrale connaît un recul notable au profit de la Chine et de la Turquie. À ce titre, plusieurs républiques centrasiatiques renforcent leurs liens avec d'autres puissances régionales. Cette recomposition illustre parfaitement l'affaiblissement du rayonnement géopolitique de Moscou.

**§14 - Conclusion P2 + transition**
Dès lors, la Russie apparaît affaiblie simultanément sur les fronts ukrainien, africain, syrien et centrasiatique, révélant les limites structurelles de sa puissance projetée. Ces constats nous amènent à examiner les perspectives de sortie de crise et les conditions d'une négociation possible.

**§15 - ID3**
Outre l'affaiblissement sur le terrain et le recul géopolitique global, les dynamiques intérieures russes, les opportunités de négociation manquées et le poids croissant du coût humain et économique restent des leviers à même de faire évoluer la trajectoire du conflit vers une issue négociée.

**§16 - IS31**
Effectivement, la société russe montre des signes croissants d'épuisement face à la durée et au coût de la guerre. Dans ce même registre, la répression intérieure s'intensifie pour contenir une contestation qui progresse silencieusement. Comme c'est le cas des familles de soldats mobilisés qui multiplient discrètement les protestations contre les autorités.

**§17 - IS32**
Aussi, l'opportunité d'une négociation avec Donald Trump a été manquée par Vladimir Poutine. À ce propos, Washington avait proposé une levée partielle des sanctions en échange d'un statu quo territorial. La posture inflexible de Moscou en témoigne éloquemment, révélant une rigidité stratégique préjudiciable aux intérêts russes à long terme.

**§18 - IS33**
Enfin, le coût économique de la guerre pèse lourdement sur les finances russes malgré la hausse des revenus énergétiques. En effet, les dépenses militaires absorbent une part croissante du budget national au détriment des investissements civils. Ce déséquilibre structurel constitue une aubaine pour les partisans d'une résolution négociée du conflit.

**§19 - Conclusion P3 SANS transition**
Ainsi, les pressions intérieures, les opportunités diplomatiques inexploitées et l'insoutenabilité économique progressive du conflit convergent pour dessiner un scénario où la Russie sera contrainte, tôt ou tard, d'accepter une sortie de guerre à des conditions qu'elle n'aura pas pleinement choisies.

**§20 - Reformulation de l'idée maîtresse**
En définitive, si la Russie a effectivement étendu son emprise territoriale sur la Crimée et une partie du Donbass, ces gains limités ne compensent pas l'ampleur des pertes stratégiques subies. Le maintien du soutien occidental à l'Ukraine, l'affaiblissement russe en Syrie, au Mali et en Asie centrale, l'épuisement de la société russe et le refus de saisir l'opportunité de négociation offerte par Trump révèlent un bilan global négatif pour le Kremlin. Poutine a engagé une guerre qu'il ne peut ni gagner pleinement, ni conclure favorablement dans les conditions actuelles.

**§21 - Ouverture**
Par ailleurs, la recomposition en cours des alliances internationales, avec le renforcement du flanc est de l'OTAN, l'émergence d'une industrie de défense européenne autonome et le rôle croissant des puissances moyennes dans la médiation de ce conflit, annonce une nouvelle architecture de sécurité mondiale dont les contours redéfiniront durablement les équilibres stratégiques du XXIe siècle.""",
    },

    # -----------------------------------------------------------------------
    # COMPOSITION 6 — Africa Climate Talks / COP32 Addis Abeba
    # Source : UNECA — Genere le 13/05/2026 16:29 — COMPLETE
    # -----------------------------------------------------------------------
    {
        "date": "2026-05-13 16:29",
        "title": "Africa Climate Talks call for stronger negotiating capacity and implementation-focused COP32 in Addis Ababa",
        "source": "UNECA",
        "url": "https://www.uneca.org/stories/africa-climate-talks-call-for-stronger-negotiating-capacity-and-implementation-focused-cop32",
        "composition": """\
**Limites** : 2026-2027 (post-COP30, préparation COP32) · Afrique / mondial · Environnemental, politique, économique

**§1 - PRÉAMBULE**
Le continent africain représente moins de 4% des émissions mondiales de gaz à effet de serre. Pourtant, il subit de plein fouet les conséquences du dérèglement climatique. Les sécheresses, les inondations et la désertification y compromettent la sécurité alimentaire de millions d'habitants. Les négociations climatiques internationales constituent le cadre multilatéral privilégié pour traiter ces enjeux. Cependant, la capacité de l'Afrique à peser sur ces négociations demeure insuffisante. La tenue de la COP32 à Addis Abeba en 2027 offre une opportunité historique au continent. Ce contexte interpelle une profonde réflexion quant à la capacité de l'Afrique à transformer cette opportunité en résultats concrets pour ses populations.

**§2 - QUESTION POSÉE**
Il serait judicieux de s'interroger sur la manière dont l'Afrique peut renforcer sa position dans les négociations climatiques mondiales, afin que la COP32 d'Addis Abeba génère des avancées tangibles en matière d'adaptation, de financement climatique et de résilience pour le continent.

**§3 - IDÉE MAÎTRESSE**
Bien que l'Afrique demeure vulnérable face au dérèglement climatique et marginalisée dans les processus de décision multilatéraux, il n'en demeure pas moins que le renforcement de sa capacité de négociation et la mobilisation de coalitions continentales solides constituent des leviers déterminants pour faire de la COP32 un moment de mise en œuvre concrète et d'équité climatique mondiale.

**§4 - ANNONCE DU PLAN**
Pour s'en convaincre, seront examinés successivement les enjeux liés au renforcement de la capacité de négociation africaine, les impératifs de financement climatique et de mise en œuvre, et les conditions d'une appropriation continentale et communautaire des solutions climatiques.

**§5 - ID1**
Les lacunes en matière de préparation technique, conjuguées à la fragmentation des positions africaines et à l'insuffisance des ressources humaines qualifiées, sont autant de faiblesses structurelles qui constituent le principal obstacle à une négociation climatique africaine efficace.

**§6 - IS11**
De prime abord, la faiblesse des équipes de négociation africaines compromet la défense des intérêts du continent. À ce propos, de nombreux États africains envoient des délégations réduites aux COPs, manquant d'experts thématiques spécialisés. La 7ème Africa Climate Talks d'Addis Abeba en constitue un exemple éloquent, ayant explicitement placé le renforcement de la capacité de négociation comme première priorité continentale.

**§7 - IS12**
Par ailleurs, la dispersion des positions nationales affaiblit le poids collectif de l'Afrique dans les négociations. Dans ce cadre, les 54 États africains peinent à parler d'une seule voix face aux grands émetteurs. À titre d'illustration, les divergences entre pays exportateurs de pétrole africains et îles vulnérables sur la transition énergétique ont parfois fracturé le bloc africain lors des COPs précédentes.

**§8 - IS13**
De surcroît, l'absence de groupes de travail thématiques permanents fragilise la continuité des positions africaines entre deux COPs. En effet, la préparation des négociations se fait souvent dans l'urgence, sans capitalisation sur les sessions précédentes. La recommandation des Africa Climate Talks de créer des groupes de travail dédiés vient corroborer cette analyse, en proposant la rédaction de notes analytiques pour guider les délégués africains.

**§9 - Conclusion P1 + transition**
Partant, le renforcement de la capacité de négociation africaine passe par des équipes plus étoffées, une coordination continentale renforcée et des groupes de travail permanents. Il en est de même pour les enjeux de financement climatique et de mise en œuvre, qui conditionnent la crédibilité même du processus multilatéral.

**§10 - ID2**
Outre les déficits de capacité de négociation, le manque de financement climatique accessible, conjugué aux insuffisances de mise en œuvre et aux pertes et préjudices non compensés, constitue l'essentiel des obstacles à une action climatique africaine efficace.

**§11 - IS21**
Assurément, le fossé entre les promesses de financement climatique et leur décaissement effectif demeure un obstacle majeur. À cet égard, les pays développés n'ont toujours pas pleinement honoré l'objectif des 100 milliards de dollars annuels promis depuis 2009. La COP32 d'Addis Abeba est révélatrice à ce sujet, car elle s'inscrit dans un contexte où la crédibilité des engagements financiers internationaux est gravement mise en doute.

**§12 - IS22**
De même, les mécanismes de pertes et préjudices restent sous-financés malgré leur création formelle à la COP27 de Charm el-Cheikh. Dans ce même ordre d'idée, l'Afrique supporte des coûts colossaux liés aux catastrophes climatiques sans compensation adéquate. À en croire les participants des Africa Climate Talks, la COP32 doit impérativement démontrer des progrès tangibles sur ce dossier, au risque de perdre toute légitimité aux yeux des populations africaines.

**§13 - IS23**
De surcroît, le Premier Bilan Mondial issu de la COP28 a révélé que les trajectoires actuelles restent insuffisantes pour limiter le réchauffement à 1,5°C. À ce titre, l'Afrique doit préparer ses contributions nationales déterminées de troisième génération (NDC 3.0) en tenant compte de ces constats. La 7ème Africa Climate Talks, qui a spécifiquement examiné les implications du Bilan Mondial pour les NDC africaines, illustre parfaitement ce constat.

**§14 - Conclusion P2 + transition**
Dès lors, la crédibilité du processus climatique international dépendra de la capacité à transformer les déclarations en actions financées et mesurables. Ces constats nous amènent à examiner les conditions d'une appropriation africaine et communautaire des solutions climatiques, seule garantie d'une mise en œuvre durable.

**§15 - ID3**
Outre le renforcement de la capacité de négociation et les impératifs de financement, la valorisation des solutions endogènes africaines, l'intégration des communautés locales et le développement de marchés carbone équitables restent des leviers à même de garantir une mise en œuvre réelle et durable des engagements climatiques.

**§16 - IS31**
Effectivement, les communautés locales doivent être co-créatrices des solutions climatiques et non simples bénéficiaires. Dans ce même registre, les savoirs locaux, les droits fonciers et la justice de genre constituent des fondements indispensables aux solutions fondées sur la nature. Comme c'est le cas des initiatives agroforestières sahéliennes portées par des femmes agricultrices, qui combinent résilience climatique et sécurité alimentaire avec un faible coût.

**§17 - IS32**
Aussi, le développement de marchés carbone africains équitables et transparents représente une source de financement endogène stratégique. À ce propos, les Africa Climate Talks ont insisté sur la nécessité de systèmes de surveillance robustes, de traçabilité fiable et d'interopérabilité entre marchés. L'initiative de la Grande Muraille Verte, qui commence à générer des crédits carbone certifiés au bénéfice des communautés locales, en témoigne éloquemment.

**§18 - IS33**
Enfin, le renforcement de la capacité scientifique africaine et les liens entre universités, instituts de recherche et ministères constituent un atout décisif. En effet, une science africaine robuste légitime les positions de négociation et alimente des politiques publiques adaptées aux réalités du continent. La recommandation des Africa Climate Talks de créer des espaces d'apprentissage intégrés reliant recherche et gouvernements constitue une aubaine à ce sujet, notamment en vue de préparer COP32.

**§19 - Conclusion P3 SANS transition**
Ainsi, l'appropriation communautaire, le développement de marchés carbone équitables et le renforcement scientifique africain forment ensemble les piliers d'une mise en œuvre climatique crédible, ancrée dans les réalités du continent et capable de peser sur les négociations mondiales.

**§20 - Reformulation de l'idée maîtresse**
En définitive, si l'Afrique demeure la région la plus vulnérable au dérèglement climatique tout en étant la moins responsable de ses causes, il n'en demeure pas moins que la 7ème Africa Climate Talks d'Addis Abeba a tracé une feuille de route claire. Le renforcement des équipes de négociation, la création de groupes de travail thématiques, l'exigence de financement climatique effectif, la prise en compte du Bilan Mondial dans les NDC 3.0, et l'intégration des communautés locales comme co-créatrices de solutions constituent les axes prioritaires. La COP32, qui se tiendra à Addis Abeba en 2027, offre à l'Afrique une occasion sans précédent de faire basculer le processus multilatéral de la déclaration vers la mise en œuvre concrète, équitable et mesurable.

**§21 - Ouverture**
Par ailleurs, le Maroc, fort de son expérience en tant qu'hôte de la COP22 à Marrakech en 2016 et de son leadership reconnu en matière d'énergies renouvelables, dispose d'un positionnement stratégique pour accompagner les préparatifs de la COP32, en partageant son expertise diplomatique climatique avec les pays africains et en renforçant les coalitions Sud-Sud qui seront déterminantes pour l'avenir de la gouvernance climatique mondiale.""",
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
            entry = (
                f"\n---\n\n"
                f"## {comp['date']} — {title}\n"
                f"**Source** : {comp['source']}\n"
                f"**URL** : {comp['url']}\n\n"
                f"{comp['composition']}\n"
            )
            f.write(entry)
            existing_titles.add(title)
            added += 1
            print(f"  + {title[:80]}")

    print(f"\n{added} composition(s) ajoutee(s) dans {ARCHIVE_FILE}")


if __name__ == "__main__":
    main()
