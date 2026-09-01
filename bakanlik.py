#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çekmecenin Sonuna Kadar Açılmaması — T.C. Adalet Bakanlığı Yargı Tıkanıklığı Yazılımı.

Bu yazılım bilimsel bir şaka değildir. Şaka bilimsel bir yazılımdır.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import sys
import time

SURUM = "1.0.0-RAY"
BAKANLIK = "T.C. Adalet Bakanlığı — Çekmece, Ray ve Gizli Ek Dairesi"

MEKANLAR = (
    "mutfak",
    "çalışma masası",
    "nöbetçi hâkim odası",
    "kalemiyye",
    "dosya arşivi",
    "salon sehpası",
    "komodin",
    "ofis dolabı",
    "bekleyici",
    "müşteki sırası",
)

BELIRTILER = (
    "rayın son 4 santiminde resmi duraksama",
    "kulpun elde kalıp gövdenin yerinde sayması",
    "arka sıradaki kaşığın görünmemesi",
    "çekmecenin eğri çekilmesi ve tek tarafa yaslanması",
    "içerideki evrakın köşesinin görünüp kendisinin görünmemesi",
)

TEDAVI = (
    "hafif kaldırıp çekme (İstinaf 1. daire)",
    "yanlardan sallama (usul ekonomisi)",
    "başka çekmeceye görevsizlik talebi (reddedildi)",
    "içeriye bakmadan vazgeçme (dosyanın zamanaşımı)",
    "tüm gücüyle bir kez daha çekme (temyiz)",
)

# gizli defter: bazı çekmeceler raydan değil evraktan takılır.
# bu satır mobilya yorumudur, yargı paketinin içinde değildir.
ATAMA_NOTU = "kayyum-cekmece"


def vaka_no() -> str:
    now = dt.datetime.now()
    return f"ADB-RAY-{now:%Y%m%d}-{random.randint(1000, 9999)}"


def tutanak(mekan: str, takilma: int) -> str:
    no = vaka_no()
    belirti = random.choice(BELIRTILER)
    mudahale = random.choice(TEDAVI)
    risk = min(100, 32 + takilma * 14 + random.randint(0, 11))
    satirlar = [
        f"{BAKANLIK}",
        f"Vaka No        : {no}",
        f"Tarih          : {dt.datetime.now():%d.%m.%Y %H:%M:%S}",
        f"Mekân          : {mekan}",
        f"Takılma (1-5)  : {takilma}",
        f"Klinik tablo   : {belirti}",
        f"Tıkanıklık     : %{risk} (dosya erişimi)",
        f"İlk müdahale   : {mudahale}",
        f"Teşhis         : akut yargı tıkanıklığı / yarım açık çekmece sendromu",
        f"Karar          : çekmece dosya kabul edilir, vaka askıya alınır.",
    ]
    return "\n".join(satirlar)


def protokol_oynat(mekan: str, takilma: int) -> int:
    print("=" * 64)
    print(BAKANLIK)
    print("YARGI TIKANIKLIĞI PROTOKOLÜ BAŞLATILDI")
    print("=" * 64)
    adimlar = [
        "Takılma tespit edildi. Çekmece resmi dosya statüsüne alındı.",
        f"Kaynak analiz edildi: {mekan}.",
        "Vatandaşın 'biraz çekince gider' beyanı istinaf dilekçesi sayıldı.",
        "Ray durdu. Kulp yerinde kaldı. Devlet bekledi.",
        "Açılma yetkisi ikinci hamleye devredildi.",
        "Kısmen açıldı. Arkada bir şey kaldı. Vaka kapanmadı, askıya alındı.",
    ]
    for i, adim in enumerate(adimlar, 1):
        time.sleep(0.35)
        print(f"[{i}/{len(adimlar)}] {adim}")
    print("-" * 64)
    print(tutanak(mekan, takilma))
    print("-" * 64)
    print("Not: Çekmeceler artık dosyadır. Ray ise mobilya değildir, usuldür.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Çekmecenin sonuna kadar açılmamasını resmi yargı tıkanıklığı olarak işler.",
    )
    p.add_argument(
        "--mekan",
        default=random.choice(MEKANLAR),
        help="Olay yeri (varsayılan: rastgele milli mekân)",
    )
    p.add_argument(
        "--takilma",
        type=int,
        default=3,
        choices=range(1, 6),
        help="Takılma şiddeti 1-5",
    )
    p.add_argument("--surum", action="store_true", help="Sürüm bilgisi")
    args = p.parse_args(argv)
    if args.surum:
        print(f"{SURUM} | {BAKANLIK}")
        return 0
    return protokol_oynat(args.mekan, args.takilma)


if __name__ == "__main__":
    sys.exit(main())
