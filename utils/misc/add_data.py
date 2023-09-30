import psycopg2
from data import config

categories = [
    {
        "name": "📲 Telefonlar"
    },
    {
        "name": "💻 Noutbuklar"
    },
    {
        "name": "Macbook",
        "parent_id": 2
    },
    {
        "name": "DELL",
        "parent_id": 2
    },
    {
        "name": "Asus",
        "parent_id": 2
    },
    {
        "name": "Acer",
        "parent_id": 2
    },
    {
        "name": "iPhone",
        "parent_id": 1
    },
    {
        "name": "Samsung",
        "parent_id": 1
    },
    {
        "name": "Xiaomi",
        "parent_id": 1
    },
    {
        "name": "Vivo",
        "parent_id": 1
    },

]

def add_category(name, parent_id=None):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Categories (name, parent_id) VALUES (%s,%s)"""
        record_to_insert = (name, parent_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Categories table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Categories table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def add_category_to_db():
    for category in categories:
        add_category(name=category.get("name"), parent_id=category.get("parent_id"))


products = [
    {
        "name": "iPhone 14 Pro 8/256GB Silver",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://images.uzum.uz/cdq98a2vtie1lhbe1arg/original.jpg",
        "price": 15612999,
        "category_id": 7
    },
    {
        "name": "iPhone 14 Pro Max 256 GB ",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://images.uzum.uz/cjavcrkjvf2nv3nn5rog/original.jpg",
        "price": 17465000,
        "category_id": 7
    },
    {
        "name": "Apple iPhone 13 Pro 256 ГБ ",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://static.sello.uz/unsafe/x500/https://static.sello.uz/fm/20230810/c4fa1942-5796-4fe3-9168-2fd550a247da.WEBP",
        "price": 14600000,
        "category_id": 7
    },
    {
        "name": "iPhone 13 6/128GB",
        "description": "Phone bilan ishlashning yangi sehrli usuli.\nHayotni saqlab qolish uchun yaratilgan innovatsion xavfsizlik xususiyatlari.\nAjoyib tafsilotlar uchun innovatsion 48 megapikselli kamera.\nUlarning barchasi smartfonlar uchun eng yangi chip bilan jihozlangan.\nHar qanday smartfon oynasidan ko'ra bardoshli keramik ekran bilan. Suvga chidamli. Jarrohlik sinfidagi zanglamaydigan po'lat.",
        "image_url": "https://images.uzum.uz/cifat5r6edfostii340g/original.jpg",
        "price": 11999999,
        "category_id": 7
    },
    {
        "name": "Galaxy A54 5G 8/256 GB",
        "description": "OT: Android 13\nDispley: 6,4 dyuymli Super AMOLED - 1080 x 2340\nChip: Samsung Exynos 1380\nKamera: 3 (50 MP + 12 MP + 5 MP)\nBatareya: 5000 mA / soat\nOg'irligi: 202 gr.",
        "image_url": "https://images.uzum.uz/ck1guakjvf2qegt3ku30/original.jpg",
        "price": 5439999,
        "category_id": 8
    },
    {
        "name": "Galaxy Z flod  12/256 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor: Qualcomm Snapdragon 8 Plus, 8 yadroli\nRAM: 12 GB\nO'rnatilgan xotira: 256 GB\nEkran: 7,6 2176 * 1812 Dinamik AMOLED, 6,2 2316 * 904 Super AMOLED\nAsosiy kameralar: 50 MP + 10 MP + 12 MP\nBatareya quvvati: 4400 mA/soat",
        "image_url": "https://images.uzum.uz/cd02m570tgqvlm57tneg/original.jpg",
        "price": 5439999,
        "category_id": 8
    },
    {
        "name": "Galaxy S23 Ultra 12/512 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cjhm2akvutv1klhdlm00/original.jpg",
        "price": 16999000,
        "category_id": 8
    },
    {
        "name": "Galaxy S23 Ultra 12/256 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cj8jtp4vutv1p29khhs0/original.jpg",
        "price": 14599000,
        "category_id": 8
    },
    {
        "name": "Galaxy S22 Ultra 8/256 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cegk47ivtie1lhbf76lg/original.jpg",
        "price": 18999000,
        "category_id": 8
    },
    {
        "name": "Galaxy S22 Ultra 12/512 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cegkaegl08kcldtoudug/original.jpg",
        "price": 19600000,
        "category_id": 8
    },
    {
        "name": "Galaxy S22 + 8/256 GB",
        "description": "Mahsulot haqida qisqacha:\nOperatsion tizim - Android 12\nEkranni yangilash tezligi 120 Gts\nEkran turi Dynamic AMOLED 2X, HDR10+\n Corning Gorilla Glass Victus\nDiagonali 6,6 dyuym\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKamera 50 MP + 12 MP + 10 MP, LED chirog'i\n4500 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cjs6eokjvf2hdh3etu7g/original.jpg",
        "price": 14399000,
        "category_id": 8
    },
    {
        "name": "Galaxy S22 8/128 GB",
        "description": "Mahsulot haqida qisqacha:\nProtsessor - Qualcomm Snapdragon 8 Gen2\nOperatsion tizim - Android 13\nHimoya darajasi - IP68\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKameralar - orqa tomondan 4 (200 MP + 10 MP + 12 MP + 10 MP), old kamera 12 MP\n5000 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cjs6c3cvutvfmkmj80o0/original.jpg",
        "price": 11499000,
        "category_id": 8
    },
    {
        "name": "Xiaomi 13 lite 8/256 GB",
        "description": "Mahsulot haqida qisqacha:\nOlchamlari: 159,2 * 72,7 * 7,2 mm, Og'irligi: 172 g\nBatareya: 4500 mA / soat, tez zaryadlash\nAsosiy kamera: 50 MP + 8 MP + 3 MP, ikkita old kamera: 32 MP\nEkran: 6,55 dyuym, yangilanish tezligi 120 Gts, AMOLED displey\nProtsessor: Qualcomm Snapdragon 7 Gen 1. Operatsion tizim: Android 13, MIUI 14\nAloqa: Bluetooth 5.2, Wi-Fi 6, NFC, GPS, Glonass\nXavfsizlik: displeydagi barmoq izlari skaneri",
        "image_url": "https://images.uzum.uz/cjqo0srk9fq13g4536ug/original.jpg",
        "price": 4899000,
        "category_id": 9
    },
    {
        "name": "Xiaomi Redmi Note 12 pro+ 8/256 GB",
        "description": "Mahsulot haqida qisqacha:\nOlchamlari: 159,2 * 72,7 * 7,2 mm, Og'irligi: 172 g\nBatareya: 4500 mA / soat, tez zaryadlash\nAsosiy kamera: 50 MP + 8 MP + 3 MP, ikkita old kamera: 32 MP\nEkran: 6,55 dyuym, yangilanish tezligi 120 Gts, AMOLED displey\nProtsessor: Qualcomm Snapdragon 7 Gen 1. Operatsion tizim: Android 13, MIUI 14\nAloqa: Bluetooth 5.2, Wi-Fi 6, NFC, GPS, Glonass\nXavfsizlik: displeydagi barmoq izlari skaneri",
        "image_url": "https://images.uzum.uz/cipn2bt6sfhndlbqf400/original.jpg",
        "price": 4675000,
        "category_id": 9
    },
    {
        "name": "Xiaomi Redmi Pad SE 6/128 GB",
        "description": "Mahsulot haqida qisqacha:\nMobil platforma: Snapdragon® 680 4G\nRuxsat: 1920 x 1200, dyuym uchun 207 piksel\nYorqinligi: 400 nits\nOrqa kamera 8MP f/2.0 orqa kamera, 1,12 mkm piksel o'lchami\nBatareyani zaryadlash: 8000 mA / soat",
        "image_url": "https://images.uzum.uz/ck1u7hrk9fq74920gm4g/original.jpg",
        "price": 2290000,
        "category_id": 9
    },
    {
        "name": "Xiaomi 13 Ultra 12/256 GB",
        "description": "Mahsulot haqida qisqacha:\nMobil platforma: Snapdragon® 680 4G\nRuxsat: 1920 x 1200, dyuym uchun 207 piksel\nYorqinligi: 400 nits\nAsosiy kamera: 50 MP \n video: 8K@24fps, 4K@24/30/60fps, 1080p@30/60/120 \nOrqa kamera 8MP f/2.0 orqa kamera, 1,12 mkm piksel o'lchami\nBatareyani zaryadlash: 8000 mA / soat",
        "image_url": "https://fdn2.gsmarena.com/vv/bigpic/xiaomi-13-ultra.jpg",
        "price": 14600000,
        "category_id": 9
    },
    {
        "name": "Smartfon Vivo Y02T, 4/64 GB",
        "description": "Mahsulot haqida qisqacha:\nOperatsion tizim - Android 12\nEkranni yangilash tezligi 120 Gts\nEkran turi Dynamic AMOLED 2X, HDR10+\n Corning Gorilla Glass Victus\nDiagonali 6,6 dyuym\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKamera 50 MP + 12 MP + 10 MP, LED chirog'i\n4500 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cj6vnq56sfhggrk1nv7g/original.jpg",
        "price": 1299000,
        "category_id": 10
    },
    {
        "name": "Smartfon Vivo V27e 8/256 GB",
        "description": "Mahsulot haqida qisqacha:\nMobil platforma: Snapdragon® 680 4G\nRuxsat: 1920 x 1200, dyuym uchun 207 piksel\nYorqinligi: 400 nits\nAsosiy kamera: 50 MP \n video: 8K@24fps, 4K@24/30/60fps, 1080p@30/60/120 \nOrqa kamera 8MP f/2.0 orqa kamera, 1,12 mkm piksel o'lchami\nBatareyani zaryadlash: 8000 mA / soat",
        "image_url": "https://images.uzum.uz/cjvajl4jvf2hdh3fc0fg/original.jpg",
        "price": 4599000,
        "category_id": 10
    },
    {
        "name": "Smartfon Vivo Y27 6/128Gb",
        "description": "Mahsulot haqida qisqacha:\nMobil platforma: Snapdragon® 680 4G\nRuxsat: 1920 x 1200, dyuym uchun 207 piksel\nYorqinligi: 400 nits\nAsosiy kamera: 50 MP \n video: 8K@24fps, 4K@24/30/60fps, 1080p@30/60/120 \nOrqa kamera 8MP f/2.0 orqa kamera, 1,12 mkm piksel o'lchami\nBatareyani zaryadlash: 8000 mA / soat",
        "image_url": "https://images.uzum.uz/cjvapcjk9fq13g45rfm0/original.jpg",
        "price": 2644000,
        "category_id": 10
    },
    {
        "name": "Smartfon Vivo Y35 4/128 GB",
        "description": "Mahsulot haqida qisqacha:\nOperatsion tizim - Android 12\nEkranni yangilash tezligi 120 Gts\nEkran turi Dynamic AMOLED 2X, HDR10+\n Corning Gorilla Glass Victus\nDiagonali 6,6 dyuym\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKamera 50 MP + 12 MP + 10 MP, LED chirog'i\n4500 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cj6ithr0lbjbpr7feprg/original.jpg",
        "price": 2289000,
        "category_id": 10
    },
    {
        "name": "Smartfon Vivo V25e, 8/128 GB",
        "description": "Mahsulot haqida qisqacha:\nOperatsion tizim - Android 12\nEkranni yangilash tezligi 120 Gts\nEkran turi Dynamic AMOLED 2X, HDR10+\n Corning Gorilla Glass Victus\nDiagonali 6,6 dyuym\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKamera 50 MP + 12 MP + 10 MP, LED chirog'i\n4500 mА / soat batareya",
        "image_url": "https://images.uzum.uz/cf38d1ol08k0o9qhu6vg/original.jpg",
        "price": 3300000,
        "category_id": 10
    },
    {
        "name": "Smartfon Vivo Y15s 3/32GB",
        "description": "Mahsulot haqida qisqacha:\nOperatsion tizim - Android 12\nEkranni yangilash tezligi 120 Gts\nEkran turi Dynamic AMOLED 2X, HDR10+\n Corning Gorilla Glass Victus\nDiagonali 6,6 dyuym\nOg'irligi - 234g\nEkran - 6.8 Dynamic AMOLED 2* 120 Hz\nKamera 50 MP + 12 MP + 10 MP, LED chirog'i\n4500 mА / soat batareya",
        "image_url": "https://images.uzum.uz/ck216e4jvf2qegt3mo90/original.jpg",
        "price": 1699000,
        "category_id": 10
    },
    {
        "name": "Asus x515EA i3-1115G4 4/256 GB SSD 15.6 FHD",
        "description": "Mahsulot haqida qisqacha:\nEkran matritsasi turi IPS \nDrayvlarning umumiy hajmi 256GB SSD \n Drayv konfiguratsiyasi SSD \nXotira turi DDR4\n Operativ xotira 4 GB \nProtsessor chastotasi 3.0 GHz\n Protsessor Intel Core i3-1115G4 \nDispley turi Full HD \nDispley diagonali 15.6 FHD",
        "image_url": "https://images.uzum.uz/ck8hetbk9fq1var6g9mg/original.jpg",
        "price": 5699000,
        "category_id": 5
    },
    {
        "name": "ASUS Vivobook M1702Q Ryzen 5-5600H/8G/256 SSD/17,3 FHD",
        "description": "Mahsulot haqida qisqacha:\nProtsessor AMD Ryzen R5 5600H 4,2 gigagertsgacha (6 yadroli 12 ip)\nAMD Radeon RX Vega 7\nOperativ xotira 8 GB DDR4\nSaqlash 256 GB M.2 NVMe PCIe 3.0 SSD\nBarmoq izi sensori\nOrqadan yoritilgan klaviatura (klaviaturaning orqa nuri)\nDispley 17,3 dyuymli HD+ (1600 x 900) 16:9, IPS, LED yoritgichli, 60Hz, 200cd/m², NTSC: 60%, porlashga qarshi\nRang: muzli kumush",
        "image_url": "https://images.uzum.uz/ck06g2bk9fq749207pn0/original.jpg",
        "price":8500000 ,
        "category_id": 5
    },
    {
        "name": "Asus VivoBook P/N 90NB0WY2-M00R90/X1503ZA-L1502",
        "description": "Mahsulot haqida qisqacha:\nIntel UHD Grafikasi\nEkran o'lchami 15,6 dyuym\nEkranni yangilash tezligi 60 Gts\nOLED displey matritsasi turi\nEkran o'lchamlari 1920x1080\nProtsessor i3-1220P\nOperativ xotira 8 GB DDR4\nQattiq holatdagi disk 512 GB\nOperatsion tizim",
        "image_url": "https://images.uzum.uz/cjmcra4jvf2ofbh8aifg/original.jpg",
        "price": 7400000,
        "category_id": 5
    },
    {
        "name": " Asus Expertbook B5 Intel Core i5-1135G7 8GB DDR4 512GB SSD 13.3 Fingerprint",
        "description": "Mahsulot haqida qisqacha:\nProtsessor: Intel Core i5-1135G7\nOperativ xotira: 8 GB DDR4\nXotira: 512 GB SSD\nBarmoq izi skaneri bilan\nKamera: 720p HD Maxfiylik panjasi bilan\nGrafika: Intel® Iris® Xe Grafikasi\nBatareya: 66 Vt/soat, 4S1P, 4 hujayra, lityum-ion\n12 oy kafolat",
        "image_url": "https://images.uzum.uz/cilt0o75d7kom1tjj9k0/original.jpg",
        "price": 8100000,
        "category_id": 5
    },
    {
        "name": " DELL Latitude 3520 15.6 AG/Intel i3-1115G4/4/1000/int/Lin",
        "description": "Mahsulot haqida qisqacha:\nProtsessori: Intel® Core™ i3-1115G4\nDrayvlarning umumiy hajmi: 1000 GB HDD\nTezkor xotira: 4 Gb",
        "image_url": "https://images.uzum.uz/cctbfgv0tgqvlm57nu60/original.jpg",
        "price": 8600000,
        "category_id": 4
    },
    {
        "name": " Dell Inspiron 3501 i5-1135G7 8/256GB",
        "description": "Mahsulot haqida qisqacha:\nДисплей кенглиги: 1920x1080\nДисплей диагонали: 15.6\nЎрнатилган ОТ: Windows 10\nУмумий сақлаш хажми: 256GB SSD\nПроцессор: Intel® Core™ i5-1135G7",
        "image_url": "https://olcha.uz/image/700x700/products/2022-08-21/noutbuk-dell-inspiron-3501-i5-1135g7-8256gb-ssd-156-s100573468-100200-0.jpeg",
        "price": 6600000,
        "category_id": 4
    },
    {
        "name": "Acer Aspire 7 A715",
        "description": "Mahsulot haqida qisqacha:\nDiagonal: 15-15.9\nEkran o'lchamlari: 1080p to'liq HD\nQattiq disk turi: HDD\nOperativ xotira: 8GB",
        "image_url": "https://images.uzum.uz/ck1dghcvutvccfo27ng0/original.jpg",
        "price": 9300000,
        "category_id": 6
    },
    {
        "name": "Acer Predator Helios 300 PH317",
        "description": "Mahsulot haqida qisqacha:\nProtessor:i5-11400H\nXotira:16/512GB (DDR4/SSD)\nVideo karta:NVIDIA GeForce RTX 3050 Ti ",
        "image_url": "https://images.uzum.uz/ck1dkacjvf2qegt3jp60/original.jpg",
        "price": 16000000,
        "category_id": 6
    },
    {
        "name": "Acer Swift X SFX14",
        "description": "Mahsulot haqida qisqacha:\nProtsessor:AMD Ryzen 5 5625U\nXotira:8/512GB (DDR4/SSD)\nVideo karta:GeForce® RTX 3050 ",
        "image_url": "https://images.uzum.uz/ck1dfn4vutvccfo27n2g/original.jpg",
        "price": 10600000,
        "category_id": 6
    },
    {
        "name": "Acer Predator Helios 300 PH315",
        "description": "Mahsulot haqida qisqacha:\nProtsesor:i7-11800H\nXotira:16GB/1TB (DDR4/SSD)\nVideo karta:\nNVIDIA GeForce RTX 3050 Ti ",
        "image_url": "https://images.uzum.uz/ck1ddtkjvf2qegt3jmmg/original.jpg",
        "price": 16600000,
        "category_id": 6
    },
    {
        "name": "MacBook Air 13 M1 8GB/256GB",
        "description": "Mahsulot haqida qisqacha:\nO'rnatilgan: macOS\nRam: 8GB\nUmumiy saqlash hajmi: 256 GB SSD\nOg'irligi: 1,29 kg\nVeb kamera: FaceTime 720p HD kamera\nDispley ravshanligi: 2560x1600\nProtsessor yadrolari soni: 8 yadro",
        "image_url": "https://olcha.uz/image/700x700/products/2021-01-28/apple-macbook-air-13-m1-8gb256gb-2020-gold-20982-0.jpeg",
        "price": 11300000,
        "category_id": 3
    },
    {
        "name": "Macbook Air i5 8/512GB",
        "description": "Mahsulot haqida qisqacha:\nроцессор ядролари сони: 4 ядро\nҚаттиқ диск: 512GB SSD\nВазни: 1.3 кг\nЭкран: 13.3\nОператив хотира: 8 ГБ",
        "image_url": "https://olcha.uz/image/700x700/products/Eh9Pw8Cc9xbcLyQxRzA5upFRDlFYH4odVKkwHij2bQPvoFKNNi2Ix125Z83t.jpg",
        "price": 11300000,
        "category_id": 3
    },
    {
        "name": "Macbook Air M2 13 8/256GB",
        "description": "Mahsulot haqida qisqacha:\nПроцессор ядролари сони: 8 ядро\nРанги: Space Gray\nУмумий сақлаш хажми: 256GB SSD\nОператив хотира: 8 ГБ",
        "image_url": "https://olcha.uz/image/700x700/products/2022-08-26/macbook-air-m2-13-2022-space-gray-1000-gb-ssd-16-gb-102153-0.jpeg",
        "price": 15600000,
        "category_id": 3
    },
    {
        "name": "Macbook Air M2 13 8/256пи",
        "description": "Mahsulot haqida qisqacha:\nПроцессор ядролари сони: 8 ядро\nДисплей диагонали: 13.3\nДисплей кенглиги: 2560x1600\nУмумий сақлаш хажми: 256GB SSD\nОператив хотира: 8 ГБ",
        "image_url": "https://olcha.uz/image/700x700/products/2022-08-15/noutbuk-apple-macbook-pro-13-m2-8256gb-99035-0.jpeg",
        "price": 16900000,
        "category_id": 3
    }
]


def add_product(name, description, image_url, price, category_id):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                    password=config.DB_PASS,
                                    host=config.DB_HOST,
                                    port="5432",
                                    database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Products (name, description, image_url, price, category_id) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (name, description, image_url, price, category_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Products table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Products table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def add_products_to_db():
    for product in products:
        add_product(name=product.get("name"), description=product.get("description"), image_url=product.get("image_url"), price=product.get("price"), category_id=product.get("category_id"))
