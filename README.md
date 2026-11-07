# mr1charles tweaks (Sileo / Zebra / Cydia repo)

**Repo URL:** `https://mr1charles.github.io/island26-repo/`

Add it in your package manager (Sileo: Sources → + , Zebra: Sources → + , Cydia: Sources → Edit → Add), then install the packages below.

## Island26 (beta)
An iOS 26 look for older iPhones:
- Dynamic Island pill with a battery card and charging pop-up
- Now-playing live activity (album art, equaliser, controls) from any music app
- Liquid-glass Control Center tiles
- Floating dock without the plate
- Home-screen long-press menu with a Customize sheet (Default / Dark / Clear / Tinted icon styles)
- Falling snow overlay
- Settings → About shows "27.0" (cosmetic, Settings only)

**Tested on:** iPhone 6, iOS 12.5.8, Amethyst jailbreak. Other devices and versions are untested. The pill is drawn over a screen with no notch.
**Not done yet:** timer/call live activities, a preferences pane, home-screen widget tiles.

Settings are read from `/var/mobile/Library/Preferences/com.mr1charles.island26.plist`. Defaults: island, snow, cc, dock, menu, aboutSpoof on; `neverlock` (disable auto-lock), `bubble` (turn on AssistiveTouch) and `dev` (developer command channel) off. Set a key to `false`/`true`, then respring.

If SpringBoard ever goes into safe mode, remove the package over SSH (`dpkg -r com.mr1charles.island26`) and respring.

## Spotify Lite
A full-screen app around open.spotify.com. On iOS 12 Safari Spotify's web player restricts full-song playback, so expect browsing and limited playback. Not affiliated with Spotify.

## GlassLock
Lock screen tweak: giant condensed outline clock, glass battery / alarm / weather widgets, glass torch and camera buttons, an unlock clock morph and an LCD always-on display (dimmed backlight, 10 minute limit off the charger, off below 20% battery). Tested on iPhone 6, iOS 12.5.8. It records SpringBoard crashes to `/var/mobile/Library/Logs/GlassLock-crashes.log`. Set `dev` to `true` in `com.mr1charles.glasslock.plist` only if you want the developer command channel.

## SmartSiri
Hold the Home button for an AI assistant that answers questions and controls the phone, using Groq (`gpt-oss-120b`, `whisper-large-v3-turbo`). **You must supply your own Groq API key**: put it under `apiKey` in `/var/mobile/Library/Preferences/com.mr1charles.smartsiri.plist`. Without a key the Home button behaves normally. Listening uses the microphone; your questions go to Groq.

## Web Lite (YT Lite and TT Lite)
Full-screen apps around the video sites' mobile websites. YT Lite loads m.youtube.com. TT Lite needs a helper program running on a computer, so it does not work on its own yet.

## Updating the repo
Drop new `.deb` files in `debs/`, run `python3 build.py`, commit, push.
