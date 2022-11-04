name: "GitHub Readme YouTube Cards"
author: "Jonah Lawrence"
description: "Workflow for displaying recent YouTube videos as SVG cards in your readme"
branding:
  icon: "grid"
  color: "red"

inputs:
  channel_id:
    description: "The channel ID to use for the feed"
    required: true
  lang:
    description: "The language you want your cards description to use"
    required: false
    default: "en"
  comment_tag_name:
    description: "The name of the comment tag to use for the cards"
    required: false
    default: "YOUTUBE-CARDS"
  max_videos:
    description: "The maximum number of videos to display"
    required: false
    default: "6"
  base_url:
    description: "The base URL to use for the cards"
    required: false
    default: "https://ytcards.demolab.com/"
  youtube_api_key:
    description: "The YouTube API key to use for additional features such a the video duration"
    required: false
    default: ""
  card_width:
    description: "The width of the SVG cards"
    required: false
    default: "250"
  background_color:
    description: "The background color of the SVG cards"
    required: false
    default: "#0d1117"
  title_color:
    description: "The color of the title text"
    required: false
    default: "#ffffff"
  stats_color:
    description: "The color of the stats text"
    required: false
    default: "#dedede"
  theme_context_light:
    description: "JSON theme for light mode (keys: background_color, title_color, stats_color)."
    required: false
    default: "{}"
  theme_context_dark:
    description: "JSON theme for dark mode (keys: background_color, title_color, stats_color)"
    required: false
    default: "{}"
  show_duration:
    description: "Whether to show the video duration. Requires `youtube_api_key` to be set."
    required: false
    default: "false"
  author_name:
    description: "The name of the committer"
    required: false
    default: "GitHub Actions"
  author_email:
    description: "The email address of the committer"
    required: false
    default: "41898282+github-actions[bot]@users.noreply.github.com"
  commit_message:
    description: "The commit message to use for the commit"
    required: false
    default: "docs(readme): Update YouTube cards"
  readme_path:
    description: "The path to the readme file"
    required: false
    default: "README.md"
  output_only:
    description: "Whether to return the section markdown as output instead of writing to the file"
    required: false
    default: "false"
  output_type:
    description: "The type of output to be rendered by the action ('markdown' or 'html')"
    required: false
    default: "markdown"

outputs:
  markdown:
    description: "The section markdown as output"
    value: ${{ steps.generate-readme-update.outputs.markdown }}

runs:
  using: "composite"
  steps:
    - name: Checkout
      uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install Python dependencies
      shell: bash
      run: python -m pip install -r ${{ github.action_path }}/requirements-action.txt

    - name: Generate Readme Update
      id: "generate-readme-update"
      shell: bash
      run: |
        UPDATE=$(python ${{ github.action_path }}/action.py \
                --channel "${{ inputs.channel_id }}" \
                --lang "${{ inputs.lang }}" \
                --comment-tag-name "${{ inputs.comment_tag_name }}" \
                --max-videos ${{ inputs.max_videos }} \
                --base-url "${{ inputs.base_url }}" \
                --card-width ${{ inputs.card_width }} \
                --background-color "${{ inputs.background_color }}" \
                --title-color "${{ inputs.title_color }}" \
                --stats-color "${{ inputs.stats_color }}" \
                --youtube-api-key "${{ inputs.youtube_api_key }}" \
                --show-duration "${{ inputs.show_duration }}" \
                --theme-context-light '${{ inputs.theme_context_light }}' \
                --theme-context-dark '${{ inputs.theme_context_dark }}' \
                --readme-path "${{ inputs.readme_path }}" \
                --output-only "${{ inputs.output_only }}" \
                --output-type "${{ inputs.output_type }}" \
        ) || exit 1
        echo "::set-output name=markdown::$(echo $UPDATE)"

    - name: Commit changes
      uses: EndBug/add-and-commit@v9
      with:
        message: "${{ inputs.commit_message }}"
        author_name: "${{ inputs.author_name }}"
        author_email: "${{ inputs.author_email }}"
