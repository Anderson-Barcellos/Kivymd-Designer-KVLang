
# Kivy Dynamic Interface Loader

This repository contains a Kivy-based application that dynamically loads and displays a `.kv` file. The application continuously checks for changes in the `test.kv` file and updates the interface in real-time.

## Features

- **Predefined Window Size:** The application starts with a fixed window size of 800x1200 pixels.
- **Dynamic Interface Loading:** Automatically updates the interface when changes in the `test.kv` file are detected.
- **Error Handling:** Displays any errors that occur during the loading of the `.kv` file.

## Getting Started

### Prerequisites

- Python 3.x
- Kivy
- KivyMD

You can install the necessary libraries using pip:

```bash
pip install kivy kivymd
```

### Running the Application

1. **Clone the Repository:**
   
    ```bash
    git clone https://github.com/your_username/kivy-dynamic-interface-loader.git
    cd kivy-dynamic-interface-loader
    ```

2. **Create the `test.kv` File:**

    The script will automatically create a `test.kv` file if it does not exist. Edit this file to define your Kivy interface.

3. **Run the Script:**

    ```bash
    python main.py
    ```

## Code Overview

### Configuration

The initial window size and the non-resizable property are set at the very beginning of the script using `kivy.config.Config`.

### Widgets

- **MDFloatLayout:** The root widget of the application.
- **MDLabel:** A placeholder label for displaying the contents of the `.kv` file or any errors encountered.

### Main Application Class

```python
class KvApp(MDApp):
    """Application class. Main entry point to the application.
    Inherits from the MDApp class.
    """
```

- **Initialization:** Initializes the application and creates a `rendered` attribute to store the contents of the `.kv` file.
- **on_start:** Schedules the `cicle` method to run periodically to check for changes in the `.kv` file.
- **build:** Sets up the root widget and creates a placeholder label.
- **cicle:** Checks if the contents of the `.kv` file have changed and calls the `update` method if they have.
- **update:** Updates the interface based on the new contents of the `.kv` file or displays an error message if there's an issue.

### Error Handling

If there's an error during the dynamic loading of the `.kv` file, it catches the exception and displays an error message within the application window.

## Limitations

- The application does not handle complex `.kv` files that require additional Python classes or methods.
- The window size is fixed and cannot be resized by the user.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

```
