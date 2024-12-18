# Sonar-Car
Autíčko, které jezdí po místnosti a vytváří její mapu.

## Použité součástky

- 2x RPi Pico
- [Motory kol](https://www.laskakit.cz/dc-motorek-130-3v-16500-rpm/)
- [Otočná kontaktní průchodka, 4 vodiče](https://www.laskakit.cz/otocna-kontaktni-pruchodka--4-vodice/)
- [Ultrazvukový senzor vzdálenosti](https://www.laskakit.cz/ultrazvukovy-meric-vzdalenosti-hc-sr04/)
- [H-můstek řadič L9110S](https://www.laskakit.cz/h-mustek-radic-l9110s/)
- [Krokový motor 28BYJ-48](https://www.laskakit.cz/krokovy-motor-28byj-48/)
- Mecanum Omni Wheels
- Drátování

## Software tohoto projektu je rozdělen na 3 části:

### 1. Program pro řízení vozítka
Tento program bude řídit pohyb vozítka v souřadnicovém poli. Bude přijímat příkazy k pohybu a posunutí o určitý počet souřadnic (např. 10 cm) v daném směru. Zahrnuje:

- Řízení motorů omniwheelů pro pohyb ve všech směrech.
- Komunikaci přes sériovou linku s druhou deskou.
- API pro přijímání povelů k pohybu o určitý počet souřadnic v daném směru (dopředu, dozadu, doleva, doprava).
- Překlad příkazů na konkrétní pohyby omni kol pro dosažení požadovaného cíle v souřadnicovém poli.

### 2. Program pro mapování místnosti
Tento program bude kromě mapování také přijímat aktuální polohu vozítka od skriptu pro řízení vozidla. Zahrnuje:

- Vytváření mapy místnosti, kde jedna jednotka bude reprezentovat 10 cm v reálném světě.
- Aktualizaci mapy na základě nových dat z ultrazvukového senzoru.
- Ukládání dat do pole, které reprezentuje mapu místnosti.
- Poskytování těchto informací skriptu pro řízení vozidla.

### 3. Skript pro řízení vozidla na základě mapy
Tento skript bude řídit pohyb vozidla na základě aktuální mapy místnosti a bude poskytovat aktuální informace o svém pohybu programu pro mapování. Zahrnuje:

- Analýzu dat z mapy a aktuální polohy k rozhodování, kam se vozidlo má pohybovat.
- Generování možných směrů pro pohyb vozidla.
- Výběr z těchto směrů takový, aby se vozidlo pohnulo pryč a zároveň zabezpečit, aby se v dalším kroku nevrátilo zpět.
- Odesílání vybraného směru programu pro řízení vozidla.

## Instalace a spuštění

### Požadavky
- Python 3.x
- Tkinter
- Paho MQTT
- Matplotlib
- NumPy
