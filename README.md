# DA_BAIGIAMASIS_DARBAS

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir python programavimo pagrindų kursui

**Darbo autoriai:** [Roberta Lukaševičiūtė](https://github.com/rchyvas) ir [Julius Serbenta](https://github.com/Julius0991)

**Projekto tema:** Sergamumo užkrečiamomis ligomis analizė

**Projekto tikslas:** Apžvelgti užkrečiamų ligų ir jų gydymo tendencingumą nuo 2010 metų iki dabar, (...)

Darbas atliktas Python kalba, panaudojant Postgres duomenų bazę ir json failą.

## PROJEKTO SEKA

**SKREIPINIMAS.PY**

**Panaudotos bibliotekos:** requests, pandas, json

1. Suradome analizei reikalingus duomenis apie užkrečiamas ligas iš [Lietuvos atvirų duomenų portale](https://data.gov.lt/datasets/1852/) esančios [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenų bazės](https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji);
2. Išsirinktus duomenis suformatavome .json formatu;
3. Gauti duomenys buvo žodyno formato, todėl atsirinkome raktus, pagal kuriuos išsifiltravome duomenis;
4. Duomenis iš skreipinimo eksportavome dataframe formatu

**DATABASE.PY**

**Panaudotos bibliotekos:** requests, psycopg2, pandas

1. Duomenis iš skreipinimo.py failo importavome dataframe formatu;
2. Prisijungėme prie Postgres duomenų bazės, kad galėtume sukurti duomenų bazę;
3. Sukūrėme naują duomenų bazę, kad galėtume lokaliai saugoti atsisiųstus duomenis;
4. Sukūrėme funkcijas, kurių pagalba duomenis sukėlėme į susikurtą duomenų bazę;
5. Sukūrėme funkciją, kuri duomenis iš naujos duomenų bazės eksportavo dataframe formatu

**ANALYSIS.PY**

-------------------

## ANALIZĖS IŠVADOS

-------------------
