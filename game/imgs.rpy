init offset = -2
transform char_one:
    xalign 0.29
    yalign 0.5
transform char_two:
    xalign 0.43
    yalign 0.5
transform char_three:
    xalign 0.57
    yalign 0.5
transform char_four:
    xalign 0.71
    yalign 0.5

image load_bg_mane = "gui/load/normal/001.png"
image load_bg_die = "gui/load/normal/002.png"
image load_bg_hesp = "gui/load/normal/003.png"
image load_bg_noct = "gui/load/normal/004.png"
image load_bg_dilu = "gui/load/normal/005.png"
image load_bg_sei = "gui/load/normal/006.png"
image load_bg_sam = "gui/load/normal/007.png"

image load_ell:
    "gui/load/normal/char1_1.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char1_1r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_ghilley:
    "gui/load/normal/char1_2.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char1_2r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_jamie:
    "gui/load/normal/char1_3.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char1_3r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_licht:
    "gui/load/normal/char1_4.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char1_4r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
########    Mane    ##########
##Ell
image ell_blink:
    "chars/ell/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/ell/002.png"
    pause 0.15
    repeat
layeredimage ell:
    always:
        "chars/ell/ell_base.png"
    group eyes:
        attribute eyes_to_player default:
            "ell_blink"
        #attribute eyes_to_side:
        #    "ell_sideblink"
        attribute eyes_closed_up:
            "chars/ell/003.png"
        attribute eyes_closed_down:
            "chars/ell/002.png"
        attribute wink:
            "chars/ell/004.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/ell/blank.png"
        #attribute eyebrows_down:
        #    "chars//.png"
    group mouth:
        attribute mouth_smile_line:
            "chars/ell/005.png"
        attribute mouth_smile_1 default:
            "chars/ell/blank.png"
        attribute mouth_smile_2:
            "chars/ell/006.png"
        #attribute mouth_serious:
        #    "chars//.png"
    group blush:
        attribute blush:
            "chars/ell/008.png"
##Jamie
image jamie_blink:
    "chars/jamie/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/jamie/002.png"
    pause 0.15
    "chars/jamie/003.png"
    pause 0.15
    repeat
image jamie_lowblink:
    "chars/jamie/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/jamie/003.png"
    pause 0.15
    repeat
layeredimage jamie:
    always:
        "chars/jamie/jamie_base.png"
    group eyes:
        attribute eyes_to_player default:
            "jamie_blink"
        attribute eyes_closed_up:
            "chars/jamie/004.png"
        attribute eyes_closed_down:
            "chars/jamie/003.png"
        attribute eyes_low:
            "jamie_lowblink"
        attribute wink:
            "chars/jamie/005.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/jamie/blank.png"
        #attribute eyebrows_down:
    group mouth:
        attribute mouth_smile_line:
            "chars/jamie/006.png"
        attribute mouth_smile_1 default:
            "chars/jamie/007.png"
        attribute mouth_teeth:
            "chars/jamie/008.png"
        attribute mouth_serious:
            "chars/jamie/009.png"
    group blush:
        attribute blush:
            "image/jamie/010.png"
##Ghilley
image ghilley_blink:
    "chars/ghilley/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/ghilley/003.png"
    pause 0.15
    repeat
image ghilley_sideblink:
    "chars/ghilley/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/ghilley/003.png"
    pause 0.15
    repeat
layeredimage ghilley:
    always:
        "chars/ghilley/ghilley_base.png"
    group eyes:
        attribute eyes_to_player default:
            "ghilley_blink"
        attribute eyes_to_side:
            "ghilley_sideblink"
        attribute eyes_closed_up:
            "chars/ghilley/004.png"
        attribute eyes_closed_down:
            "chars/ghilley/003.png"
        attribute wink:
            "chars/ghilley/005.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/ghilley/blank.png"
        attribute eyebrows_down:
            "chars/ghilley/006.png"
    group mouth:
        attribute mouth_smile_line default:
            "chars/ghilley/007.png"
        attribute mouth_smile_teeth:
            "chars/ghilley/008.png"
        attribute mouth_teeth:
            "chars/ghilley/009.png"
        attribute mouth_serious:
            "chars/ghilley/010.png"
    group blush:
        attribute blush:
            "chars/ghilley/011.png"
##Licht
image licht_blink:
    "chars/licht/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/licht/002.png"
    pause 0.15
    "chars/licht/003.png"
    pause 0.15
    repeat
image licht_lowblink:
    "chars/licht/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/licht/003.png"
    pause 0.15
    repeat
layeredimage licht:
    always:
        "chars/licht/licht_base.png"
    group eyes:
        attribute eyes_to_player default:
            "licht_blink"
        attribute eyes_closed_up:
            "chars/licht/004.png"
        attribute eyes_closed_down:
            "chars/licht/003.png"
        attribute eyes_low:
            "licht_lowblink"
        attribute wink:
            "chars/licht/005.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/licht/blank.png"
        attribute eyebrows_down:
            "chars/licht/006.png"
    group mouth:
        attribute mouth_smile_line_1:
            "chars/licht/007.png"
        attribute mouth_smile_line_2:
            "chars/licht/010.png"
        attribute mouth_smile_1 default:
            "chars/licht/008.png"
        attribute mouth_smile_2:
            "chars/licht/009.png"
        attribute mouth_teeth:
            "chars/licht/011.png"
    group blush:
        attribute blush:
            "chars/licht/012.png"

