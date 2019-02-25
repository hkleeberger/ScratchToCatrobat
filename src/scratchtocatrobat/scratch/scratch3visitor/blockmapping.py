import looks, motion, event, sensing, sound, operator, control, data, pen

visitormap = {
    "sensing_touchingobjectmenu" : sensing.visitTouchingObjectMenu,


    "event_whenflagclicked" : event.visitWhenflagclicked,
    "motion_movesteps" : motion.visitMovesteps,
    "motion_turnright" : motion.visitTurnright,
    "motion_turnleft" : motion.visitTurnleft,
    "motion_goto" : motion.visitGoto,
    "motion_gotoxy" : motion.visitGotoxy,
    "motion_glideto" : motion.visitGlideto,
    "motion_glidesecstoxy" : motion.visitGlidesecstoxy,
    "motion_pointindirection" : motion.visitPointindirection,
    "motion_pointtowards" : motion.visitPointtowards,
    "motion_changexby" : motion.visitChangexby,
    "motion_setx" : motion.visitSetx,
    "motion_changeyby" : motion.visitChangeyby,
    "motion_sety" : motion.visitSety,
    "motion_ifonedgebounce" : motion.visitIfonedgebounce,
    "motion_setrotationstyle" : motion.visitSetrotationstyle,
    "looks_sayforsecs" : looks.visitSayforsecs,
    "looks_say" : looks.visitSay,
    "looks_thinkforsecs" : looks.visitThinkforsecs,
    "looks_think" : looks.visitThink,
    "looks_switchcostumeto" : looks.visitSwitchcostumeto,
    "looks_nextcostume" : looks.visitNextcostume,
    "looks_switchbackdropto" : looks.visitSwitchbackdropto,
    "looks_nextbackdrop" : looks.visitNextbackdrop,
    "looks_changesizeby" : looks.visitChangesizeby,
    "looks_setsizeto" : looks.visitSetsizeto,
    "looks_changeeffectby" : looks.visitChangeeffectby,
    "looks_seteffectto" : looks.visitSeteffectto,
    "looks_cleargraphiceffects" : looks.visitCleargraphiceffects,
    "looks_show" : looks.visitShow,
    "looks_hide" : looks.visitHide,
    "looks_gotofrontback" : looks.visitGotofrontback,
    "looks_goforwardbackwardlayers" : looks.visitGoforwardbackwardlayers,

    "sound_play" : sound.visitPlay,
    "sound_playuntildone" : sound.visitPlayuntildone,
    "sound_stopallsounds" : sound.visitStopallsounds,
    "sound_changeeffectby" : sound.visitChangeeffectby,
    "sound_seteffectto" : sound.visitSeteffectto,
    "sound_cleareffects" : sound.visitCleareffects,
    "sound_changevolumeby" : sound.visitChangevolumeby,
    "sound_setvolumeto" : sound.visitSetvolumeto,
    "event_broadcast" : event.visitBroadcast,
    "event_broadcastandwait" : event.visitBroadcastandwait,
    "control_wait" : control.visitWait,
    "control_repeat" : control.visitRepeat,
    "control_if" : control.visitIf,
    "control_if_else" : control.visitIf_else,
    "control_wait_until" : control.visitWait_until,
    "control_repeat_until" : control.visitRepeat_until,
    "control_create_clone_of" : control.visitCreate_clone_of,
    "control_create_clone_of_menu" : control.visitCreate_clone_of_menu,
    "control_stop" : control.visitStop,

    "control_start_as_clone" : control.visitStart_as_clone,
    "control_forever" : control.visitForever,
    "control_delete_this_clone" : control.visitDelete_this_clone,

    "sensing_askandwait" : sensing.visitAskandwait,
    "sensing_setdragmode" : sensing.visitSetdragmode,
    "sensing_resettimer" : sensing.visitResettimer,
    "data_setvariableto" : data.visitSetvariableto,
    "data_changevariableby" : data.visitChangevariableby,
    "data_showvariable" : data.visitShowvariable,
    "data_hidevariable" : data.visitHidevariable,

    "sensing_distanceto" : sensing.visitDistanceto,
    "sensing_distancetomenu" : sensing.visitDistanceto_menu,
    "looks_costumenumbername" : looks.visitCostumenumbername,
    "sensing_loudness" : sensing.visitLoudness,
    "sensing_coloristouchingcolor" : sensing.visitColoristouchingcolor,
    "sensing_of" : sensing.visitOf,
    "sensing_current" : sensing.visitCurrent,
    "looks_size" : looks.visitSize,
    "motion_xposition" : motion.visitXposition,
    "sound_volume" : sound.visitVolume,
    "sensing_answer" : sensing.visitAnswer,
    "sensing_dayssince2000" : sensing.visitDayssince2000,
    "sensing_keypressed" : sensing.visitKeypressed,
    "sensing_keyoptions" : sensing.visitKey_options,
    "looks_backdropnumbername" : looks.visitBackdropnumbername,
    "sensing_mousex" : sensing.visitMousex,
    "sensing_mousedown" : sensing.visitMousedown,
    "sensing_mousey" : sensing.visitMousey,
    "motion_yposition" : motion.visitYposition,
    "sensing_timer" : sensing.visitTimer,
    "sensing_touchingcolor" : sensing.visitTouchingcolor,
    "motion_direction" : motion.visitDirection,
    "sensing_touchingobject" : sensing.visitTouchingObject,
    "sensing_currentmenu" : sensing.visitCurrent_menu,

    "event_whenbroadcastreceived" : event.visitWhenbroadcastreceived,
    "operator_subtract" : operator.visitSubtract,
    "operator_gt" : operator.visitGt,
    "operator_join" : operator.visitJoin,
    "operator_letter_of" : operator.visitLetter_of,
    "event_whenbackdropswitchesto" : event.visitWhenbackdropswitchesto,
    "operator_lt" : operator.visitLt,
    "operator_not" : operator.visitNot,
    "operator_mod" : operator.visitMod,
    "operator_add" : operator.visitAdd,
    "event_whengreaterthan" : event.visitWhengreaterthan,
    "operator_equals" : operator.visitEquals,
    "operator_mathop" : operator.visitMathop,
    "operator_and" : operator.visitAnd,
    "event_whenthisspriteclicked" : event.visitWhenthisspriteclicked,
    "operator_round" : operator.visitRound,
    "operator_multiply" : operator.visitMultiply,
    "operator_random" : operator.visitRandom,
    "operator_divide" : operator.visitDivide,
    "event_whenkeypressed" : event.visitWhenkeypressed,
    "operator_contains" : operator.visitContains,
    "operator_or" : operator.visitOr,
    "operator_length" : operator.visitLength,
    "sensing_username" : sensing.visitUsername,

    "sensing_of_object_menu" : sensing.visitOf_object_menu,
    "sound_sounds_menu" : sound.visitSounds_menu,
    "motion_goto_menu" : motion.visitGoto_menu,
    "motion_glideto_menu" : motion.visitGlideto_menu,
    "motion_pointtowards_menu" : motion.visitPointtowards_menu,

    "data_addtolist" : data.visitAddtolist,
    "data_deleteoflist" : data.visitDeleteoflist,
    "data_insertatlist" : data.visitInsertatlist,
    "data_replaceitemoflist" : data.visitReplaceitemoflist,
    "data_itemoflist" : data.visitItemoflist,
    "data_itemnumoflist" : data.visitItemnumoflist,
    "data_lengthoflist" : data.visitLengthoflist,
    "data_listcontainsitem" : data.visitListcontainsitem,
    "data_showlist" : data.visitShowlist,
    "data_hidelist" : data.visitHidelist,
    "data_contentsoflist" : data.visitContentsoflist,

    "looks_costume" : looks.visitCostume,
    "looks_backdrops" : looks.visitBackdrops,

    "procedures_call" : control.visitProcedures_call,
    "procedures_definition" : control.visitProcedures_definition,
    "argument_reporter_string_number" : control.visitArgumentIntOrString,
    "argument_reporter_boolean" : control.visitArgumentBool,
    "procedures_prototype" : control.visitProcedures_prototype,

    "pen_clear" : pen.visitClear,
    "pen_stamp" : pen.visitStamp,
    "pen_penDown" : pen.visitPenDown,
    "pen_penUp" : pen.visitPenUp,
    "pen_setPenColorToColor" : pen.visitSetPenColorToColor,
    "pen_changePenColorParamBy" : pen.visitChangePenColorParamBy,
    "pen_menu_colorParam" : pen.visitPen_menu_colorParam,
    "pen_setPenColorParamTo" : pen.visitSetPenColorParamTo,
    "pen_changePenSizeBy" : pen.visitChangePenSizeBy,
    "pen_setPenSizeTo" : pen.visitSetPenSizeTo,
    "pen_setPenShadeToNumber" : pen.visitSetPenShadeToNumber,
    "pen_changePenShadeBy" : pen.visitChangePenShadeByNumber,
    "pen_setPenHueToNumber" : pen.visitSetPenHueToNumber,


}