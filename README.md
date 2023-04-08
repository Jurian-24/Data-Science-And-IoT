
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
## De gedachte achter dit project

De afgelopen tijd ben ik steeds meer gaan letten op lichaamstaal bij mensen waar ik een gesprek mee heb. Hier kan ik meestal zien of ze het gesprek leuk vinden of niet. Door wat zelfstandig onderzoek te doen ben ik erachter gekomen dat mensen vaak verder van je af staan als ze het gesprek niet leuk vinden of niet interessant genoeg vinden. Dit wilde ik graag testen!

Ik ben gaan nadenken over hoe ik een afstand sensor kan gaan gebruiken om te bepalen of mensen het gesprek leuk of niet leuk vinden.

## Installaties

**Raspberry Pi**

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

Open den terminal en voer het volgende commando uit:
dataScience = de naam van jouw mapje
```bash
$ cd ~/Desktop/dataScience

```












