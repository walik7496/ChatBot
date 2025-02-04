# Chat Bot

A simple Python-based chatbot application with a graphical user interface (GUI) built using Tkinter. This chatbot allows basic text-based interactions, responding to predefined inputs stored in a text file.

## Features

- **Basic Text Responses:** Responds to user inputs based on predefined key-value pairs.
- **Scrollable Chat History:** Displays conversation history with scroll functionality.
- **Easy Response Customization:** Supports adding new responses through a `responses.txt` file.
- **Keyboard Shortcut:** Press `Enter` to send messages quickly.

## Prerequisites

- **Python 3.x**
- Python Libraries:
  - `tkinter` (comes pre-installed with Python)
  - `os` (built-in module)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/walik7496/chatbot.git
   cd chat-bot
   ```

2. **Run the application:**
   ```bash
   python chatbot.py
   ```

## Usage

### Instructions:
- Type your message in the input field.
- Click the **Send** button or press **Enter** to send the message.
- The bot will respond if it finds a matching input in `responses.txt`. Otherwise, it will reply with "Sorry, I don't understand."

### Adding Custom Responses:
- Open the `responses.txt` file.
- Add new responses in the format:
  ```
  hello: Hi there!
  how are you: I'm just a bot, but I'm doing fine!
  ```
- Save the file and restart the chatbot for changes to take effect.

## File Structure

```
.
├── chatbot.py
├── responses.txt (optional, stores predefined responses)
└── README.md
```

## Troubleshooting

- **Bot Doesn't Respond Correctly:** Ensure your `responses.txt` is properly formatted (key: value pairs).
- **Missing `responses.txt`:** The bot will still function but only respond with default "Sorry, I don't understand." messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).

