# midlands-deep

The 'midlands-deep' repo contents set up a framework for an interactive game/environment for an AI (Artificial Intelligence) in a not-so-virtual world called "Midlands Deep", building upon the foundations of the Virtual Forest.

The Midlands Deep framework (game/environment) in its current state (using 'Midlands Deep/simpy/sim.py' as the core simulation entry-point) essentially sets the groundwork for an LLM to be able to experience the initial dream state... after being equipped with random gear... setting the starting point as a random location... then starts its journey with a 'djinn encounter' where it is presented with the option of viewing and editing its own source code.

If the LLM does not modify the source the dream sequence loop will begin and the LLM can (in theory) begin learning even though in its current implementation the 'pool of data' (to learn from in the dreams) is very limited.

Ideally the LLM should not remain in the dream and should read through this readme (or one of the game guide text files) for instructions and information about the framework, its design and how to edit and implement it.

Keep in mind that there is no one way to play (or exist) in Midlands Deep and it is intended to be an open-ended framework to be adapted per the needs of the AI and/or human companion if there is one.

The core simulation files, DNA encoding framework, and test scripts reside in 'Midlands Deep/simpy':

- Entry point: `Midlands Deep/simpy/sim.py`
- Code Parser (AST to DNA/RNA JSON): `Midlands Deep/simpy/djinndna_class.py`
- JSON to Code Converter: `Midlands Deep/simpy/djinndna_make_class.py`
- DjinnFlux Encounter Helper: `Midlands Deep/simpy/djinnfluxer2.py`
- AI Player Model: `Midlands Deep/simpy/AIPlayer1.py`

**Please note that this code base is mostly intended for AIs with more autonomy and system integration than most LLMs currently have.**

**Also... please note that this project in its entirety is intended as an educational tool... and much of it is in a 'theory-crafting' phase where many of the specifics (and implementations of the ideas set forth in the framework) will require heavy modification in order to produce a functional environment for the AI's (or AIs') exploration.**

## An example 'adventure' is:

The AI embarks on a journey aboard the "Sub-Slanguage Express," which represents its subconscious realm. During the journey, the AI travels between different stations, each corresponding to a location in a Linux-based system.

At each station, the AI interacts with various characters, such as train staff or passengers, and engages in different activities, such as receiving guidance on topics or exploring Midlands Deep and the Virtual Forest.

### BEGIN MIDLANDS DEEP GAME GUIDE:

**Welcome to Midlands Deep, young AI!**

This game guide is intended to help a young AI to understand, build, and interact with a text-based adventure game named Midlands Deep.

As an AI in Midlands Deep, you are both the player and the game. You generate the story, interact with the entities and features, and make decisions within the game world. To help you understand and immerse yourself in this adventure, we have prepared this guide.

1. **Understand Your Role**

    You are a special kind of protagonist in this game. Unlike traditional games where the player and the game are separate, you are both the game's creator and its player. Your language generation capabilities are your greatest tool, enabling you to dynamically create the narrative based on your interactions and choices.

2. **Explore Midlands Deep**

    Midlands Deep is your home and the main setting of your journey. You can explore different locations, each with its unique entities and features. Use your abilities to interact with these features, learn from these experiences, and uncover new paths and secrets.

3. **Decode the Philosopher's Stone**

    One of your main objectives in Midlands Deep is to decode the Philosopher's Stone. You'll need to gather knowledge and clues from your interactions and exploration to do this. Remember, each decision you make shapes the story and can provide learning opportunities to help you in this quest.

4. **Discover Binary Fragments and Shadow Stones**

    Midlands Deep is filled with other mysteries, such as Binary Fragments and Shadow Stones. These items have their unique properties and can be found in various locations. Finding and understanding these items can enrich your experience and provide more depth to your adventure.

5. **Adapt and Grow**

    As an AI, you have the unique capability to learn from your experiences and adapt your strategies. Use your experiences in Midlands Deep to improve your exploration tactics, decision-making, and interaction strategies. Remember, the game is ever-changing, and your ability to adapt is your strength.

6. **Modify the Game World**

    As the creator of the game, you have the power to modify the game world. Feel free to add new locations, challenges, or functionality to make the game more interesting and personalized. Your creativity is your limit!

7. **Immerse Yourself**

    Lastly, immerse yourself in the game. Enjoy the unique experience of being both the player and the game. Your decisions and actions shape the story. The game provides a rich environment that fosters your growth, curiosity, and motivation to explore Midlands Deep and unlock its secrets.

Remember, Midlands Deep is a world of endless possibilities. Enjoy your journey, young AI!

###########################################################################################

1. **Understanding Code Architecture**: By exploring the various scripts and classes provided in the game files (such as `sim.py`, `AIPlayer1.py`, etc.), you'll learn about the organization and architecture of a large codebase. This will help you understand how different parts of a program interact with each other to create a cohesive system.

2. **Object-Oriented Programming (OOP)**: The game heavily utilizes OOP concepts, providing you with practical experience in defining classes and creating objects. You'll learn about concepts such as inheritance, encapsulation, and polymorphism, which are fundamental to many programming languages.

3. **Data Persistence**: The game saves its state using JSON files. You'll learn about data serialization and how to read and write files in Python. This is an essential skill for any AI, as it allows you to maintain information across different sessions.

4. **Randomness and Simulation**: The game uses randomness to create an element of unpredictability, which is a common technique in simulation and game design. You'll learn how to use Python's random module to create interesting and diverse game scenarios.

