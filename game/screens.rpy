﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox2.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

################################################################################
## Main and Game Menu Screens
################################################################################
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

default current_bg = "gui/bgs/bg_room1_base.jpg"
default current_chr = "ell"
default current_chr_chibi = "gui/button/chrs_chibi/char1_1.png"
define overlay = "gui/overlay/confirm.png"
define task_note = "gui/task_note.png"

init python:
    def advance_line():
        global line_index, line
        if line_index + 1 < len(lines):
            line_index += 1
            line = lines[line_index]

style say_who_button:
    color "#ffffff"
    size 30
    xalign 0.06
    bold True

style say_dialogue_button:
    color "#110050"
    size 26
    xalign 0.3
    yalign 0.5
    #padding (80, 35, 100, 60)

style dialogue_button is default:
    background "gui/textbox.png"
    padding (12, 7)

screen main_menu():
    tag menu

    add current_bg
    add current_chr xpos 0.35 ypos 0.58 anchor (0.5, 0.5)
    
    frame:
        background None
        xsize 600
        ysize 220
        xalign 0.6
        yalign 0.75
        #padding (50, 40, 50, 40)
        button:
            action Function(advance_line)
            style "dialogue_button"
            vbox:
                spacing 5
                text "[speaker]" style "say_who_button"
                text "[line]" style "say_dialogue_button"

    frame:
        style "main_menu_frame"

    vbox: #vertical buttons
        spacing 30
        xalign 0.01
        yalign 0.4

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("treat_screen")

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("shop_screen")

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("dailies_screen")

    hbox: #horizontal buttons
        spacing 20
        xalign 0.01
        yalign 1.0

        imagebutton:
            idle current_chr_chibi
            action Show("chrs_screen")

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("bg_screen")

    hbox:
        spacing 20
        xalign 0.99
        yalign 1.0

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("search_screen")

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Show("all_tasks_screen")

        imagebutton:
            idle "gui/button/v_buttons.png"
            action Jump("create_task")

screen treat_screen():
    tag menu
    text "Treat Screen Placeholder" align (0.5, 0.5)
    vbox:
        align (0.9, 0.01)
        textbutton "go back" action Show("main_menu")

screen shop_screen():
    tag menu
    text "Shop Screen Placeholder" align (0.5, 0.5)
    vbox:
        align (0.9, 0.01)
        textbutton "go back" action Show("main_menu")

screen dailies_screen():
    tag menu
    text "Dailies Screen Placeholder" align (0.5, 0.5)
    vbox:
        align (0.9, 0.01)
        textbutton "go back" action Show("main_menu")

init python:
    def change_ell():
        speaker = "Ell"
        current_chr = "ell"
        current_chr_chibi = "gui/button/chrs_chibi/char1_1.png"

screen chrs_screen():
    tag menu
    #hbox: #horizontal buttons
    #    spacing 20
    #    xalign 0.01
    #    yalign 1.0

    #    imagebutton:
    #        idle "gui/button/chrs_chibi/char1_1.png"
    #        action Function(change_ell)

    vbox:
        align (0.9, 0.01)
        textbutton "X" action Show("main_menu")

screen bg_screen():
    tag menu
    text "Background Assets Screen Placeholder" align (0.5, 0.5)
    vbox:
        align (0.9, 0.01)
        textbutton "go back" action Show("main_menu")

screen search_screen():
    tag menu
    text "Search Screen Placeholder" align (0.5, 0.5)
    vbox:
        align (0.9, 0.01)
        textbutton "go back" action Show("main_menu")

screen all_tasks_screen():
    add task_note xpos 0.8 ypos 0.5 anchor (0.5, 0.5)
    vbox:
        align (0.98, 0.12)
        textbutton "X" action Hide("all_tasks_screen")
    vbox:
        xpos 0.66
        ypos 0.17
        text "Your Tasks" style "task_info_title"
        #if not tasks:
        #    text "You have no tasks yet." color "#bbbbbb"
        #else:
    vbox:
        xpos 0.66
        ypos 0.25
        spacing 32
        for t in persistent.tasks:
            vbox:
                hbox:
                    spacing 10
                    text "Title: [t.title]" style "task_info_sum"
                    text "Priority: [t.priority]" style "task_info_sum"
                hbox:
                    spacing 10
                    text "Due: [t.due_date]" style "task_info_sum"
                    text "Status: [t.status]" style "task_info_sum"

