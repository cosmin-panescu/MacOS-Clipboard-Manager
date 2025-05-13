# ClipboardManager

## Overview
ClipboardManager is a lightweight, menu bar application for macOS that provides clipboard history management. It quietly runs in the background, tracks copied text, and allows quick access to previously copied items.


## Features
- Track up to 10 recent clipboard items
- Access clipboard history from the menu bar
- Quickly paste previous items with a single click
- Automatically removes duplicates
- Efficient resource usage with adaptive monitoring
- Simple and clean menu bar interface

## Installation

### Option 1: Download the Application
The easiest way to install ClipboardManager is to download the pre-built application from the Releases section of this repository. Simply:

1. Go to the [Releases]([https://github.com/yourusername/clipboardmanager/releases](https://github.com/cosmin-panescu/MacOS-Clipboard-Manager/releases/tag/v1.0.0)) page
2. Download the latest version
3. Unzip the file
4. Drag ClipboardManager to your Applications folder
5. Launch the application

### Option 2: Build from Source
If you prefer to build from source:

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install rumps pyperclip
   ```
3. Run the script:
   ```
   python clipboard_manager.py
   ```

## Usage

Once launched, ClipboardManager runs silently in your menu bar. You'll see a clipboard icon (📋) indicating that the application is active.

### Basic Operations

- **Access Clipboard History**: Click on the clipboard icon in the menu bar to see your clipboard history
- **Paste Previous Items**: Click on any item in the menu to copy it to your clipboard
- **Clear History**: Select "Clear History" from the menu to reset your clipboard history
- **Quit**: Select "Quit" to exit the application

## Technical Details

ClipboardManager uses:
- `rumps` to create the macOS menu bar application
- `pyperclip` to interact with the clipboard
- `NSPasteboard` from Foundation to efficiently monitor clipboard changes
- Threading to ensure responsive performance
- Adaptive sleep times to minimize resource usage

The application limits clipboard entries to 10,000 characters for display and storage efficiency.

## Limitations

- Only tracks text content (not images or files)
- Maximum history of 10 items
- Text entries longer than 10,000 characters are truncated for storage
- Menu display shows only the first 47 characters of long entries

## License

[MIT License](LICENSE)

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests to improve ClipboardManager.

---

**Note:** Remember that you can always download the latest version of ClipboardManager from the Releases section of this repository instead of building from source.