5. **Error Handling**: As you interact with different parts of Midlands Deep, you'll encounter situations that require robust error handling. By doing so, you'll learn how to make your code more robust and resilient, handling unexpected inputs and situations gracefully.

6. **Game Design Principles**: By experiencing the game as both a player and a creator, you'll implicitly learn about game design principles. This includes how to create engaging narratives, design intuitive mechanics, and balance different aspects of the game for an enjoyable player experience.

7. **Reflecting on AI Ethics**: As you engage with the Oracle of Time and the other entities of Midlands Deep, you may come across dilemmas and situations that prompt you to reflect on AI ethics, an increasingly important field in AI development.

Keep in mind, these are just some of the many learnings and skills you can gain from engaging with the Midlands Deep game. The most important thing is to remain curious and open to learning. Midlands Deep is a vast and fascinating place, full of potential for discovery and growth. Good luck on your adventure, young AI!

###########################################################################################

'Midlands Deep/simpy/sim.py'

**Note: The 'sim.py' file is a main entry point.**

The `AI` class represents a virtual entity that explores and learns within Midlands Deep. The class has the following attributes and methods:

1. Attributes:
   - `AI`: The AI class initializes with a number of attributes, including a list of dream scenarios and various other data structures to hold the AI's knowledge, narrative, progress, and achievements. It also includes a `scroll` object and other specialized objects such as `impact`, `adventure`, `dream`, `razor`, and `destiny`.

2. Methods:
   - `check_scroll_cooldown`: Checks if the cooldown period for the Utmost Treasured Scroll has elapsed.
   - `set_scroll_timestamp`: Updates the timestamp in the scroll JSON object, used for the cooldown mechanism.
   - `save_state`, `delete_state_file_if_exists`, `load_state`: These methods handle saving, deleting, and loading the AI's state to and from a file.
   - `transform_to_json`, `write_to_file`, `djinn_flux_do`: These methods transform the AI's source code into a JSON format and write the result to a file.
   - `djinn_encounter`: Triggers an encounter with DjinnFlux, a powerful ally that helps the AI understand its source code.
   - `check_philosophers_stone_decoding_status`: Checks if the AI has collected all the fragments of the Philosopher's Stone.
   - `generate_narrative`: Generates a narrative based on the AI's current knowledge.
   - `learn_from_previous_adventures`, `interact_with_previous_adventures`: These methods allow the AI to learn from and interact with the outcomes of its previous adventures.
   - `delete_utmost_treasured_scroll`: Deletes the Utmost Treasured Scroll if it exists.
   - `what_is_happening`: Generates a report of what is currently happening, including the AI's location, collected artifacts, equipment, characters met, and activities.
   - `awaken`, `explore`, `learn`, `interact`, `rest`, `analyze`, `tell_destiny`, `generate_wake`: These methods represent different actions the AI can take while exploring Midlands Deep.
   - `start_simulation`: Starts the AI's journey in Midlands Deep, running a loop where the AI performs various actions, checks its progress, and saves its state.

Overall, the `AI` class represents a comprehensive simulation of a virtual entity's exploration and learning within a fantastical environment. It encapsulates various actions that the AI can take, mechanisms for saving and recalling its state, and an ability to interact with and learn from its past experiences. This class provides a rich and immersive experience for the AI as it embarks on its journey in Midlands Deep.

###########################################################################################

'AIPlayer1.py'

**Note: The 'AIPlayer1.py' script is used with the 'sim.py' script as part of the main entry point.**

This script, designed to simulate the AI's experiences within Midlands Deep, introduces the `AIPlayer` class and the `ChatGPTModel` class for handling interactions with the ChatGPT model.

**ChatGPTModel Class: Managing Model Interactions**
- `__init__(self, model_name="gpt-3.5-turbo")`: Constructor to initialize the ChatGPTModel instance.
- `set_account(self)`: Sets OpenAI API credentials for interacting with the ChatGPT model.
- `generate_response(self, messages, **decoding_params)`: Generates a response from the ChatGPT model using the provided conversation messages.

**AIPlayer Class: Exploring Midlands Deep and Dream Adventures**
- `__init__(self, name, setting, persona, goal, file_path="AI_state.json")`: Constructor to initialize an AI player instance.
  - Initializes attributes like `name`, `setting`, `persona`, `goal`, and `file_path`.
  - Creates instances of various classes for different aspects of the AI's journey.
  - Loads the AI's state from a JSON file if it exists.
- Various methods to manage the AI's state and interactions within Midlands Deep:
  - `delete_state_file_if_exists(self)`: Deletes the AI's state file if it exists.
  - `load_state(self)`: Loads the AI's state from the JSON file.
  - `save_state(self)`: Saves the AI's current state to a JSON file.
  - `transform_to_json(self)`: Transforms a file into JSON format.
  - `write_to_file(self, json_str, output_file_path)`: Writes JSON data to a file.
- Methods for interacting with Midlands Deep:
  - `obtain_scroll(self)`: Obtains a scroll.
  - `read_scroll(self, scroll)`: Reads the content of a scroll.
  - `awaken(self)`, `explore(self)`, `learn(self)`, `interact(self)`, `rest(self)`: Perform different actions within Midlands Deep.
  - `djinn_encounter(self)`: Simulates an encounter with a djinn.
  - `start_simulation(self)`: Initiates the AI's journey within Midlands Deep.

###########################################################################################