default title = ""
default description = ""
default priority = ""
default due_date = ""

style task_info_title:
    size 50
    bold True
    color "#005b82"

style task_info_note:
    size 35
    color "#3f89a9"

style task_info_sum:
    size 30
    color "#3f89a9"

screen create_task_screen():
    tag menu
    add current_bg
    add overlay
    add current_chr xpos 0.2 ypos 0.58 anchor (0.5, 0.5)
    add task_note xpos 0.7 ypos 0.5 anchor (0.5, 0.5)
    vbox:
        align (0.88, 0.12)
        textbutton "X" action Start()

    vbox:
        xpos 0.6
        ypos 0.17
        spacing 50
        text "New task!" style "task_info_title"
        text "Title: [title]" style "task_info_note"
    vbox:
        xpos 0.6
        ypos 0.37
        text "Description: [description]" style "task_info_note"
    vbox:
        xpos 0.6
        ypos 0.57
        spacing 65
        text "Priority: [priority]" style "task_info_note"
        text "Due Date: [due_date]" style "task_info_note"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

#        for h in _history_list:
#
#            window:
#
#                ## This lays things out properly if history_height is None.
#                has fixed:
#                    yfit True

#                if h.who:

#                    label h.who:
#                        style "history_name"
#                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
#                        if "color" in h.who_args:
#                            text_color h.who_args["color"]

#                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                text what:
#                    substitute False

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add overlay

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## GUI screens ############################################################
## Made by me (years ago) :P
## Mockery of the screens from the original game
default persistent.prolog = False

transform floating:
    linear 4.0 xoffset -28 yoffset +20
    linear 0.2 xoffset -32 yoffset +15
    linear 2.0 xoffset -28 yoffset +0
    linear 0.2 xoffset -32 yoffset -3
    linear 0.4 xoffset -5 yoffset +9
    linear 0.6 xoffset 28 yoffset +15
    linear 0.2 xoffset 32 yoffset +10
    linear 0.8 xoffset 25 yoffset +0
    repeat

label loadingscreen:
label splashscreen:
    $ import random
    $ result = random.randint(1, 5)
    if result == 1:
        call load_mane
    elif result == 2:
        call load_die
    elif result == 3:
        call load_hesperide
    elif result == 4:
        call load_noctu
    else:
        call load_diluculo
    return

label load_mane:
    show load_bg_mane with dissolve
    show load_ell at char_one
    show load_licht at char_two
    show load_jamie at char_three
    show load_ghilley at char_four
    pause 10
    hide load_ell
    hide load_licht
    hide load_jamie
    hide load_ghilley
    hide load_bg_mane with dissolve
    return

label load_die:
    show load_bg_die with dissolve
    show load_theo at char_one
    show load_louis at char_two
    show load_ethan at char_three
    show load_june at char_four
    pause 10
    hide load_theo
    hide load_louis
    hide load_ethan
    hide load_june
    hide load_bg_die with dissolve
    return

label load_hesperide:
    show load_bg_hesp with dissolve
    show load_sian at char_one
    show load_cyrille at char_two
    show load_kati at char_three
    show load_noah at char_four
    pause 10
    hide load_sian
    hide load_cyrille
    hide load_kati
    hide load_noah
    hide load_bg_hesp with dissolve
    return

label load_noctu:
    show load_bg_noct with dissolve
    show load_nine at char_one
    show load_kirr at char_two
    show load_day at char_three
    show load_aitachi at char_four
    pause 10
    hide load_nine
    hide load_kirr
    hide load_day
    hide load_aitachi
    hide load_bg_noct with dissolve
    return

label load_diluculo:
    show load_bg_dilu with dissolve
    show load_youssef at char_one
    show load_mori at char_two
    show load_quincy at char_three
    show load_verine at char_four
    pause 10
    hide load_youssef
    hide load_mori
    hide load_quincy
    hide load_verine
    hide load_bg_dilu with dissolve
    return