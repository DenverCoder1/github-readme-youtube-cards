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

2. In your repo, create a `.github` folder and inside create a folder named `workflows` if it does not exist. Then create a file in your `.github/workflows/` folder and give it a name such as `youtube-cards.yml` with the following contents.

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
```
<!-- prettier-ignore-end -->

3. Make sure to change the `channel_id` to your YouTube channel ID.

4. The [cron expression](https://crontab.cronhub.io/) in the example above is set to run at the top of every hour. The first time, you may want to [trigger the workflow manually](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Running-the-GitHub-Action-Manually).

5. You're done! Star the repo and share it with friends! ⭐

See below for [advanced configuration](#advanced-configuration).

## Live Example

<!-- prettier-ignore-start -->
<!-- BEGIN EXAMPLE-YOUTUBE-CARDS -->
[![Automatically Deploy to Fly.io with GitHub Actions](https://ytcards.demolab.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+with+GitHub+Actions&lang=en&timestamp=1661864404&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=312 "Automatically Deploy to Fly.io with GitHub Actions")](https://www.youtube.com/watch?v=6u9BrDaSHJc#gh-dark-mode-only)[![Automatically Deploy to Fly.io with GitHub Actions](https://ytcards.demolab.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+with+GitHub+Actions&lang=en&timestamp=1661864404&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=312 "Automatically Deploy to Fly.io with GitHub Actions")](https://www.youtube.com/watch?v=6u9BrDaSHJc#gh-light-mode-only)
[![Hosting a Python Discord Bot for Free with Fly.io](https://ytcards.demolab.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&lang=en&timestamp=1661708747&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=403 "Hosting a Python Discord Bot for Free with Fly.io")](https://www.youtube.com/watch?v=J7Fm7MdZn_E#gh-dark-mode-only)[![Hosting a Python Discord Bot for Free with Fly.io](https://ytcards.demolab.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&lang=en&timestamp=1661708747&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=403 "Hosting a Python Discord Bot for Free with Fly.io")](https://www.youtube.com/watch?v=J7Fm7MdZn_E#gh-light-mode-only)
[![Making a Wordle Clone Discord Bot with Python (Nextcord)](https://ytcards.demolab.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&lang=en&timestamp=1643900217&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=2115 "Making a Wordle Clone Discord Bot with Python (Nextcord)")](https://www.youtube.com/watch?v=0p_eQGKFY3I#gh-dark-mode-only)[![Making a Wordle Clone Discord Bot with Python (Nextcord)](https://ytcards.demolab.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&lang=en&timestamp=1643900217&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=2115 "Making a Wordle Clone Discord Bot with Python (Nextcord)")](https://www.youtube.com/watch?v=0p_eQGKFY3I#gh-light-mode-only)
[![Run Open Source Code in Seconds with GitPod](https://ytcards.demolab.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&lang=en&timestamp=1642108413&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=578 "Run Open Source Code in Seconds with GitPod")](https://www.youtube.com/watch?v=Mt_Bsj6K9Lw#gh-dark-mode-only)[![Run Open Source Code in Seconds with GitPod](https://ytcards.demolab.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&lang=en&timestamp=1642108413&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=578 "Run Open Source Code in Seconds with GitPod")](https://www.youtube.com/watch?v=Mt_Bsj6K9Lw#gh-light-mode-only)
[![Custom Help Commands [#2] Select Menus - Python Discord Bot](https://ytcards.demolab.com/?id=xsA5QAkr-04&title=Custom+Help+Commands+%5B%232%5D+Select+Menus+-+Python+Discord+Bot&lang=en&timestamp=1633051808&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=1188 "Custom Help Commands [#2] Select Menus - Python Discord Bot")](https://www.youtube.com/watch?v=xsA5QAkr-04#gh-dark-mode-only)[![Custom Help Commands [#2] Select Menus - Python Discord Bot](https://ytcards.demolab.com/?id=xsA5QAkr-04&title=Custom+Help+Commands+%5B%232%5D+Select+Menus+-+Python+Discord+Bot&lang=en&timestamp=1633051808&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=1188 "Custom Help Commands [#2] Select Menus - Python Discord Bot")](https://www.youtube.com/watch?v=xsA5QAkr-04#gh-light-mode-only)
[![Custom Help Commands [#1] Embeds - Python Discord Bot](https://ytcards.demolab.com/?id=TzR8At0SFQI&title=Custom+Help+Commands+%5B%231%5D+Embeds+-+Python+Discord+Bot&lang=en&timestamp=1632947582&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=250&duration=1245 "Custom Help Commands [#1] Embeds - Python Discord Bot")](https://www.youtube.com/watch?v=TzR8At0SFQI#gh-dark-mode-only)[![Custom Help Commands [#1] Embeds - Python Discord Bot](https://ytcards.demolab.com/?id=TzR8At0SFQI&title=Custom+Help+Commands+%5B%231%5D+Embeds+-+Python+Discord+Bot&lang=en&timestamp=1632947582&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&width=250&duration=1245 "Custom Help Commands [#1] Embeds - Python Discord Bot")](https://www.youtube.com/watch?v=TzR8At0SFQI#gh-light-mode-only)
<!-- END EXAMPLE-YOUTUBE-CARDS -->
<!-- prettier-ignore-end -->

## Advanced Configuration

See [action.yml](https://github.com/DenverCoder1/github-readme-youtube-cards/blob/main/action.yml) for full details.

Check out the [Wiki](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki) for frequently asked questions.

### Inputs

| Option                | Description                                       | Default                                                 |
| --------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| `channel_id`          | The channel ID to use for the feed                | Required                                                |
| `lang`                | The language for cards description text           | "en"                                                    |
| `comment_tag_name`    | The name in the comment tag for replacing content | "YOUTUBE-CARDS"                                         |
| `youtube_api_key`     | The API key to use for features marked with 🔑    | ""                                                      |
| `max_videos`          | The maximum number of videos to display           | 6                                                       |
| `base_url`            | The base URL to use for the cards                 | "https://ytcards.demolab.com/"                          |
| `card_width`          | The width of the SVG cards                        | 250                                                     |
| `background_color`    | The background color of the SVG cards             | "#0d1117"                                               |
| `title_color`         | The color of the title text                       | "#ffffff"                                               |
| `stats_color`         | The color of the stats text                       | "#dedede"                                               |
| `theme_context_light` | JSON object with light mode colors <sup>🎨</sup>  | "{}"                                                    |
| `theme_context_dark`  | JSON object with dark mode colors <sup>🎨</sup>   | "{}"                                                    |
| `show_duration` 🔑    | Whether to show the duration of the videos        | "false"                                                 |
| `author_name`         | The name of the commit author                     | "GitHub Actions"                                        |
| `author_email`        | The email address of the commit author            | "41898282+github-actions[bot]@users.noreply.github.com" |
| `commit_message`      | The commit message to use for the commit          | "docs(readme): Update YouTube cards"                    |
| `readme_path`         | The path to the README file                       | "README.md"                                             |
| `output_only`         | Whether to skip writing to the readme file        | "false"                                                 |
| `output_type`         | The output syntax to be used by the action        | "markdown"                                              |

🔑 YouTube API Key required. See [Setting Up the Action with a YouTube API Key](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Setting-Up-the-Action-with-a-YouTube-API-Key) in the wiki for more information.

<sup>🎨</sup> See [Setting Theme Contexts for Light and Dark Mode](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Setting-Theme-Contexts-for-Light-and-Dark-Mode) in the wiki for more information.

[key]: https://user-images.githubusercontent.com/20955511/189419733-84384135-c5c4-4a20-a439-f832d5ad5f5d.png

### Outputs

| Output     | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| `markdown` | The generated markdown section used for updating the README file |

See [Using the Markdown as an Action Output](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Using-the-Markdown-as-an-Action-Output) for more information.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a way to improve this project.

Make sure your request is meaningful and you have tested the app locally before submitting a pull request.

Please check out our [contributing guidelines](/CONTRIBUTING.md) for more information on how to contribute to this project.

## 🙋‍♂️ Support

💙 If you like this project, give it a ⭐ and share it with friends!

<p align="left">
  <a href="https://www.youtube.com/channel/UCipSxT7a3rn81vGLw9lqRkg?sub_confirmation=1"><img alt="Youtube" title="Youtube" src="https://img.shields.io/badge/-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white"/></a>
  <a href="https://github.com/sponsors/DenverCoder1"><img alt="Sponsor with Github" title="Sponsor with Github" src="https://img.shields.io/badge/-Sponsor-ea4aaa?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

[☕ Buy me a coffee](https://ko-fi.com/jlawrence)
