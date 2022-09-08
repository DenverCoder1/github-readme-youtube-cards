<p align="center">
  <img src="https://user-images.githubusercontent.com/20955511/189236319-b20eb901-aec0-4d6b-9b4a-944bd2c322d7.png" width="100px"/>
  <h3 align="center">GitHub Readme YouTube Cards</h3>
</p>

<p align="center">
  Workflow for displaying recent YouTube videos as SVG cards in your readme
</p>

<p align="center">
  <a href="https://discord.gg/fPrdqh3Zfu" alt="Discord" title="Dev Pro Tips Discussion & Support Server">
    <img src="https://img.shields.io/discord/819650821314052106?color=7289DA&logo=discord&logoColor=white&style=for-the-badge"/></a>
</p>


## Basic Usage

1. Add the following snippet to your markdown file where you want the cards to appear.

```html
<!-- BEGIN YOUTUBE-CARDS -->
<!-- END YOUTUBE-CARDS -->
```

2. Create a file in your repo's `.github/workflows` folder and give it a name such as `youtube-cards.yml` with the following contents.

<!-- prettier-ignore-start -->
```yml
name: GitHub Readme YouTube Cards
on:
  schedule:
    # Runs every hour, on the hour
    - cron: "0 * * * *"
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: DenverCoder1/github-readme-youtube-cards@main
        with:
          channel_id: UCipSxT7a3rn81vGLw9lqRkg
          comment_tag_name: YOUTUBE-CARDS
```
<!-- prettier-ignore-end -->

Make sure to change the `channel_id` to your YouTube channel ID. See below for advanced configuration.

## Live Example

<!-- prettier-ignore-start -->
<!-- BEGIN EXAMPLE-YOUTUBE-CARDS -->
[![Automatically Deploy to Fly.io from GitHub with Actions](https://youtube-cards.onrender.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+from+GitHub+with+Actions&timestamp=1661864404&views=159&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Automatically Deploy to Fly.io from GitHub with Actions")](https://www.youtube.com/watch?v=6u9BrDaSHJc) [![Hosting a Python Discord Bot for Free with Fly.io](https://youtube-cards.onrender.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&timestamp=1661708747&views=479&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Hosting a Python Discord Bot for Free with Fly.io")](https://www.youtube.com/watch?v=J7Fm7MdZn_E) [![Making a Wordle Clone Discord Bot with Python (Nextcord)](https://youtube-cards.onrender.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&timestamp=1643900217&views=4088&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Making a Wordle Clone Discord Bot with Python (Nextcord)")](https://www.youtube.com/watch?v=0p_eQGKFY3I) [![Run Open Source Code in Seconds with GitPod](https://youtube-cards.onrender.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&timestamp=1642108413&views=3751&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Run Open Source Code in Seconds with GitPod")](https://www.youtube.com/watch?v=Mt_Bsj6K9Lw) [![Custom Help Commands [#2] Select Menus - Python Discord Bot](https://youtube-cards.onrender.com/?id=xsA5QAkr-04&title=Custom+Help+Commands+%5B%232%5D+Select+Menus+-+Python+Discord+Bot&timestamp=1633051808&views=10089&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Custom Help Commands [#2] Select Menus - Python Discord Bot")](https://www.youtube.com/watch?v=xsA5QAkr-04) [![Custom Help Commands [#1] Embeds - Python Discord Bot](https://youtube-cards.onrender.com/?id=TzR8At0SFQI&title=Custom+Help+Commands+%5B%231%5D+Embeds+-+Python+Discord+Bot&timestamp=1632947582&views=8492&width=250&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede "Custom Help Commands [#1] Embeds - Python Discord Bot")](https://www.youtube.com/watch?v=TzR8At0SFQI)
<!-- END EXAMPLE-YOUTUBE-CARDS -->
<!-- prettier-ignore-end -->

## Advanced Configuration

See [action.yml](https://github.com/DenverCoder1/github-readme-youtube-cards/blob/main/action.yml).

| Option             | Description                                       | Default                                                 |
| ------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| `channel_id`       | The channel ID to use for the feed                | Required                                                |
| `comment_tag_name` | The name in the comment tag for replacing content | "YOUTUBE-CARDS"                                         |
| `max_videos`       | The maximum number of videos to display           | 6                                                       |
| `base_url`         | The base URL to use for the cards                 | "https://youtube-cards.onrender.com/"                   |
| `card_width`       | The width of the SVG cards                        | 250                                                     |
| `background_color` | The background color of the SVG cards             | "#0d1117"                                               |
| `title_color`      | The color of the title text                       | "#ffffff"                                               |
| `stats_color`      | The color of the stats text                       | "#dedede"                                               |
| `author_name`      | The name of the commit author                     | "GitHub Actions"                                        |
| `author_email`     | The email address of the commit author            | "41898282+github-actions[bot]@users.noreply.github.com" |

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a way to improve this project.

Make sure your request is meaningful and you have tested the app locally before submitting a pull request.

### Installing dependencies

```bash
# Dependencies for running the Flask server
poetry install

# Dependencies for testing and development
poetry install --with dev

# Dependencies for running the action script
pip install feedparser
```

### Running the Flask server

```bash
gunicorn web.app:app
```

### Running the action Python part of the workflow locally

```bash
python action.py --channel_id=UCipSxT7a3rn81vGLw9lqRkg
```

### Running tests

```bash
tox
```

## 🙋‍♂️ Support

💙 If you like this project, give it a ⭐ and share it with friends!

<p align="left">
  <a href="https://www.youtube.com/channel/UCipSxT7a3rn81vGLw9lqRkg?sub_confirmation=1"><img alt="Youtube" title="Youtube" src="https://img.shields.io/badge/-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white"/></a>
  <a href="https://github.com/sponsors/DenverCoder1"><img alt="Sponsor with Github" title="Sponsor with Github" src="https://img.shields.io/badge/-Sponsor-ea4aaa?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

[☕ Buy me a coffee](https://ko-fi.com/jlawrence)
