# 📞 Known 1.0 Tool phonenumbers 🌍

This Python script is a command-line tool designed to retrieve information about a phone number, including its location and carrier details. It leverages the `phonenumbers` library for parsing and validating phone numbers, the OpenCage Geocoder API for detailed location information, and `folium` for generating an interactive map of the phone number's approximate location. This tool helps you quickly identify the origin and carrier of a phone number.

## 🚀 Key Features

- **Phone Number Validation:** Ensures the entered phone number is in a valid format.
- **Location Lookup:** Retrieves the geographical location associated with the phone number using the OpenCage Geocoder API.
- **Carrier Identification:** Identifies the carrier associated with the phone number.
- **Interactive Map Generation:** Creates an HTML file containing an interactive map showing the phone number's location using `folium`.
- **User-Friendly Output:** Displays the location and carrier information in a clear and concise format.
- **API Key Handling:** Securely retrieves the OpenCage Geocoder API key from environment variables or prompts the user for input.
- **Normalization:** Normalizes the phone number to international format.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Phone Number Parsing & Validation:** `phonenumbers`
- **Geocoding API:** OpenCage Geocoder
- **Map Generation:** `folium`
- **Environment Variables:** `os`
- **Error Handling:** `sys`

## 📦 Getting Started

### Prerequisites

- Python 3.6 or higher
- An OpenCage Geocoder API key (You can obtain one for free at [https://opencagedata.com/](https://opencagedata.com/))

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required Python packages:

    ```bash
    pip install phonenumbers opencage folium
    ```

### Running Locally

1.  Set the OpenCage Geocoder API key as an environment variable:

    ```bash
    export API_KEY="YOUR_API_KEY"
    ```

    Or, you can enter it when prompted by the script.

2.  Run the script:

    ```bash
    python py.py
    ```

3.  Enter the phone number when prompted.

4.  The script will display the location and carrier information and generate an HTML file named `MyMap.html` containing the map.

## 💻 Usage

After running the script, it will prompt you to enter a phone number. Enter the phone number in any format, and the script will attempt to normalize it to the international format. The script will then display the location and carrier information associated with the phone number. An HTML file named `MyMap.html` will also be created, which you can open in your browser to view the interactive map.

## 📂 Project Structure

```
.
├── py.py           # Main Python script
├── README.md       # Project documentation
```

## 📸 Screenshots
<img width="473" height="227" alt="image" src="https://github.com/user-attachments/assets/ca9d559a-f65e-486f-9f07-fc0ae8ba6459" />



## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.



## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [farilpratamap@gmail.com] / My instagram @fr.project.id

## 💖 Thanks

Thank you for checking out this project! I hope you find it useful.

This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
