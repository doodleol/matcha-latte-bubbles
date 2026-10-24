 MATCHA LATTE BUBBLES  (Krita 5.2.x)

1) Plugin
   Krita > Tools > Scripts > Import Python Plugin from File... > pick matcha_bubbles.zip
   (older menu: Settings > Manage Resources > Import Python Plugin)
   Then Settings > Configure Krita > Python Plugin Manager > tick "Matcha Latte Bubbles"
   Restart Krita.

2) Color scheme (optional, makes the base palette match)
   Settings > Manage Resources > Open Resource Folder
   Make a folder called "color-schemes" if it isn't there, drop MatchaLatteBubbles.colors in it.
   Restart Krita, then Settings > Themes > pick "Matcha Latte Bubbles".

Tweak it: edit matcha_bubbles/style.qss, then Tools > Scripts > Matcha Bubbles: Reload Style.
Turn off for the session: Tools > Scripts > Matcha Bubbles: Turn Off.
Remove for good: untick it in the Python Plugin Manager.

Font: Handlee (SIL Open Font License) is bundled in matcha_bubbles/fonts and loads automatically, no install needed.
Bolder text: matcha_bubbles/fonts/MatchaHand-Regular.ttf is Handlee made slightly bolder.
