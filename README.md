
<h3 align="center">ChatGPT + Whisper API Voice Discord Bot</h3>

  <p align="center">
    The Discord bot is designed to interact with users in a voice channel. Upon joining a voice channel, the bot is capable of listening to users' spoken words and processing them as text. The bot utilizes voice recognition software to transcribe the speech into text, and then passes the text to ChatGPT for generating a response.
    <br />
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

### Built With

* [Python](https://www.python.org/) - A high-level programming language for general-purpose programming.
* [ChatGPT API](https://openai.com/blog/chat-with-gpt-3/) - A powerful natural language processing API created by OpenAI.
* [Python Whisper API](https://whisper-python.readthedocs.io/en/latest/) - A Python library for working with the Discord API.

### Built By
* [Ghaith](https://www.linkedin.com/in/ghaith-khoja/) & [Zuair](https://www.linkedin.com/in/azuair/) & [Hamdan](https://www.linkedin.com/in/mhalhamdan/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Get a Discord Bot Token [Discord Bot Token Guide](https://www.writebots.com/discord-bot-token/)
2. Get an OpenAI API Key at [OpenAI API](https://platform.openai.com/account/api-keys)
3. Get a Whisper API key at [Whisper API](https://whisperapi.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/moo-gn/VoiceBot.git
   ```
2. Enter your API keys in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- ROADMAP -->
## Roadmap

- [ ] Call the bot to hear input using Discord Buttons instead of text input.
- [ ] Convert the ChatGPT text response back to speech using text-to-speech synthesis and deliver it to the voice channel.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Ghaith Khoja - gkhoja@umich.edu

Project Link: https://github.com/moo-gn/VoiceBot.git

