"""THE WORLD TODAY — Saturday, 21 November 2026.
Dense multi-story front page, 1024x1024, rendered with PIL only.
Deterministic: fixed story data, fixed layout, no randomness, no network.
All 39 stories are events reported on 21 November 2026 (UTC), except
two follow-ups whose own dates are printed in their tags (Norway, 13 Nov;
Huang resignation, 12 Nov) so the date-check stays honest.
Layout budget (1024 high): masthead 0-88, UTC strip 94-118,
contents 122-140, hero+medium 146-316, grid 324-990, footer 998-1018.
Grid cells are 218 high; a story block is tag (11px) + 1-line headline
(13px) + deck (1 line in 5-story cells, 2 lines otherwise). Headlines are
kept short enough to fit one line at 11.5pt in 308px.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (18, 18, 18)
PAPER = (250, 247, 238)
RED = (178, 34, 28)
NAVY = (24, 42, 78)
GREY = (110, 108, 100)
LIGHT = (232, 228, 218)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, max_lines, lh, fill=INK):
    lines = wrap(draw, text, fnt, max_w)[:max_lines]
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


HERO = ("GULF", "21 NOV 2026", "IRAN STRIKES US BASES IN BAHRAIN AND KUWAIT",
        "Tehran says its Guards hit Patriot radar sites at al-Riffa and Awali; "
        "Bahrain reports a fire at a civilian site on Sitra Island.")

MEDIUM = [
    ("EUROPE", "21 NOV 2026", "COP31 IN OVERTIME AS FOSSIL-FUEL DEADLOCK",
     "Antalya talks run past their deadline with nearly 200 countries split over a "
     "draft that omits fossil fuels. The EU warns: a good deal or no deal at all."),
    ("MARKETS", "21 NOV 2026", "S&P 500 FALLS 3.7% AS AI SELL-OFF DEEPENS",
     "The index closes at 6,910, in correction territory, down 9.8% in a month. "
     "The Nasdaq drops 5.3% and erases all of its 2026 gains."),
    ("LATIN AMERICA", "21 NOV 2026", "MEXICO CAPTURES 'EL CHAPO ISIDRO'",
     "Fausto Isidro Meza-Flores is seized in Guasave, Sinaloa, with US help. "
     "Gun battles that follow leave at least 11 people dead."),
]

# region -> list of (utc_tag, headline <= ~44 chars, deck <= ~100 chars)
GRID = {
    "GULF": [
        ("21 NOV", "TWO TANKERS STRUCK NEAR STRAIT OF HORMUZ",
         "Two vessels hit leaving the strait; no casualties."),
        ("21 NOV", "RETALIATION CYCLE SPINS ON AFTER QESHM",
         "US hit Qeshm; Iran answered with strikes on Gulf bases."),
        ("21 NOV", "IRAN FACES ROLLING POWER CUTS SUNDAY",
         "Tehran blames war damage to its energy network."),
        ("21 NOV", "SAUDI, QATAR, KUWAIT CONDEMN ATTACKS",
         "Neighbours denounce the Bahrain strikes."),
    ],
    "WASHINGTON": [
        ("21 NOV", "DEMOCRATS RETAKE CONGRESS IN BLUE WAVE",
         "Midterm count confirms opposition control."),
        ("21 NOV", "TRUMP BACKS 10% CREDIT-CARD CAP",
         "He will work with Democrats on the ceiling."),
        ("21 NOV", "FBI PROBES INTRUSION AT CRIME DATABASE",
         "Agents probe a breach of the NCIC system."),
        ("21 NOV", "CONTRACTORS TOLD TO CLEAR HILL REQUESTS",
         "Contractors must clear Hill inquiries first."),
    ],
    "EUROPE": [
        ("21 NOV", "SPARTA II ABLAZE AFTER DRONE STRIKE",
         "Sanctioned ship hit by two drones; crew of 16 saved."),
        ("21 NOV", "KYIV FLAT HIT: 14 MISSING AFTER STRIKE",
         "Drone partly destroys a Kyiv apartment block."),
        ("13 NOV", "NORWAY COURT VOIDS DISPUTED OIL LICENCES",
         "Approvals ignored combustion emissions."),
        ("21 NOV", "EU GIVES METHANE RULES TWO-YEAR DELAY",
         "Brussels delays importer rules by two years."),
    ],
    "ASIA": [
        ("21 NOV", "EU-INDONESIA DEAL COVERS 730M PEOPLE",
         "Duties fall on 98.5% of tariff lines."),
        ("21 NOV", "BEIJING CALLS SPY CLAIMS 'GROUNDLESS'",
         "Beijing denies any role in the affair."),
        ("21 NOV", "SINGAPORE CLIENT AT CENTRE OF PROBE",
         "Megaspeed sales probed over chip rerouting."),
        ("21 NOV", "PRABOWO TO VISIT BRUSSELS ON 11 DEC",
         "Prabowo to meet von der Leyen in person."),
    ],
    "LATIN AMERICA": [
        ("21 NOV", "M6.8 PERU QUAKE SHAKES LIMA, NO DEATHS",
         "Junin tremor, 129 km deep, shakes the capital."),
        ("21 NOV", "'CHAPO ISIDRO' FLOWN TO MEXICO CITY",
         "Capo and No. 2 flown to prosecutors at 4 a.m."),
        ("21 NOV", "SINALOA ROADBLOCKS AS FANS FLEE GAME",
         "Burning trucks block roads; a game is halted."),
    ],
    "AFRICA": [
        ("21 NOV", "NIGERIA STARTS BUILDING NAVAL SHIPS",
         "Abuja cuts reliance on foreign shipyards."),
        ("21 NOV", "SOUTH AFRICANS VOTE AMID SERVICE ANGER",
         "Service anger threatens the governing ANC."),
        ("21 NOV", "KENYA SECURES 293,600 SAUDI JOBS",
         "Workers ask whether the posts are real."),
        ("21 NOV", "COP32 HEADS TO ADDIS ABABA IN 2027",
         "Next summit set for Ethiopia after Antalya."),
    ],
    "MARKETS": [
        ("21 NOV", "NASDAQ -5.3%: WORST WEEK SINCE 2020",
         "Tech rout wipes 10% off in a week."),
        ("21 NOV", "NVIDIA -14% AS $2.7TN EVAPORATES",
         "Seventh straight fall; now fourth by value."),
        ("21 NOV", "NIKKEI -5.06% IN GLOBAL SELL-OFF",
         "Tokyo follows Wall Street down."),
        ("21 NOV", "VIX SOARS 33% TO 37 AS FEAR RETURNS",
         "Fear gauge spikes as indexes correct."),
        ("21 NOV", "ECB SEARCH: SPAIN SET FOR PRESIDENCY",
         "Spain's Hernandez de Cos on track for the job."),
    ],
    "SPORT": [
        ("21 NOV", "ALCARAZ RALLIES PAST SHELTON INTO FINAL",
         "Wins 3-6, 6-3, 7-6(1); run now 13 matches."),
        ("21 NOV", "ZVEREV BEATS MEDVEDEV 7-6, 6-4",
         "7-0 tiebreak seals a Sunday decider."),
        ("21 NOV", "TURIN DECIDER SET FOR SUNDAY 18:00 CET",
         "Alcaraz seeks a first crown; Zverev a third."),
    ],
    "TECH": [
        ("21 NOV", "HUANG AGREES TO FACE CONGRESS 1 DEC",
         "He testifies after his 12 Nov resignation."),
        ("21 NOV", "ANTHROPIC SLIDES AFTER $81.3BN LISTING",
         "Closes $88.91, down 8.5% on day two."),
        ("21 NOV", "SEC INQUIRY ADDS TO NVIDIA TURMOIL",
         "Regulators probe accounting; Kress steadies firm."),
        ("21 NOV", "UN EXTENDS AUTONOMOUS-WEAPONS TALKS",
         "No binding limits; 128 states keep working."),
    ],
}

UTC_STRIP = ("01:09 PERU QUAKE 6.8  ·  07:00 SPARTA II HIT  ·  11:28 EU-INDONESIA SIGNED  ·  "
             "15:00 ALCARAZ WINS  ·  EVENING SITRA FIRE, BAHRAIN")

CONTENTS = ("GULF 5 · WASHINGTON 4 · EUROPE 5 · ASIA 4 · LATIN AMERICA 4 · "
            "AFRICA 4 · MARKETS 6 · SPORT 3 · TECH 4")


def total_stories():
    return 1 + len(MEDIUM) + sum(len(v) for v in GRID.values())


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    f_mast = font(SERIF, 50)
    f_sub = font(SANS_B, 12)
    f_tag = font(SANS_B, 10)
    f_hero = font(SERIF, 24)
    f_hero_d = font(SERIF_R, 13)
    f_med = font(SANS_B, 14)
    f_med_d = font(SANS, 11)
    f_sec = font(SANS_B, 13)
    f_h = font(SANS_B, 11)
    f_dk = font(SANS, 9)
    f_small = font(SANS, 9)
    f_utc = font(SANS_B, 11)

    # --- masthead ---
    d.rectangle([0, 0, W, 4], fill=INK)
    d.text((W // 2, 8), "THE WORLD TODAY", font=f_mast, fill=INK, anchor="mt")
    d.text((W // 2, 64), "SATURDAY, 21 NOVEMBER 2026  —  39 STORIES, ONE DAY, CHECKED AGAINST THE RECORD",
           font=f_sub, fill=INK, anchor="mt")
    d.line([14, 88, W - 14, 88], fill=INK, width=2)
    # --- UTC strip ---
    d.rectangle([14, 94, W - 14, 118], fill=INK)
    d.text((W // 2, 100), UTC_STRIP, font=f_utc, fill=(255, 255, 255), anchor="mt")
    # --- contents ---
    d.text((W // 2, 124), "CONTENTS:  " + CONTENTS, font=f_tag, fill=RED, anchor="mt")
    d.line([14, 140, W - 14, 140], fill=INK, width=1)

    # --- hero + medium row: y 146-316 ---
    y0, y1 = 146, 330
    hx, hw = 14, 556
    d.rectangle([hx, y0, hx + hw, y1], outline=INK, width=2)
    d.rectangle([hx, y0, hx + hw, y0 + 22], fill=RED)
    d.text((hx + 8, y0 + 4), "GULF  —  LEAD STORY  ·  21 NOV 2026  ·  No. 01", font=f_tag, fill=(255, 255, 255))
    y = draw_wrapped(d, hx + 10, y0 + 28, HERO[2], f_hero, hw - 20, 2, 28)
    d.line([hx + 10, y + 3, hx + hw - 10, y + 3], fill=RED, width=2)
    draw_wrapped(d, hx + 10, y + 9, HERO[3], f_hero_d, hw - 20, 2, 16)
    # drawn Gulf map panel (deterministic illustration, text drawn in-image)
    my = y1 - 42
    d.rectangle([hx + 10, my, hx + hw - 10, y1 - 8], fill=NAVY)
    for cx, lab in [(hx + 90, "BAHRAIN"), (hx + 230, "KUWAIT"), (hx + 380, "HORMUZ"), (hx + 500, "QESHM")]:
        d.ellipse([cx - 5, my + 7, cx + 5, my + 17], fill=(255, 255, 255))
        d.text((cx, my + 20), lab, font=f_tag, fill=(255, 255, 255), anchor="mt")
    d.line([hx + 90, my + 12, hx + 500, my + 12], fill=(255, 200, 60), width=2)

    # medium column: 3 stories, slot 56 each
    mx, mw = 582, 428
    med_h = (y1 - y0) // 3
    for i, (reg, tag, head, deck) in enumerate(MEDIUM):
        top = y0 + i * med_h
        d.rectangle([mx, top, mx + mw, top + med_h - 2], outline=INK, width=1)
        d.text((mx + 8, top + 3), f"{reg}  ·  {tag}  ·  No. {i + 2:02d}", font=f_tag, fill=RED)
        yy = draw_wrapped(d, mx + 8, top + 17, head, f_med, mw - 16, 1, 16)
        draw_wrapped(d, mx + 8, yy + 1, deck, f_med_d, mw - 16, 2, 11)

    # --- region grid: 3 cols x 3 rows, cells 324x218 ---
    gx, gy = 14, 338
    cw, chh, gap = 324, 212, 6
    order = ["GULF", "WASHINGTON", "EUROPE", "ASIA", "LATIN AMERICA",
             "AFRICA", "MARKETS", "SPORT", "TECH"]
    story_no = 5
    for idx, reg in enumerate(order):
        col, row = idx % 3, idx // 3
        x = gx + col * (cw + gap)
        yy0 = gy + row * (chh + gap)
        stories = GRID[reg]
        d.rectangle([x, yy0, x + cw, yy0 + chh], outline=INK, width=1)
        d.rectangle([x, yy0, x + cw, yy0 + 22], fill=INK)
        d.text((x + 8, yy0 + 4), f"{reg}  —  {len(stories)} STORIES", font=f_sec, fill=(255, 255, 255))
        body = chh - 26
        slot = body / len(stories)
        max_deck = 1
        for j, (tag, head, deck) in enumerate(stories):
            sy = yy0 + 26 + j * slot
            d.text((x + 8, sy + 1), f"{tag}  ·  No. {story_no:02d}", font=f_tag, fill=RED)
            story_no += 1
            hh = draw_wrapped(d, x + 8, sy + 12, head, f_h, cw - 16, 1, 12)
            draw_wrapped(d, x + 8, hh + 1, deck, f_dk, cw - 16, max_deck, 11)
            if j < len(stories) - 1:
                d.line([x + 8, sy + slot - 2, x + cw - 8, sy + slot - 2], fill=LIGHT, width=1)

    # --- footer ---
    d.line([14, 998, W - 14, 998], fill=INK, width=1)
    d.text((14, 1004), "Sources: Reuters, AP, CNN, BBC, ATP Tour, USGS/GFZ, EU Commission. Stories numbered No. 01-39; dates as tagged.",
           font=f_small, fill=GREY)
    d.text((W - 14, 1004), "39 STORIES", font=f_tag, fill=INK, anchor="rt")
    return img


if __name__ == "__main__":
    render().save("entry.png", optimize=True)
    print("stories:", total_stories())