image load_theo:
    "gui/load/normal/char2_1.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char2_1r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_louis:
    "gui/load/normal/char2_2.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char2_2r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_ethan:
    "gui/load/normal/char2_3.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char2_3r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_june:
    "gui/load/normal/char2_4.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char2_4r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
########    Die    ##########
##Theo
image theo_blink:
    "chars/theo/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/theo/002.png"
    pause 0.15
    repeat
layeredimage theo:
    always:
        "chars/theo/theo_base.png"
    group eyes:
        attribute eyes_to_player default:
            "theo_blink"
        attribute eyes_closed_up:
            "chars/theo/003.png"
        attribute eyes_closed_down:
            "chars/theo/002.png"
        attribute wink:
            "chars/theo/004.png"
    group mouth:
        attribute mouth_smile_line default:
            "chars/theo/006.png"
        attribute mouth_smile_1:
            "chars/theo/007.png"
        attribute mouth_smile_2:
            "chars/theo/005.png"
        attribute mouth_serious:
            "chars/theo/008.png"
    group blush:
        attribute blush:
            "chars/theo/009.png"
##June
image june_blink:
    "chars/june/june001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/june/june002.png"
    pause 0.15
    repeat
layeredimage june:
    always:
        "chars/june/june_base.png"
    group eyes:
        attribute eyes_to_player default:
            "june_blink"
        attribute eyes_closed_up:
            "chars/june/003.png"
        attribute eyes_closed_down:
            "chars/june/002.png"
        attribute wink:
            "chars/june/004.png"
        attribute eyes_soft:
            "chars/june/005.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/june/blank.png"
        attribute eyebrows_soft:
            "chars/june/006.png"
    group mouth:
        attribute mouth_smile_line:
            "chars/june/007.png"
        attribute mouth_smile_1:
            "chars/june/008.png"
        attribute mouth_smile_2:
            "chars/june/009.png"
        attribute mouth_teeth_1:
            "chars/june/010.png"
        attribute mouth_teeth_2:
            "chars/june/011.png"
        #attribute mouth_serious:
    group blush:
        attribute blush:
            "chars/june/012.png"
##Ethan
image ethan_blink:
    "chars/ethan/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/ethan/003.png"
    pause 0.15
    "chars/ethan/002.png"
    pause 0.15
    repeat
image ethan_lowblink:
    "chars/ethan/003.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/ethan/002.png"
    pause 0.15
    repeat
layeredimage ethan:
    always:
        "chars/ethan/ethan_base.png"
    group eyes:
        attribute eyes_to_player default:
            "ethan_blink"
        #attribute eyes_closed_up:
        attribute eyes_closed_down:
            "chars/ethan/002.png"
        #attribute wink:
        attribute eyes_low:
            "ethan_lowblink"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/ethan/blank.png"
        attribute eyebrows_annoy:
            "chars/ethan/004.png"
    group mouth:
        attribute mouth_smile_line:
            "chars/ethan/005.png"
        attribute mouth_smile:
            "chars/ethan/006.png"
        attribute mouth_serious:
            "chars/ethan/007.png"
        attribute mouth_serious_1:
            "chars/ethan/008.png"
    group blush:
        attribute blush:
            "chars/ethan/009.png"
##Louis
image louis_blink:
    "chars/louis/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/louis/002.png"
    pause 0.15
    "chars/louis/003.png"
    pause 0.15
    repeat
image louis_lowblink:
    "chars/louis/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/louis/003.png"
    pause 0.15
    repeat
image louis_sideblink:
    "chars/louis/louis004.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/louis/louis003.png"
    pause 0.15
    repeat
layeredimage louis:
    always:
        "chars/louis/louis_base.png"
    group eyes:
        attribute eyes_to_player default:
            "louis_blink"
        attribute eyes_to_side:
            "louis_sideblink"
        attribute eyes_low:
            "louis_lowblink"
        attribute eyes_closed_up:
            "chars/louis/005.png"
        attribute eyes_closed_down:
            "chars/louis/003.png"
        attribute wink:
            "chars/louis/006.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/louis/blank.png"
        attribute eyebrows_down:
            "chars/louis/007.png"
    group mouth:
        attribute mouth_smile_line:
            "chars/louis/008.png"
        attribute mouth_smile_1 default:
            "chars/louis/009.png"
        attribute mouth_smile_2:
            "chars/louis/010.png"
        attribute mouth_serious:
            "chars/louis/011.png"
    group blush:
        attribute blush:
            "chars/louis/012.png"

image load_sian:
    "gui/load/normal/char3_1.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char3_1r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_cyrille:
    "gui/load/normal/char3_2.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char3_2r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_kati:
    "gui/load/normal/char3_3.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char3_3r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_noah:
    "gui/load/normal/char3_4.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char3_4r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
