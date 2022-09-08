# GitHub Readme YouTube Cards

Workflow for displaying recent YouTube videos as SVG cards in your readme

## Live Example

<!-- BEGIN YOUTUBE-CARDS -->
![Automatically Deploy to Fly.io from GitHub with Actions](https://youtube-cards.onrender.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+from+GitHub+with+Actions&timestamp=1661864404.0&views=155 "Automatically Deploy to Fly.io from GitHub with Actions") ![Hosting a Python Discord Bot for Free with Fly.io](https://youtube-cards.onrender.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&timestamp=1661708747.0&views=474 "Hosting a Python Discord Bot for Free with Fly.io") ![Making a Wordle Clone Discord Bot with Python (Nextcord)](https://youtube-cards.onrender.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&timestamp=1643900217.0&views=4086 "Making a Wordle Clone Discord Bot with Python (Nextcord)") ![Run Open Source Code in Seconds with GitPod](https://youtube-cards.onrender.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&timestamp=1642108413.0&views=3743 "Run Open Source Code in Seconds with GitPod") ![Custom Help Commands [#2] Select Menus - Python Discord Bot](https://youtube-cards.onrender.com/?id=xsA5QAkr-04&title=Custom+Help+Commands+%5B%232%5D+Select+Menus+-+Python+Discord+Bot&timestamp=1633051808.0&views=10083 "Custom Help Commands [#2] Select Menus - Python Discord Bot") ![Custom Help Commands [#1] Embeds - Python Discord Bot](https://youtube-cards.onrender.com/?id=TzR8At0SFQI&title=Custom+Help+Commands+%5B%231%5D+Embeds+-+Python+Discord+Bot&timestamp=1632947582.0&views=8491 "Custom Help Commands [#1] Embeds - Python Discord Bot")
<!-- END YOUTUBE-CARDS -->

## Contributing

Installing dependencies:

```bash
# Dependencies for running the Flask server
poetry install --with web

# Dependencies for running the action script
poetry install --with action

# Dependencies for development
poetry install --with dev
```

Running the Flask server

```bash
gunicorn web.app:app
```

Running tests

```bash
tox
```
