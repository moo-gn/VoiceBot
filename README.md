
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

* [Python](https://www.python.org/)
* [ChatGPT API](https://openai.com/blog/chat-with-gpt-3/)
* [Python Whisper API](https://whisper-python.readthedocs.io/en/latest/)

### Built By
* [Ghaith](https://www.linkedin.com/in/ghaith-khoja/) & [Zuair](https://www.linkedin.com/in/azuair/) & [Hamdan](https://www.linkedin.com/in/mhalhamdan/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Get a Discord Bot Token [Discord Bot Token Guide](https://www.writebots.com/discord-bot-token/)
2. Get an OpenAI API Key at [OpenAI API](https://platform.openai.com/account/api-keys)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/moo-gn/VoiceBot.git
   ```
2. Install requirements using Pip
    ```sh
    pip install -r requirements.txt
    ```
3. Enter your API keys in `credentials.py`
   ```python
   DISCORD_BOT_TOKEN = "ENTER DISCORD TOKEN HERE"
   OPENAI_API_TOKEN = "ENTER OPENAPI KEY HERE"
   ```
4. Run the main driver
    ```sh
    python3 voice_bot.py
    ```

<!-- USAGE EXAMPLES -->
## Usage

1. Command the bot to join the voice channel using 
    ```sh
    /join
    ```
2. Click the 🔴 button to start recording your prompt
3. Click the ⬜ button to stop recording
4. Find your response in the text channel you asked the bot to join from 
5. Command the bot to leave the voice channel using
    ```sh
    /leave
    ```
 <br/>
 Here is an example where I asked the the voice bot for a pasta recipe!
    <img width="897" alt="Screenshot 2023-05-12 at 3 27 36 PM" src="https://github.com/moo-gn/VoiceBot/assets/13292277/30cb44cd-fc20-4c2b-ad3d-9ba6c0323131">


<!-- ROADMAP -->
## Roadmap

- [ ] Have the option to convert the ChatGPT text response back to speech using text-to-speech synthesis and play the response in the voice channel.
- [ ] Add voice commands.
- [ ] Make interface more user friendly. For example, remove record button and only stop recording when we are in the recording phase
- [ ] Improve the messages displayed to the user. Add the option to view the prompt recorded
- [ ] Make the user have the ability to change the join/leave commands to words of their choosing


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Ghaith Khoja - gkhoja@umich.edu

Project Link: https://github.com/moo-gn/VoiceBot.git

