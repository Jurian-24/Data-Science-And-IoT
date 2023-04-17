
# Data Sience And IoT

## Introductie

Dit project is voor het keuzevak Data Science and IoT, op de Hogeschool Rotterdam. Ik heb dan ook mijn uiterste best gedaan om een goed en werkend project neer te zetten. Hiervoor heb ik een aantal dingen gebruikt namelijk: 

- Raspberry 4
- MacOs apparaat waar XCode op staat
- Python 3
- Een afstand sensor (HC-SR04)
- Male & Female bedradingen
- Ionic (voor de mobile app)
- Gpiozero (librarie voor de afstand sensor)
- VNC viewer
## De gedachte achter dit project

De afgelopen tijd ben ik steeds meer gaan letten op lichaamstaal bij mensen waar ik een gesprek mee heb. Hier kan ik meestal zien of ze het gesprek leuk vinden of niet. Door wat zelfstandig onderzoek te doen ben ik erachter gekomen dat mensen vaak verder van je af staan als ze het gesprek niet leuk vinden of niet interessant genoeg vinden. Dit wilde ik graag testen!

Ik ben gaan nadenken over hoe ik een afstand sensor kan gaan gebruiken om te bepalen of mensen het gesprek leuk of niet leuk vinden.

## Het plan van aanpak
Nadat ik wist wat ik wilde maken ben ik begonnen met het plan van aanpak samen met onderzoek wat IoT nou precies is en hoe ik dit kan combineren 

## Data pipeline

#### Wat is een data pipeline?

Stel je voor dat je thuis een tuin hebt die je wilt bewateren, maar dat je niet elke dag naar buiten wilt om het handmatig te doen. Daarom besluit je om een systeem te creëren dat automatisch je tuin bewatert op basis van de weersvoorspelling en de vochtigheidsgraad van de bodem.

Hier is hoe een pipeline zou kunnen werken voor jouw tuinbesproeiingssysteem:

- Verzamelen van data: Allereerst moet je data verzamelen van verschillende bronnen, zoals een weer app of een bodemvochtigheidssensor. Deze gegevens kunnen automatisch worden verzameld en naar een centrale locatie worden gestuurd voor verwerking.

- Schoonmaken en voorbewerken van data: Zodra je de gegevens hebt verzameld, moet je ze schoonmaken en voorbewerken om ervoor te zorgen dat ze nauwkeurig en bruikbaar zijn. Je moet bijvoorbeeld eventuele ontbrekende of irrelevante gegevens verwijderen of de gegevens omzetten naar een formaat dat gemakkelijk kan worden geanalyseerd.

- Analyseren van data: Vervolgens ga je de gegevens analyseren. Je kunt bijvoorbeeld kijken naar de weersvoorspellingen en de vochtigheidsgraad van de bodem om te bepalen wanneer je tuin water nodig heeft.

- Bouwen van een model: Op basis van de geanalyseerde gegevens kun je een model bouwen dat voorspelt wanneer je tuin water nodig heeft en hoeveel water er nodig is.

- Implementeren van het model: Ten slotte implementeer je het model in het bewateringssysteem van je tuin, zodat het automatisch water geeft op basis van de voorspellingen en de vochtigheidsgraad van de bodem.

