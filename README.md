# DA_BAIGIAMASIS_DARBAS

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir python programavimo pagrindų kursui

**Darbo autoriai:** [Roberta Lukaševičiūtė](https://github.com/rchyvas) ir [Julius Serbenta](https://github.com/Julius0991)

**Projekto tema:** Sergamumo užkrečiamomis ligomis analizė

**Projekto tikslas:** Apžvelgti užkrečiamų ligų ir jų gydymo tendencingumą nuo 2010 metų iki dabar.

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

**Panaudotos bibliotekos:** pandas, matplotlib, seaborn, datetime, numpy

1. Suradome penkias labiausiai paplitusias užkrečiamas ligas ir nusibraižėme jų grafiką;

<img width="700" alt="Screenshot 2023-11-15 at 20 33 11" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/a96cc7be-333c-496d-bee5-877128fd04f5">

2. Suradome labiausiai paplitusių užkrečiamų ligų tendencingumą pagal metus;

<img width="423" alt="Screenshot 2023-11-15 at 21 33 35" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/a740bf3e-f05f-43b2-9c06-c9bceec50137">

<img width="423" alt="Screenshot 2023-11-15 at 21 28 22" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/49b5cfe7-7c7b-412c-857b-0ef34c41bda5">

<img width="423" alt="Screenshot 2023-11-15 at 21 27 36" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/3d2bc706-e58e-415f-ad4c-66397cbc3710">

<img width="423" alt="Screenshot 2023-11-15 at 21 26 42" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/58fc9a60-0847-4f6c-9904-5d200b43e5ae">

<img width="423" alt="Screenshot 2023-11-15 at 21 25 48" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/db244f14-079c-4d2e-b2b6-cc436b5cf674">

3. Suradome informaciją apie sergamumą labiausiai paplitusiomis užkrečiamomis ligomis ilguoju laikotarpiu;

<img width="564" alt="Screenshot 2023-11-15 at 22 41 52" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/15f18304-f5a8-4fdb-af92-a40c3aed072e">

4. Suradome informaciją apie ligonių, sergančių labiausiai paplitusiomis užkrečiamomis ligomis, gydymą 

<img width="425" alt="Screenshot 2023-11-16 at 00 16 34" src="https://github.com/rchyvas/da_baigiamasis_darbas/assets/149396134/c43f38a4-3445-4de8-ae65-fb0627336362">

## ANALIZĖS IŠVADOS

Penkios labiausiai paplitusios užkrečiamos ligos sudaro maždaug 60% visų duomenų bazėje esančių nurodytų ligų - dažniausiai lietuviai susiduria su įvairaus pobūdžio [plonosios žarnos uždegimais ir vėjaraupiais](https://user-images.githubusercontent.com/149396134/283218699-a96cc7be-333c-496d-bee5-877128fd04f5.png). 

Panašu, kad šias penkias ligas galima skirstyti į sezonines - kai kurios labiau pasireiškia žiemos pabaigoje-pavasario pradžioje ([Rotavirusų sukeltas enteritas](https://user-images.githubusercontent.com/149396134/283227754-a740bf3e-f05f-43b2-9c06-c9bceec50137.png), [Vėjaraupiai be komplikacijų](https://user-images.githubusercontent.com/149396134/283227123-49b5cfe7-7c7b-412c-857b-0ef34c41bda5.png)); kitos aktyvesnės vasaros mėnesiais-rudens pradžioje([Kampilobakterijų sukeltas enteritas](https://user-images.githubusercontent.com/149396134/283227160-3d2bc706-e58e-415f-ad4c-66397cbc3710.png), [Salmonelių sukeltas enteritas](https://user-images.githubusercontent.com/149396134/283227196-58fc9a60-0847-4f6c-9904-5d200b43e5ae.png)); dar kitos dažnesnės šaltuoju periodu, t.y. rudens pabaiga-žiemos mėnesiai ([Norovirusų (Norvalko (Norwalk) veiksnio) sukeltas ūminis gastroenteritas](https://user-images.githubusercontent.com/149396134/283227219-db244f14-079c-4d2e-b2b6-cc436b5cf674.png)). 

Stebint bendrą sergamumą, rotovirusų sukeltas enteritas yra ne tik dažniausiai pasitaikanti liga - jos sergamumo rodikliai taip pat yra labiausiai linkę staigiai pakilti ir staigiai nukristi. Taip pat grafike galima pastebėti ir Covid-19 įtaką, nes pandeminiu laikotarpiu visi nurodyti sergamumo rodikliai [ženkliai sumažėjo](https://user-images.githubusercontent.com/149396134/283242811-15f18304-f5a8-4fdb-af92-a40c3aed072e.png).


