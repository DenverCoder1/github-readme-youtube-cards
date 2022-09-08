# GitHub Readme YouTube Cards

Workflow for displaying recent YouTube videos as SVG cards in your readme

## Usage

1. Add the following snippet to your markdown file where you want the cards to appear.

```html
<!-- BEGIN YOUTUBE-CARDS -->

<!-- END YOUTUBE-CARDS -->
```

2. Create a file in your repo's `.github/workflows` folder and give it a name such as `youtube-cards.yml` with the following contents.

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

Make sure to change the channel_id to your YouTube channel ID. See below for advanced configuration.

## Live Example

<!-- BEGIN YOUTUBE-CARDS -->

<!-- END YOUTUBE-CARDS -->

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

Installing dependencies:

```bash
# Dependencies for running the Flask server
poetry install

# Dependencies for testing and development
poetry install --with dev

# Dependencies for running the action script
pip install feedparser
```

Running the Flask server

```bash
gunicorn web.app:app
```

Running the action Python script locally

```bash
python action.py --channel_id=UCipSxT7a3rn81vGLw9lqRkg
```

Running tests

```bash
tox
```