Mijn data pipeline:
![pipeline image](https://lh3.googleusercontent.com/RsRKodd4OBVE30SpDu075PVqAT34Z80hVbkRj9aLpe6-rBbqtFC7Iekx4PzKyYHJGG_TLHJ1Z5GHGjvG9BvSswFzc6aq5BLQQW9ltFu0R8T3nDu8MIuVfYcc5M6PGHlbNmS8FNpc0F8vzl8RzboGNDtiIxEK1ZrY469NX7pGfzgjXZEYCMdwXR_8ElT2kmStJotxAHa3CucowhNjVLZTwZJxij5NgCj4dMCTvTCXaRBPVXo2HeDsN9bvW5CRFlYVPowA0V5PZA0VwVSFqqCrDzabW3xRHZsSgXmnafHbKNWhR9RuI_gcS-iMkPdVqCde5l1-GVjPcmjPVOYCBSNY6_8i0fH8p8mkmt0bXdg63dW0vMuCONWlE4jOtrUyQZBrOzB4Rs__jwEvHExfveyvrMlRwe3h2bFEAspsub1KN_KMG30ZMezf7ueso2098VV53TFsSY0kl3zuu018meZZTFU2YbgKbiNzUL6EGthg9kZ2mffllSbfhv4_VNTK6BzGWiG1UPzcd-UOnJgLF_L0mknSivZXBuBXOjoGA9j5uDDFp2RbSeC79CXijZc9l8rXmTZzhcOf2vFBTPeFYeZJPwnuyKnvMlifCCxEHYobIhlFQnAISJW0_bYtkvsi8LboErcnP0yYyNJ_jij9Wi4IXGfnzBgKnY9kekKmenwrUjm7yzHqFJoOItlINF4z9MxIaLvVavXOK2llCN7E_hN-svsp8qHe29XO7QyKuRdewINWgaceWR24CDVaLgK9JZQY32O_Vqi-jmoc4RgOvqOWkkWWgWBzLgw3m1w9KfoHXVbT9KiKCxOYl6PTlfpOaNJgnOSetkBex99r1r57RDGFm1_rSA-BtSEr28_4XnU43SpdNqFvpZIKO_kQaHSUox2o6r1sYfT_Dy8phBf2eizehzloWtU6pLgwF3o20ademMoLf-HRcI6X4IIqHlFOj7D2kBw2egsARHT6av12SQ=w1080-h1080-s-no?authuser=0)

## Demo
Demo video: https://youtu.be/5Y9-NMg3k7U

## Installaties

### Raspberry Pi

**VNC viewer**

Om je Raspberry Pi vanuit een andere computer te kunnen besturen moeten we een remote desktop applicatie installeren. Hiervoor gebruiken we VNC viewer omdat deze veilig en al geinstalleerd staat op je Raspberry. Om deze te aan te zetten moet je de volgende stappen uitvoeren.

Hoe zet je VNC aan? Mijn uitleg: https://youtu.be/sNrSnWoMmww

Als je een Raspberry Pi heb aangeschaft staat er hoogstwaarschijnlijk al een versie van Python op met de bijbehorende libraries. Om dit te checken voeren we een paar commando's uit.

Voor de python versie:
```bash
python --version

Of

python3 --version
```

Nu we weten of Python geinstalleerd is kunnen we kijken wat de versie is van de library van Gpiozero. Gpiozero staat standaard geinstalleerd op de Raspberry Pi maar we kunnen dit checken. Maak een bestand aan genaamd: main.py.

Plaats hier de volgende regels code in: 
```python
from pkg_resources import require

print(f'Version -> {require("gpiozero")[0].version}')
```

Voer dit bestand vervolgens uit. Als het goed is moet er iets staan zoals:

```bash
Version -> 1.6.5
```

Mocht een van de commando's geen versie weergeven scroll dan verder naar wat er mist en voer de stappen uit voor het installatie proces.

**Python**

Voor dit project heb je minimaal Python 3 nodig. Open hiervoor een command prompt/terminal op je computer en voer het volgende commando uit:

Voor windows:
https://phoenixnap.com/kb/how-to-install-python-3-windows

Voor MacOS:
```bash
$ brew install python3
```

Voor Linux:
```bash
$ sudo apt-get install python3.6
```



**Ionic**

Voor de mobile app maken wij gebruik van Ionic. Voer de volgende commando uit om het te installeren:

```
$ npm install -g @ionic/cli
```

## Het proces

### Het project aanmaken

Om dit project lokaal te gebruiken moet je het volgende doen. Download Visual Studio Code (VSC): [Klik hier!](https://code.visualstudio.com/download)

Maak een mapje aan op de desktop met de naam die jij zelf wilt. Ik heb hem dataScience genoemd.

![App screenshot](https://lh3.googleusercontent.com/bGzneGKkVqSzRwsw4YIIezmpFeigr3vNNKdV-Vp0f2czWsiN2psbpxXO7Qn5dMifcC34KqeL9Qnvo3CshYWk8wScEAy9Pv7BGTXq6l1rf_xszLD0x-Uv57TZ_ujveIJ0cd9YGpAvDF8f-C-fPD2kNRXbXZ5jypQUgJHP2RiNLH-SsYpe81aAl21lkE5Z6Hova81Cm0XsbdCGDa_kAHV45cfVVmydqS_bamyFE4El3__7xc3gzyr3SmK1y3PsQqo9omOmYjlzSLoVChULOjtk3So3t-Wucmu7T58J6mfSM1RRv3eKe5ucK5lY3NKEbN0mfJAIyadPLytrvDoC7Y3r1zWZaMF9K3riaFlEq3OSzPk2n7QwIaKcUTtKJWzeTd91cbzHqPbXvELflMGtJpGPCLcuFtS1_E2Xm6VE0XEpC8ieF1Lz7FR5t7ug-lC3HZrq8c6TL-ia0v7GYJO6Zxd3kBEdS7l9qpuci_1OtYdJGmIkj1NmBcD_RjwsAyomUdQJziU2bEvlaDsfeXRpJbpYFrk21oA4BnuY_fDjqPXv_PQ5a0PhyB5-FnyglKJYUb9S-Fem_WjeQTREptmtTvqAAEgpwwq9YD5Doe5UvMrzBy8n6k5ETte3uGf_pq36LU8iaO0Ic5IlUs1lbkD4ist6kg_kFu1yT-UV5fROZFoedR3XgntC5FVFaxOacWrUQn8Avv5W1T7GM6rp3m5JX4ri6cyeA0VzFL2jSTMaBFm_YWsycYFaqnSPCI2l7ive9dj61BrX2KSHRJX-7q4qJSGjawhNUozCYQaF3CynYPDW0Q8wDuACjKWAhyViYnuFGslJ2YRxaLHfL2dFn_LYT9kcfHbVdPkeTXEmwZ5m9W7IAedgQDVURjT0DQ5zIuRGaXxI5dZlGK9BfKJUcw4oLdb1AEenAbkJVUPoagWFGMWvt_3bel1wg2PHGytw0vpN2_mQEkpGQhKRxTW8mRiU2A=w462-h448-s-no?authuser=0)

Open VSC na het installeren en maak een mapje met de naam die jij zelf wilt. Hier komt de ✨magie✨!

Voer de volgende commando's uit door op CTRL + ` te drukken of open een nieuw terminal venster door in VSC naar View -> Terminal te gaan. Als het goed is heb je nu een venster dat er ongeveer zo uit ziet: 

![App Screenshot](https://lh3.googleusercontent.com/rvXDo0yu9S2b1zGmdLY6MSL61dQjvMh2-rWlNe8CIhs9bpFgGxpNsnj5-ZoxfMkkK3iyJqRyrIAXmjRjm89ZAz_sp4nZtbdSotSN2EMHXhNXBpfc5VFVTOAxT3Bg-Zkz4lgNNWTYRS50lk4pD3L6qe764uyNacplhYuzK1Z7DkP9IuyeDp40VTLDlv61UvKfOJlqXtCxSAOxNuLK6INMK1mVW3bi4_yEGfmWoUNsa21Okdywn0LPP34Gsxh_C_itA5NKH5bU5OnDPX1N60TUHZywkJYv42gInk8leEvxPTygE5aD3D9WKhzfQr93VzMsyfujc9SkP8Wnpsdbj7aaDskpAtM7HEuDoYoBjdoVWVTPUjFLIqrxJZlF1scpICJGppq4XKhcGEQD0QS2lwFB1aHCVbM_chG86usOL-tXHcmdUspnrOAh4nvkt1Moy2erZf_JlSLl6Fwj6JaKgd0_k_My6Z5Vc3F0OnergpXIv2hlm9_5GQVLsDZr-ZPjbbH0jiTLndgAR4jjfDubyLX_m8DTfI33pXzYduha-Ro6t6YrGZqaIH7ibtamDFlr7Z-yahrPEfDMX-aC_mMoP8r-IvE6-TBGK-3SHQ9B4z6R6H0YFYUTerYFD3v3m7uF3XCokiq6CEt7TEuW1k3VmmuWqg3n9u8qd2QfkGrerQGKpLdT-fOjxTJOOnWgRe-WIAoCnkHcznMR4E1yN07_9euEsY6Nxf0FTSc_P7XLTaXY5sOyMYLv1D4uUWzIIihj_u5k6OxmvbuwXP3Y416jtV2siFqzN2bQmvjwwTCLVJz6Sfv6vMc6nEQcgidPv_6IwyYgwKJfAWbphM0uosO_fjWXwddioa-Cc4ehQkKIbHFfWhOF9Q27KWcaRmq3fYwP07olsyAJf8H8swc5LV-5pBuHQEpjq0SIvTR1ToT-BNy_p9NpXw_E2BNqrqrxymj-WN5ZSrDCQ9xDSJc2TdcoEQ=w2664-h1668-s-no?authuser=0)

Plaats vervolgens in deze terminal (afhankelijk van jouw besturings systeem) de volgende commando's:

#### Git installeren:
```bash
Voor windows:
https://git-scm.com/download/win

Voor Mac:
$ brew install git

Voor Linux:

$ sudo apt install git
```

#### Het project clonen:
```git
$ git init
$ git clone git@github.com:Jurian-24/Data-Science-And-IoT.git
```

Als het goed is zou je nu zoiets moeten hebben:
![App Screenshot](https://lh3.googleusercontent.com/CDSWntXAlNoLRwk04in9o181SsXAQJbDjvHFNhBrr1SWrsQ7x6j3Dr3RYQ1MQsa2od4eAxDUUmvThnGQIajLXdhhExhzd0WT6DLiPtUHdXxpTzplMoSglYJyuC71Z4Onwmj1Sd-3rs05fvVpPd19EGQrcJQm4rtoyIOchD7VMu9TBt0u3GbZjyjpJEqharpLW7rYGWxNIVelNfN9X-qUDxr1V4dkoI8_RzopfHdVAkXwzJDQ3bzyAZNpzog8pWKMiu2YFk4gtX8jVZuQaK_-oIODuKnBxhiRDb2LKX-bZQX0mnv3d8p_FWep4MikGxAny1v2lxUSEE90dd52smhLfIUiGAjclYnweN3Njg3cPiRYhgKZsKCdPs6JYmBGewcNViu6WY9SR6xMujCSXDVOPhzKekm47MKGtTwSXBIiSjuEY-3lqXKH997U1R6p_Wg3xkpLWhHk0YL1qk8IGkC5kwf2kD-0KzFlYcs6yZt8jTjXzzY6FEHzIXPVw5vt2cRTpqcT0xYjuYp7r29UeOj53WrebF_Guwpu6rRX0zKFtA_df7ka2WJ14e16I3SvhPVsamGjihVGYaxxjO4pV4tXDuUkAzlsEtrz7gg95BWGJz4vwMRNYLDfCUZCZxRQbZRPtkLBRUIJ5_tOxLfb7nL1cCNoOyhuFfGbDxyliNE1NxFh7O-iuOm7s-h0HI7kwnc_A62iIDUaIn2u3fdaKdUVqGO63W26PTrljfCSc_CWrmU9dj3bwxmLoyaB50aQifSeNrRkOwz66G5lciu6CsxnFgRVFlqluNHzva4-xooahdYtMawGiinJiMMU41A35IVYQ9rPE0AuNv9ORSCrSKUjatYPbAiSBpm9hTUO6I79wcq1UO2926lhgVfZYg2qB-PefWDFz2Hc1soe0Ucyoo1BgKzUk8k439HkgoWVPeNFI_Y9_SUmibXXqdXbD994ds55c_Oxj2-oV6fnOP9aXQ=w718-h449-no?authuser=0)

Voer vervolgens de volgende commando's in de terminal uit:

```bash
$ cd Data-Science-And-IoT
$ cd Ionic
$ npm install
```

Je hebt nu het gehele project geinstalleerd🎉

Nu komt het wellicht wat moeilijke gedeelte. We gaan de afstand sensor(HC-SR04) verbinden met de Raspberry Pi. Ontkoppel de stroom van de Raspberry en verbind de Male & Female snoertjes op de volgende manier:

![App screenshot](https://lh3.googleusercontent.com/qG4UC-IYurn9_MrMbla7JUmFQk_5lwapU-X9UdnJKbFs6P3CeKIHvB6l_Zu_aAZfOaAMBmykGGFrJCDIO4FErOS8XL85px1BahLvks4GdSFtNYjuhCN08rB_avX9LXJav40ACeo5rbwvViZgdfdA4JIVzafvABhoXJiSaumvdG66toKlSxTctcXf7X7ZZaBO9sOxGKxqsWrGs1GT1S_KcOXMlOROAh7zi_2t2CpmEg43EK6BJ4tZv-5XneHvUx_GSCC6zi-LDWYmOILfJQI5zOUEOMq-7Cgwhd_TYnsXUs-dZu6X9D3IK1D5W_qRii7_oZ4G9B7v_1VkRGO4q2RRuXA5VDV1y--n2Cjf9WIa_SDeK8UJ-ZHztjfCbDZ6p9o--3RjzloKxVRIZXX32LbUTMJfhgfHzhPyRn-hCk4ijJ8sHWtWmC7WB6XNTHkiUzKYreTWW4uaC-_sTxMbIGPTF4nhH0cwRbO9as-1wqgxKcGV23fDn6GwHXnZTPEr8DrIscsM1ohth2BFigw-0R3Klh1Nr4qZpVQaLfEZPWUFpiIG4VtAd6Dyqobf9qiWYQPMGdkVjW3fBrp1vjNHGR2D4qherTUEwinkwm-PxpA4UfvBNBQ5SU1Ls8ZDC8wrahnnyB1DRfpIk7WZXeeBzuBCRgqjs8a1rPmDiIS-arAtZDD82kXGNzSHHG030xrfw4HKBIy4h2yIo2uQD3WxNRLDVG2GHJym_p6YJMpt8ecY6AFNQu1ahQfyQYgZyqWAJLfhkWjx11z74shDB3a057UnpEt-HaEHxA4f_pukMK-VpI0oM6m6n1VIktYFGFekYg2UeaoQbESDav6ZfBt_3EYdXkRX0gLE4zdCMz7bhdy75WnWtv4vZwXH5hp5ljPD4O8RBpKP-astDCT7RFrUDphVQfhQzzPuiymQcOVjjcqgu-06cv2ub_0PdavTyyllbLZ0ezrIKQtOgRJ-Nbx1eA=w424-h316-no?authuser=0)

Sluit de voeding van de Raspberry weer aan en als het goed is kan je nu data wegschrijven! LET OP: Het is echt noodzakelijk de de verbinding van alle draden goed vast zitten en in het juiste gaatje!

Als je wilt beginnen met het wegschrijven van de data kan je dat op 2 manieren doen. De eerste manier is via de VSC terminal door simpelweg op de run knop rechts bovenin te drukken.

De 2e manier is via een terminal op je Raspberry:

Weet je nog het mapje dat op je desktop staat? Mooi! Die gaan we nu openen via de terminal. 

Open een terminal en voer de volgende commando's uit:
dataScience = de naam van jouw mapje
```bash
$ cd ~/Desktop/dataScience
$ ls
```

Als het goed is zie je dit nu:

![app screenshot](https://lh3.googleusercontent.com/iKGGLg9C9c3lsAwNLbP1KKTLyEwfWhwzSVXAHBayjRP6er7yXbyHzKJV8yHk6M1V59Tw8CFJk6EGazD6Mxytwcn3Mm10deAedO7KelAoxkCCDWz6GxgkUNaRH6tYDxShoZX0ycxAEjoIx3fIQPoi6AMBauPr3y34ncj7-Wy4GPLjaSxX5sioHz9jX1iNtqoQiNN4JQYLGJlP0kBhdOLx41C-Yi4TLMYlzqnmLgNhvDsvm9rApTr0IoOZ6rmJGZQ_ILrxvxDDF-c6zt-y73hlgFLSpiu_Yk5yKHkwe_vOcXcfixd1V17JE7g6Q7OtsbtxJqPDHvvqxdOItHFEPduOMg_nQG3FQCB1p0yrslfeLEQ9Hs29E9nHI-kPhnG-r5g2_hERQUjYCcKRq9R7D16ALlEGIgP8X5mNojyRaVgOcxn2ELItuKvnJqak7reC5Xdr1qCx2HPZmHr_j4AL7hiA3RRyl797li-MxiReYl14qzNT8yq7BPNAneBJqkGcGhS-_WKif__Ck88ez_PL0LRMwCw9jN4J0wKpHVZzexrM8VXvInTdJh838yi1cHIfYUFxKNTj9gYC5h28ZcrJM-p-vzGMID1gMDOUwNa8zBVozHmBmcpzYL7-mTI6dkfhVZvu0Fa2apcGtEU6ZgYZzd-LBHtNRwxnpyTDdtIqME1TvkUc3WLf33zalAg7qjyIrvjhXuMgJRykY2_IqQdDhu1ck5Ocfx-U49gc6rT4J4RYSKJA_XykQvby07mpvTuwp9koM5wkTW7WI9FhXGbpv9jbIFZ3-l95dXZoFqsPCLs4-1tXxkh890mQqdS38D1pX5vJVcZ5CbtkzBDrLZ-8giIS-xsadg1gVJyriJxtRG3sHe65NyequlXPtCxnGPXZ7V-GZaU7xiGRxNCE7PhG7a1Hoo0WF2A4Qm-4CHj4f6Dm3bFC9flQnjYPPd2eB1BVbdb4ACa80J6ixR2MhWcCjQ=w662-h336-s-no?authuser=0)

Voer vervolgens deze commando's uit: 

```bash
$ cd python
$ python3 main.py
```
Dit is het resultaat:
![app ss](https://lh3.googleusercontent.com/bT6rAAICSsyjDmIkgY0Z6hcMB55wDYuQm3DxAc-FWzZn8OFNBaswY0-l2QKAVVg9eITf5yXepr5sS3LZAF3MUrERUole_yUehYqmQg0KQ3ZAy4LC5fw15QzHpZKWNZw_zOHH2Ecd4CSck8G7NpzK3KSy02teFxvaNeQlCGpusfKrladVtgwK1xCDPXJyDl1rHo24g6NXQGsGsLuOa81S0QfEOxJJYs-QxxaF33QXEbpSj7hucsuTi9QSBFByNogdHlfGMpiMUcN1e7OHsLli6E4oytPv9116pGYwwZvUsVuyYOHi-x2_Im76gMl8Ctc8kv-antMnNz0sQjGEhhEX4dZwZMe6-_7nh7vA7U-e-Bp2R0wSw5-bIx3_t08S31wjebwDKw0QPuWr75brMxRT7W6r0iRMsiq4_X84I_oxDHqptlDnmsGPvaGOwek4LIs9VtikYhwNFtitM0GWQm1KFFRRlwFUTD_3LLSn9sVhSaeq5DwjpKuJTWqXIH4bC9Qqelt-KxDPdzj5c9lzPVPRj2obYpSXBX514AsZ5eJ-ofw8n3mKNaa3Xsr0WPY53IAFWe0OO6YGhkv9itPiHtW9ADkOV4-igyz3rwZYiha3D8d1jdAAdfOS3XNElYpacCJZKAVPrbGqnLX_oiLXQboj1fLA2IURH9mkY7A842Rx0NREvKSeLnpZ58fFbZg-SGUKKcX7cLQXtyXPzDUW70Wch43wIH2t7P7yi0YQP1VwNLkb2x4m6gG6JbIH6jrHeJ4c9u5tkKPSDNTsUiVOLIhLw3AI5hpXbraBTDzDiUE3vSO4WBqsE5WeOM9QvKf7PMdKL38AeQntHxrFz91euvW11AQJsbgQJDrEzjR13YRT6SD7NeIqAWELOUDQAK1lwa3hTxoxsSNOjl4T5sA0KIelnN6xq4KXbUC4nsOlVobTwtm96lzrqdvFXKyDzdA3jreouyIvhf1sRFpHx0f2zg=w846-h526-s-no?authuser=0)

Als je op CTRL + C klikt dan ga je door naar de volgende vraag. Terwijl de vragen worden gesteld wordt er om de seconde de afstand berekend en opgestuurd naar Thingsspeak

### Ionic

Nu komen we bij het mobiele gedeelte die de data ophaald. Hiervoor is wel een computer nodig met een MacOS besturings systeem. Als je dit niet tot je beschikking hebt kan je helaas de data niet uitlezen. 

Herhaal het installatie proces van VSC & de Github repository en voer daarna de volgende commando's uit in de VSC terminal.

```bash
$ cd ionic
$ ionic cap add ios
$ ionic cap build ios
```

Dit opent vervolgens XCode en daar kunnen we de app in een simulator runnen. Wacht heel even tot XCode is opgestart (dit kan heel even duren omdat het een groot project is wat we inladen). Druk vervolgenns op het play icoontje links boven:

![app ss](https://lh3.googleusercontent.com/jMpnvB_zfmgbYl7BYfDT-hX2ZhQSmVNAEhLjGuVno-VL-KTmOwb0tjtcaJxXmB3xwz1ZUQmbu-8sLDWPdwKnDJMWOy2jjNMwZxD4Nxz63QTIl4x7Nz2ZDUNoEOoevsd9VHE6SeLeP_cZYMyEpbgf5himDa7RG10-YF_XJyCyIqwnQaJLGxQVLmyF6Ull92C7vw1rPI0NiPlOEYrXpRMb8HlXQemTJKp3clDeZDYtgUwYl9zR6Pv0R_pQOpqmu0cLLh6x62HEu0fvijID4BkL1m1a12svYtMwcWQcpHtCc5xb-qhqpiUlhp4Df1Kqbe5_Wz7iivnIwZ1ZloQ41qbaHs9XjpaMooT7h6w_h-tPggjjYCkwDpbOLEI2mstIxL__qpZoW-byNw20pKxsCBATF1UqW4htMjq0kYoKEH5-vZLU1QLXThKREm4uabEnlSrLs5BlXhCzG5CVtGl-1hmG59f9M9f7IyaWInpg6lF9VAFHJPZlRhxAVy15hdD8mn4Gfpx2l7rUQR-CePDUHCMsV1Y7xG135CKmWFCUzIsKjMHlJ7yWKl2xoUlzvtQB0TGrke3Tdt2VCFk7dWE2Dsmsr4wzNQC372ZbDyFC2PQNnrP8T4ndvYbXH_NGiLtlt5jam-oUL820MmPYG3zc6p21Ila79mB6KGMk0O2K4pbS8IGFtdz5EGd9HApqgvtAzCWE4Bm3aHObqhtX7jtiz_PEJ7h8qZXOeNmH-sael_QG619d-JQFIpQZbuYcm_Pg9tvQR9rLTXTcqrICPTEQT_LP6Bt9v7eRhCYFk5AescN1MncUruxRFAQzLO3p9X_bTEACnw6bKQ2luN0gYrx1FhEbvWuFATswoNuDYfWsLArUdXXFuV4pGf96rmXj7Vfq7mKPrEbQ2xoX1FNRm4PCbA4SgS2WjPH6Yw3K0521dvN-kPEFs8ORLk5n1eHLebml7eZaRx_jpMIFdtJjw-PLiw=w1828-h66-s-no?authuser=0)

Je wordt vervolgens begroet door een IPhone simulator:

![app ss](https://lh3.googleusercontent.com/DyNel_woDTf7oQN2oek_jn9An7KXkCZz8KBAXZp9yk_pEEwfYUIHqi2umZmuTMzjdaGxdT3h_73p2i7lFwewasz_WfFyD1yPnY9ZwUduv7hkPvJkJ75xOepxV2oVQXV2exd0-Xx1J2EBhUiYSvIOjM5rE7zurX0v6y6UXZmQr8QRzxMcSOgDafjanQGpuF6t5xLGMy3G3mfiMr7EkBs3jo2uTzsLpV6Oq7581g3wCbKl3I-OQnXzztkzxKuWAiBa8kuj3funOENrJ1kJI7QJfcFXLHDxIeECfq3KcCHMqQOUbfeEjjbmJ5_XJiaJIKJwNNBvqlrL0TuYzte2ZL4Ksm4Tprg4Slvr38hMEsS47G84szc3B5nAsFpb_MLZpGVB5WQ0Yu63Ic75yAbbIuX7P7rCg6insZOFYzLrFS9YNr-K0_b0KcBrV8nHRLlHtg1jRqS-QZB6A9KrEo2b2vm_Eb_G0n8L1-PkfEuGJ4cNKb3XrnmkUcEF9kTd9qvsGAw8Afiyo-cSkkgXM3I5aHZ7xiRCfkmvjELlU3uhGyDKg6iovnbzEwXLdZh9E2Prq7HCn3LTEuUpfNu20MnE9zc-5poN5I-zITnPlw2dSzHrrrKg5iZfjacKDiCDJSUJtNHjsm11FgEjep57YBtJaFh-3LFrGwQp94DLlE64RIpoK5dJk_G0FlJPnkH0fXD6AKZWnximKcl5GH7b3RDeuIbGGAvgbigAFvs0BMhaWm_iPKY_tH7bd8VPbpBnNH--uV1mHfNZYkBjKjx7dfCVqSACb5Bb0o4FFkwt_EWX_JA0nywSLxTUhNf__S_ll4TarMqwJWCME_I3yKHjYr7FD3iXWCtsisFNUfwlAC-rG4iR2X2_Dycv5L1zA4e0GFuTQGxUtRykrrmZe5qxKNdF9OJaKEucT4NbXDuU89ZnAs9fwaon7lY4i7sOZJpY-dKGMTxAOUUn2tEF-avepFeyRw=w1794-h1668-s-no?authuser=0)

#### ✨Magie✨

Je kan vervolgens het ID van de geinterviewde persoon in de inpu field zetten en op de knop "Get data" drukken. Vervolgens krijg je een response van een groene check (als de persoon geinteresseerd is in het gesprek) of een rood kruis (als de gebruiker het niet leuk vind)

Groene check:
![app ss](https://lh3.googleusercontent.com/kPm5YuwIlWyjQdcmGKTb7oB-oeakMdFZ3zHCKL7jaTBMVRD61R3aqKT9u31W3-756tFQY9IJlv-nbWLbcckkrp9GzNhxjr6LL_UamcfAm9Sd5OBWTv5daImfZN5N2c8Lun2s1hwuS7fbkC6ov3OrfWJeSFDzzLGl7tLsBCxCVeYRMDAbiK9Wt7LLuzw1tALhGVSFn8wfP0w2oUWZi7VTW8Rzx0Fl2G9-QzihMMTRwfoCS7SyrpQd4yTZ-901Gxe3j3Omodt4wcvr2FQk71qv0Go1Dx7LrVQQYwj8R3bwFbEOegXrLDs3I3pfvIq3RjkuVWc22CNHXZFZKgGnaRKelD9x52lt6BUshyagHyjKHKfDrGKqI2pIXt7eXdoE3vX3l-T1cNJYYHUBGNhTrqUKWJymWbg3uu-KxEOTA2SZZSZjV6TFkHLSUyq2UljXqb6SdiliFrazxvlMdj3N77KQCWi34dzxwX3-MC7O5qb1zyYwxNRW3FAD6ksrSzMJ3ulGNSNVoYZjwCXp23F8u-cxPcg55KnsI-xLvrCu3f0KCSuu8VBSKii875r0uF1642I3hD1zyKnyHMW71PF6PeOu3W0MS4xFimagHFgK1hRx0mFupP5La5HV1PWwoCxBXmQ7kmtTCeB0PcX9VCjUR63qjAAwE5mDVD-gfJI_S0NV5SXdYGrHYzekNgkEEa3BZmVLrH4TyL91k34xkTAnP4Xol2hol3YJnPPL8e2ej-dbHOx-rdoJmSErCEF9rz7dRi-DJd17l7sxEf-KxEfDYUo1JMHRAF0JlR1tlqN-PuxdSN6tUisyV6MiDjTF2j260S5Qr3EK5kiQTiLC-pVJGLqFKPO444ZS_vi5CovtoFQTnJ2TZzTKoV-6CfxYVu0heE4iy-arA1tly5Y43Bv1vh3QwUNK1xWbAQaFRgPmPgwJjujwddg_b7RQyujKFxfeMivjew-Pa6V15iou7lu1gQ=w772-h912-s-no?authuser=0)

Rood kruis:
![app ss](https://lh3.googleusercontent.com/OTUSMHgemGHfHUILUUqUsbpBVeHFgre8nnsCbZC6V-omrdPS5Z0lwwOCPjGAGb7e7Vqwk7knlmQek5EIjElJutzN_oBouLxwe65biSl_VE1z1XhByVRYPqGlbuoZHOkubPI80hdJraB--QrVoad-L7c5rhkpK7KVbWnPJ2dGHxGLNcjn7GV-pUFQv7a6wJvsgwrYyTWNkDog5t7yCo05oTxRBm2rVVFV1lOwQxyQx9bIRHo_jwUzhP-60CDttUFKaFHfDSHt2dp_cH2wzPhod3OSxHm33Hlu5gKzVOV56_vMug-SXJ1oM0feuJu5neyk0iA8lXPQFvcPg2vxTgnmnJS_8UuoYyYmQuWTkne7UaqhHCr5NSFWux_RoILd1tvWfSmqrsvvf0_FQ9d1MT3P2KVP9s2cIYaTUCKfrBPlLCOopn2lChX57_3MLJgPWdq2sI4lktG2NbKKhOpS2ToLyMX_NgoUb6H40H3Gv8WzmmOv5lUDsYZn8jE0Srcjklql4LDX-ic24jk41aejLYF__egU-IDqwrWm98iPCZVsV1plHBwxyVObJUuE0rOaL2WBWa6TbSa-Z5BAApNsqVic515Akvd_lRxNINUBKZnltXUA-i-SZjigUp9BdHAT4fwZ6sHYDZ1xBV9lAa4E3Hls-HIRNa1YOZ11_HpvrttlT4jyy3J8Agfu8cSNgeeOBTZ7Jab1QrZyhxwVFewiBFFFWeH6HM2OGsGbKmPkRrx2thg1MZrA5z2JE8AzcUgHfSXsuAVN9LRibpRxoBubXJU5LbquIoFlJDa9hvqdfD-E6Prdwy_bjhQA--IWmf8qIty6TrLy7s0w2wcJdqMDWtJb_gHo6Lfk-0l9-8NlD8lk15CBFPNhG-DIacEgYjR2GFdcV8MHmhsEn0ma4IVjnNium6h8pFpxFkdl-Q5OcTegy7fYWretKzd-lAjAso3JAeYXt-d1mcz98xVfAthh2w=w772-h942-s-no?authuser=0)

Gefeliciteerd! Je hebt succesvol deze applicatie geinstalleerd!🎉

## Code Uitleg

### Python code: 

```python
<<MAIN.PY>>

from time import sleep # Makes it possible to send the reading to thingsspeak
from logic.Person import * # Import the person class
from api import * # Import the writing functionality
from gpiozero import DistanceSensor # The sensor that makes it possible!

# Convertion from M to CM
def getPos():
    distance = sensor.distance * 100
    distance = round(distance, 2)
    return distance

#
def getPosition(personID):
    distances = []

    loop = True
    while(loop):
        # Check for keyboard interruption
        try:
            # Get and convert the distance
            distance = sensor.distance * 100
            distance = round(distance, 2)
            # If the distance > 10M (maximum) print that it needs to be configured. Can occure if a person is moving to fast.
            if(distance != 1000.0):
                print(distance)
                distances.append(getPos())
                # Write to thingsspeak
                API.write(distance, personID)
                sleep(1)
            else:
                print("Needs to be configured!")
                sleep(1)
                continue
        # Stop the question and continue to the next
        except KeyboardInterrupt:
            loop = False
            return distances

if __name__ == "__main__":
    # Distance sensor (HC-SR04) setup
    sensor = DistanceSensor(23, 24, max_distance=10)

    # Creation of a person
    id = input("ID: \n > ")
    firstName = input("First name: \n > ")
    lastName = input("Last name: \n > ")
    startPos = 100
    print("first question")
    firstQuestion = getPosition(id);
    print("second question")
    secondQuestion = getPosition(id);
    print("third question")
    thirdQuestion = getPosition(id);

    person = Person(
        id,
        firstName,
        lastName,
        startPos,
        firstQuestion,
        secondQuestion,
        thirdQuestion
    )

    try:
        # write the person to json (is now turned off)
        person.writePersonToJson()
        print("Data has been written to JSON!")
    except:
        print("Something went wrong")

```

```python
<<API.PI>>
import requests

class API:
    # create static method in order for it to be called everywhere in the code withour creation an API instantiation
    @staticmethod
    # Write the code to the thingsspeak field based of the given field (person ID)
    def write(value, field = 1):
        requests.post(f"https://api.thingspeak.com/update?api_key=N7QUSQSDA8IUJM89&field{field}={value}")

    # Code for testing the GET method of the API more info in the Ionic code below!
    def get(field = 2):
        response = requests.get("https://api.thingspeak.com/channels/2094803/feeds.json?api_key=X6OZE8XX2HH3L7VF&results=8000")
        response = response.json()

        data = response['feeds']

        test = []
        for item in data:
            test.append(item[f'field{field}'])

        return test[::-1]


```

```vue
<template>
    <ion-page>
        <ion-header>
        <ion-toolbar>
            <ion-title>Main Page</ion-title>
        </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true">
        <ion-header collapse="condense">
            <ion-toolbar>
            <ion-title size="large">Tab 1</ion-title>
            </ion-toolbar>
        </ion-header>
        <!-- start of the form -->
        <ion-grid>
            <ion-row class="ion-align-items-center">
            <ion-col size="4"></ion-col>
            <ion-col size="4" class="ion-text-center">
                <ion-item>
                    <ion-label>Enter ID here:</ion-label>
                    <!-- put the person ID in this field -->
                    <ion-input id="id-field" aria-label="Enter ID here:"></ion-input>
                </ion-item>
                <!-- button for getting the data -->
                <ion-button color="primary" @click="getDistance()">Get data</ion-button>
                <!-- show the easter egg or show the red cross/green check -->
                <lottie-player v-if="showImage" :src="imageSource" background="transparent" speed="1" style="width: 75%; height: 75%;" autoplay></lottie-player>
                <img v-if="showCapy" :src="imageSource" alt="">
            </ion-col>
            <ion-col size="4"></ion-col>
            </ion-row>
        <!-- end of the form -->
        </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script>
import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonButton,
    IonGrid,
    IonCol,
    IonRow,
    IonInput
} from "@ionic/vue";
import { person } from 'ionicons/icons';

export default {
    name: "tab-page-1",
    data() {
        return {
            id: 0,
            personData: [],
            imageSource: "",
            showImage: false,
            showCapy: false
        }
    },
    components: {
        IonPage,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonButton,
        IonGrid,
        IonCol,
        IonRow,
        IonInput
    },
    methods: {
        // get the ID in the form
        receiveID() {
            this.id = document.getElementById("id-field").value;
            if(this.id != null) {
                return this.id;
            }
        },
        // get the distance data
        getDistance() {
            // receive the ID
            const personID = this.receiveID();
            const personData = [];
            let obj;
            this.showImage = false;

            // get the data from the API
            fetch('https://api.thingspeak.com/channels/2094803/feeds.json?api_key=X6OZE8XX2HH3L7VF&results=8000')
                // format the data
                .then(res => res.json())
                .then(data => {
                    obj = data['feeds'];
                })
                // foreach 'feed' in the received data only get the data from the given ID from the form
                .then(() => {
                    obj.forEach(element => {
                        try {
                            const newInt = parseInt(element[`field${personID}`])
                            if(!isNaN(newInt)) {
                                personData.push(newInt);
                            }
                        } catch (error) {
                            console.log(error)
                        }
                    });
                })
                // calculate if the person was interested in the conversation or not.
                .then(() => {
                    const sum = personData.reduce((partialSum, a) => partialSum + a, 0);
                    const avg = (sum / personData.length)

                    // check if the average distance was below 50 cm (interested in conversation)
                    if(avg < 50) {
                        //determine if the image will be an easter egg or not
                        const rndInt = Math.floor(Math.random() * 1000);
                        if(rndInt == 69){
                            this.showCapy = true;
                            this.imageSource = "https://external-preview.redd.it/lPGMRn-cDmoLcOWEKqJIhiZKb35_nsdhBQLVon-8bo0.png?format=pjpg&auto=webp&s=827495651278171413c9c5e3fa5ec2411b0c8456"
                        } else if(rndInt == 420){
                            this.showCapy = true;
                            this.imageSource = "https://media.tenor.com/qu3ChHRA6O4AAAAd/gort.gif"
                        } else {
                            this.showImage = true
                            this.imageSource = "https://assets1.lottiefiles.com/packages/lf20_niyfyoqs.json"
                        }
                    } else {
                        this.showImage = true
                        this.imageSource = "https://assets5.lottiefiles.com/packages/lf20_pqpmxbxp.json"
                    }
                })
                // log any errors
                .catch(error => console.error(error))
        }
    }
};
</script>

```

## De IoT Pipeline
![pipeline](https://lh3.googleusercontent.com/_g9icb8LKyqXnaSf_4tgwL9kKC7CofvhweDFDX2cgP7L-XuDCFHw6zhDoOiWRG2bTjK77toQvQvQoueyMMrrqa6P2F19UyMZRLhaX3vuJxSFyVPCr-ES7PbARKHTl_E53YzQdOjS5_8uUee4akhG-puc7bsfggBG6eFf3jF7ylhLXq1Fb8bRGEZYTP5CqSua01IuHl1hdttYW13ma9XY1_5jyRxM7yvs0BBDJBP2DL7NT14bMkE_GUpSEU2uks034RSxiHMaBnMJQ9eVTPDHO4n9SpM5Q4ZgnGIZZjwL-7_Gh4hxmShmyBbC7tPNie_RSCFR-qJAHLCKZqkB4TsY32U4q0DRUi1ZfRXHhFA4-1bIWZan8FGr-Gu-yH0GpPpTdyCYSE_MdLCGxHeWmO-5t_m_wfEmq1euaV6_-XRWnPFdmvo8OcbfPG3fWyEQzuMtpTB3B7l-wPCqY4wTIYlN0eXcTOMbVzHbLulJZREg2xaVt7mCx6DGK0U7E3A2bnqqg5G2Zw9pswupl9p5cFsrJ15gA70iBa1SPN7BQ6yG6V2ZyBdzhvt0KJ_tyAvIPY6zMwHWfbaHF7w1jOr-y0kRgHgihAyGDIo0wVb01hu6G0NnE60NxlkDgjJsOB2zeVL3KFPg8djfpp76vl9sNSY12zUt9Rz4L6EH2jrbORcCg4tGe05MyMwSkpvbSdjJ9X8387sGFHJc3wxl1QJBZ-BDS2spz_eK_iG74hm-8TRKPKzt8TEiQHVxwvAdQMez9mpea0XRroPOgBH8uVS82hCRBOb9JZXqzbVURK82S0bVN2bQGKw9K5xvYTHJ76wAEfFL4xWYidm6fhuZAsCp0W9w8IRpR2JMSXYNeznzx-Q6AZehdjnuZe-CAebFCaSAmX2Pd-udKaWAFYB3qFQeW8j20TRm_n53HWdfYXaBzeRyNM7_ZKLy0nj2f4TF26O9_MMKctH2CELpJmS7CqmuDw=w1080-h1080-s-no?authuser=0)

## Conclusie

Ik heb met veel plezier dit project gemaakt. Ik heb veel geleerd of een hoe een Raspberry Pi werkt, bedradingen, hoe je lichaamstaal kan aflezen en hoe ik mooie readme's kan maken! Ik denk dat dit project geslaagd is omdat ik op een hele IoT pipeline heb opgezet vanaf scratch.
