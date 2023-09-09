In order to use macros. 
Need to add buttons in buttons.json in /src following the example:
```
{
   "buttons": [
     {
       "name": "key1",
       "gpo": "GP16"
     },
     {
       "name": "key2",
       "gpo": "GP15"
     },
     {
       "name": "key3",
       "gpo": "GP14"
     }
   ]
}
```

Then in the folder command_json/ create 
or change the macro settings for the buttons following the example
```
{
   "name": "macro1",
   "command": {
     "key1": ["COMMAND", "TAB"],
     "key2": ["COMMAND", "SPACE"],
     "key3": ["CONTROL", "SPACE", "LEFT_ARROW"]
   }
}
```
In the last_macro.json file, specify the default macros to run
```
{
   "macros": "macro1.json"
}
```

**Available key**

```
F23

F24

KEYPAD_FIVE

KEYPAD_NUMLOCK

FOUR

SEVEN

KEYPAD_ENTER

BACKSLASH

RETURN

CAPS_LOCK

KEYPAD_THREE

TAB

WINDOWS

KEYPAD_NINE

RIGHT_SHIFT

KEYPAD_PERIOD

LEFT_ARROW

KEYPAD_ZERO

RIGHT_GUI

DELETE

ESCAPE

POUND

OPTION

ZERO

GUI

NINE

COMMAND

THREE

MINUS

END

INSERT

KEYPAD_SEVEN

KEYPAD_ASTERISK

FIVE

KEYPAD_FORWARD_SLASH

PAGE_DOWN

KEYPAD_FOUR

E

KEYPAD_SIX

CONTROL

D

G

SHIFT

F

A

M

SPACE

KEYPAD_PLUS

N

C

B

COMMA

L

TWO

T

W

V

Q

P

S

PAUSE

R

RIGHT_BRACKET

SEMICOLON

DOWN_ARROW

Y

X

KEYPAD_BACKSLASH

Z

__module__

POWER

ENTER

PAGE_UP

SPACEBAR

LEFT_ALT

KEYPAD_MINUS

SCROLL_LOCK

LEFT_SHIFT

PERIOD

O

LEFT_BRACKET

I

LEFT_CONTROL

PRINT_SCREEN

H

K

HOME

__qualname__

J

U

RIGHT_CONTROL

KEYPAD_EIGHT

F3

F2

F1

RIGHT_ALT

KEYPAD_TWO

F7

F6

F5

F4

modifier_bit

F9

F8

ALT

APPLICATION

F12

F13

F10

F11

RIGHT_ARROW

F16

F14

SIX

KEYPAD_EQUALS

F15

BACKSPACE

F17

F18

F19

EIGHT

EQUALS

LEFT_GUI

KEYPAD_ONE

QUOTE

F21

ONE

F20

GRAVE_ACCENT

FORWARD_SLASH

F22

UP_ARROW
```