########    Hesperide    ##########
##Sian
image sian_blink:
    "chars/sian/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/sian/002.png"
    pause 0.15
    "chars/sian/003.png"
    pause 0.15
    repeat
image sian_lowblink:
    "chars/sian/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/sian/003.png"
    pause 0.15
    repeat
image sian_sideblink:
    "chars/sian/004.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/sian/003.png"
    pause 0.15
    repeat
layeredimage sian:
    always:
        "chars/sian/sian_base.png"
    group eyes:
        attribute eyes_to_player default:
            "sian_blink"
        attribute eyes_low:
            "sian_lowblink"
        attribute eyes_to_side:
            "sian_sideblink"
        #attribute eyes_closed_up:
        attribute eyes_closed_down:
            "chars/sian/003.png"
        #attribute wink:
    #group eyebrows:
        #attribute eyebrows_base default:
        #attribute eyebrows_down:
    group mouth:
        attribute mouth_smile_line default:
            "chars/sian/005.png"
        attribute mouth_smile_1:
            "chars/sian/006.png"
        attribute mouth_smile_2:
            "chars/sian/007.png"
        attribute mouth_murmur:
            "chars/sian/008.png"
        attribute mouth_serious:
            "chars/sian/009.png"
    group blush:
        attribute blush:
            "chars/sian/010.png"
##Cyrille
image cyrille_blink:
    "chars/cyrille/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/cyrille/002.png"
    pause 0.15
    "chars/cyrille/003.png"
    pause 0.15
    repeat
image cyrille_lowblink:
    "chars/cyrille/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/cyrille/003.png"
    pause 0.15
    repeat
layeredimage cyrille:
    always:
        "chars/cyrille/cyrille_base.png"
    group eyes:
        attribute eyes_to_player default:
            "cyrille_blink"
        attribute eyes_low:
            "cyrille_lowblink"
        #attribute eyes_closed_up:
        attribute eyes_closed_down:
            "chars/cyrille/003.png"
        attribute eyes_glasses:
            "chars/cyrille/004.png"
        #attribute wink:
    group eyebrows:
        attribute eyebrows_base default:
            "chars/cyrille/blank.png"
        attribute eyebrows_n:
            "chars/cyrille/005.png"
        attribute eyebrows_v:
            "chars/cyrille/006.png"
    group mouth:
        attribute mouth_smile_line:
            "chars/cyrille/007.png"
        attribute mouth_smile_1:
            "chars/cyrille/008.png"
        attribute mouth_smile_2:
            "chars/cyrille/009.png"
        attribute mouth_smile_3:
            "chars/cyrille/010.png"
        attribute mouth_o:
            "chars/cyrille/011.png"
        attribute mouth_serious:
            "chars/cyrille/012.png"
        attribute mouth_a:
            "chars/cyrille/013.png"
    group blush:
        attribute blush:
            "chars/cyrille/014.png"
##Kati
image kati_blink:
    "chars/kati/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/kati/003.png"
    pause 0.15
    repeat
image kati_lowblink:
    "chars/kati/002.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/kati/003.png"
    pause 0.15
    repeat
layeredimage kati:
    always:
        "chars/kati/kati_base.png"
    group eyebrows:
        attribute eyebrows_base default:
            "chars/kati/blank.png"
        attribute eyebrows_v:
            "chars/kati/006.png"
    group eyes:
        attribute eyes_to_player default:
            "kati_blink"
        attribute eyes_low:
            "kati_lowblink"
        attribute eyes_closed_up:
            "chars/kati/004.png"
        attribute eyes_closed_down:
            "chars/kati/003.png"
        attribute wink:
            "chars/kati/005.png"
    group mouth:
        attribute mouth_smile_v:
            "chars/kati/007.png"
        attribute mouth_smile_line:
            "chars/kati/008.png"
        attribute mouth_smile_t:
            "chars/kati/009.png"
        attribute mouth_smile_a:
            "chars/kati/010.png"
        attribute mouth_small_o:
            "chars/kati/011.png"
        attribute mouth_o:
            "chars/kati/012.png"
    group blush:
        attribute blush:
            "chars/kati/012.png"
##Noah
image noah_blink:
    "chars/noah/001.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/noah/003.png"
    pause 0.15
    "chars/noah/002.png"
    pause 0.15
    repeat
image noah_lowblink:
    "chars/noah/003.png"
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 2
    "chars/noah/002.png"
    pause 0.15
    repeat

image load_nine:
    "gui/load/normal/char4_1.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char4_1r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_kirr:
    "gui/load/normal/char4_2.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char4_2r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_day:
    "gui/load/normal/char4_3.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char4_3r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_aitachi:
    "gui/load/normal/char4_4.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char4_4r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat


image load_youssef:
    "gui/load/normal/char5_1.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char5_1r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_mori:
    "gui/load/normal/char5_2.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char5_2r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_quincy:
    "gui/load/normal/char5_3.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char5_3r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
image load_verine:
    "gui/load/normal/char5_4.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    "gui/load/normal/char5_4r.png"
    choice:
        pause 2
    choice:
        pause 1
    choice:
        pause 0.5
    repeat
