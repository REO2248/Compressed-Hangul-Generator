import random
import time
import pyperclip
c=['ᄢ', 'ᄣ', 'ᄤ', 'ᄥ', 'ᄦ', 'ꥧ', 'ꥪ', 'ꥲ', 'ꥵ', 'ꥸ']
v=['ᆀ', 'ᆁ', 'ᆅ', 'ᆊ', 'ᆋ', 'ᆌ', 'ᆐ', 'ᆑ', 'ᆒ', 'ᆗ', 'ᆧ', 'ힳ', 'ힶ', 'ힷ', 'ힽ', 'ힾ', 'ퟀ', 'ퟁ']
p=['ᇌ', 'ᇌ', 'ᇑ', 'ᇒ', 'ᇓ', 'ᇔ', 'ᇖ', 'ᇭ', 'ퟎ', 'ퟑ', 'ퟕ', 'ퟖ', 'ퟗ', 'ퟘ', 'ퟙ', 'ퟚ', 'ퟜ', 'ퟟ', 'ퟡ', 'ퟤ', 'ퟧ', 'ퟸ']
while True:
    r=random.choice(c)+random.choice(v)+random.choice(p)
    print(r)
    pyperclip.copy(r)
    time.sleep(0.01)
