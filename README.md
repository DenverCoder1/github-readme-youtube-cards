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
  build:
    runs-on: ubuntu-latest
    # Allow the job to commit to the repository
    permissions:
      contents: write
    # Run the GitHub Readme YouTube Cards action
    steps:
      - uses: DenverCoder1/github-readme-youtube-cards@main
        with:
          channel_id: UCipSxT7a3rn81vGLw9lqRkg
```
<!-- prettier-ignore-end -->

3. Make sure to change the `channel_id` to [your YouTube channel ID](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/How-to-Locate-Your-Channel-ID).

4. The [cron expression](https://crontab.cronhub.io/) in the example above is set to run at the top of every hour. The first time, you may want to [trigger the workflow manually](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Running-the-GitHub-Action-Manually).

5. You're done! Star the repo and share it with friends! ⭐

See below for [advanced configuration](#advanced-configuration).

## Live Example

<!-- prettier-ignore-start -->
<!-- BEGIN EXAMPLE-YOUTUBE-CARDS -->
<a href="https://www.youtube.com/watch?v=1lXaKEy97qE">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=1lXaKEy97qE&title=GitHub+Star+Swag+Unboxing+and+Giveaways&lang=en&timestamp=1696868769&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=172">
    <img src="https://ytcards.demolab.com/?id=1lXaKEy97qE&title=GitHub+Star+Swag+Unboxing+and+Giveaways&lang=en&timestamp=1696868769&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=172" alt="GitHub Star Swag Unboxing and Giveaways" title="GitHub Star Swag Unboxing and Giveaways">
  </picture>
</a>
<a href="https://www.youtube.com/watch?v=maoXtlb8t44">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=maoXtlb8t44&title=How+To+Self-Host+GitHub+Readme+Streak+Stats+on+Vercel&lang=en&timestamp=1693523015&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=257">
    <img src="https://ytcards.demolab.com/?id=maoXtlb8t44&title=How+To+Self-Host+GitHub+Readme+Streak+Stats+on+Vercel&lang=en&timestamp=1693523015&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=257" alt="How To Self-Host GitHub Readme Streak Stats on Vercel" title="How To Self-Host GitHub Readme Streak Stats on Vercel">
  </picture>
</a>
<a href="https://www.youtube.com/watch?v=6u9BrDaSHJc">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+with+GitHub+Actions&lang=en&timestamp=1661864404&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=312">
    <img src="https://ytcards.demolab.com/?id=6u9BrDaSHJc&title=Automatically+Deploy+to+Fly.io+with+GitHub+Actions&lang=en&timestamp=1661864404&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=312" alt="Automatically Deploy to Fly.io with GitHub Actions" title="Automatically Deploy to Fly.io with GitHub Actions">
  </picture>
</a>
<a href="https://www.youtube.com/watch?v=J7Fm7MdZn_E">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&lang=en&timestamp=1661708747&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=403">
    <img src="https://ytcards.demolab.com/?id=J7Fm7MdZn_E&title=Hosting+a+Python+Discord+Bot+for+Free+with+Fly.io&lang=en&timestamp=1661708747&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=403" alt="Hosting a Python Discord Bot for Free with Fly.io" title="Hosting a Python Discord Bot for Free with Fly.io">
  </picture>
</a>
<a href="https://www.youtube.com/watch?v=0p_eQGKFY3I">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&lang=en&timestamp=1643900217&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=2115">
    <img src="https://ytcards.demolab.com/?id=0p_eQGKFY3I&title=Making+a+Wordle+Clone+Discord+Bot+with+Python+%28Nextcord%29&lang=en&timestamp=1643900217&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=2115" alt="Making a Wordle Clone Discord Bot with Python (Nextcord)" title="Making a Wordle Clone Discord Bot with Python (Nextcord)">
  </picture>
</a>
<a href="https://www.youtube.com/watch?v=Mt_Bsj6K9Lw">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://ytcards.demolab.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&lang=en&timestamp=1642108413&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration=578">
    <img src="https://ytcards.demolab.com/?id=Mt_Bsj6K9Lw&title=Run+Open+Source+Code+in+Seconds+with+GitPod&lang=en&timestamp=1642108413&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration=578" alt="Run Open Source Code in Seconds with GitPod" title="Run Open Source Code in Seconds with GitPod">
  </picture>
</a>
<!-- END EXAMPLE-YOUTUBE-CARDS -->
<!-- prettier-ignore-end -->

## Advanced Configuration

See [action.yml](https://github.com/DenverCoder1/github-readme-youtube-cards/blob/main/action.yml) for full details.

Check out the [Wiki](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki) for frequently asked questions.

### Inputs

| Option                        | Description                                       | Default                                                 |
| ----------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| `channel_id`                  | The channel ID to use for the feed <sup>📺</sup>  | ""                                                      |
| `playlist_id`                 | The playlist ID to use for the feed <sup>📺</sup> | ""                                                      |
| `lang`                        | The locale for views and timestamps <sup>💬</sup> | "en"                                                    |
| `comment_tag_name`            | The text in the comment tag for replacing content | "YOUTUBE-CARDS"                                         |
| `youtube_api_key`             | The API key to use for features marked with 🔑    | ""                                                      |
| `max_videos`                  | The maximum number of videos to display           | 6                                                       |
| `base_url`                    | The base URL to use for the cards                 | "https://ytcards.demolab.com/"                          |
| `card_width`                  | The width of the SVG cards in pixels              | 250                                                     |
| `border_radius`               | The border radius of the SVG cards                | 5                                                       |
| `background_color`            | The background color of the SVG cards             | "#0d1117"                                               |
| `title_color`                 | The color of the title text                       | "#ffffff"                                               |
| `stats_color`                 | The color of the stats text                       | "#dedede"                                               |
| `theme_context_light`         | JSON object with light mode colors <sup>🎨</sup>  | "{}"                                                    |
| `theme_context_dark`          | JSON object with dark mode colors <sup>🎨</sup>   | "{}"                                                    |
| `max_title_lines`             | The maximum number of lines to use for the title  | 1                                                       |
| `show_duration` <sup>🔑</sup> | Whether to show the duration of the videos        | "false"                                                 |
| `author_name`                 | The name of the commit author                     | "GitHub Actions"                                        |
| `author_email`                | The email address of the commit author            | "41898282+github-actions[bot]@users.noreply.github.com" |
| `commit_message`              | The commit message to use for the commit          | "docs(readme): Update YouTube cards"                    |
| `readme_path`                 | The path to the Markdown or HTML file to update   | "README.md"                                             |
| `output_only`                 | Whether to skip writing to the readme file        | "false"                                                 |
| `output_type`                 | The output syntax to use ("markdown" or "html")   | "markdown"                                              |

<sup>📺</sup> A Channel ID or Playlist ID is required. See [How to Locate Your Channel ID](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/How-to-Locate-Your-Channel-ID) in the wiki for more information. To filter videos by type such as removing shorts or showing only popular videos, see [How to Filter Videos by Type](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/How-to-Filter-Videos-by-Type).

<sup>🔑</sup> Some features require a YouTube API key. See [Setting Up the Action with a YouTube API Key](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Setting-Up-the-Action-with-a-YouTube-API-Key) in the wiki for more information.

<sup>🎨</sup> See [Setting Theme Contexts for Light and Dark Mode](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Setting-Theme-Contexts-for-Light-and-Dark-Mode) in the wiki for more information.

<sup>💬</sup> See [this directory](https://github.com/DenverCoder1/github-readme-youtube-cards/tree/main/api/locale) for a list of locales with the word "views" translated. The timestamps will still be translated using [Babel](https://github.com/python-babel/babel) even if a translation file is not present. See [issue #48](https://github.com/DenverCoder1/github-readme-youtube-cards/issues/48) for info on contributing translations.

[key]: https://user-images.githubusercontent.com/20955511/189419733-84384135-c5c4-4a20-a439-f832d5ad5f5d.png

### Outputs

| Output            | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| `markdown`        | The generated Markdown or HTML used for updating the README file   |
| `committed`       | Whether the action has created a commit (`true` or `false`)        |
| `commit_long_sha` | The full SHA of the commit that has just been created              |
| `commit_sha`      | The short 7-character SHA of the commit that has just been created |
| `pushed`          | Whether the action has pushed to the remote (`true` or `false`)    |

See [Using the Markdown as an Action Output](https://github.com/DenverCoder1/github-readme-youtube-cards/wiki/Using-the-Markdown-as-an-Action-Output) for more information.

### Example Workflow

This is an advanced example showing the available options. All options are optional except `channel_id`.

```yaml
name: GitHub Readme YouTube Cards
on:
  schedule:
    # Runs every hour, on the hour
    - cron: "0 * * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    # Allow the job to commit to the repository
    permissions:
      contents: write
    # Run the GitHub Readme YouTube Cards action
    steps:
      - uses: DenverCoder1/github-readme-youtube-cards@main
        with:
          channel_id: UCipSxT7a3rn81vGLw9lqRkg
          lang: en
          comment_tag_name: YOUTUBE-CARDS
          youtube_api_key: ${{ secrets.YOUTUBE_API_KEY }} # Configured in Actions Secrets (see Wiki)
          max_videos: 6
          base_url: https://ytcards.demolab.com/
          card_width: 250
          border_radius: 5
          background_color: "#0d1117"
          title_color: "#ffffff"
          stats_color: "#dedede"
          theme_context_light: '{ "background_color": "#ffffff", "title_color": "#24292f", "stats_color": "#57606a" }'
          theme_context_dark: '{ "background_color": "#0d1117", "title_color": "#ffffff", "stats_color": "#dedede" }'
          max_title_lines: 2
          show_duration: true # Requires YouTube API Key (see Wiki)
          author_name: GitHub Actions
          author_email: 41898282+github-actions[bot]@users.noreply.github.com
          commit_message: "docs(readme): Update YouTube cards"
          readme_path: README.md
          output_only: false
          output_type: markdown
```

### Example Playlist Workflow

This is an example workflow for using a playlist instead of a channel.

```yaml
name: GitHub Readme YouTube Cards
on:
  schedule:
    # Runs every hour, on the hour
    - cron: "0 * * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    # Allow the job to commit to the repository
    permissions:
      contents: write
    # Run the GitHub Readme YouTube Cards action
    steps:
      - uses: DenverCoder1/github-readme-youtube-cards@main
        with:
          playlist_id: PL9YUC9AZJGFFAErr_ZdK2FV7sklMm2K0J
```

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
