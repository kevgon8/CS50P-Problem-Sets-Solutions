# Instagram Followers Analyzer

#### Video Demo:  <URL https://youtu.be/tKzBaumflmU>

#### Description:
Welcome to Instagram Followers Analyzer README. This project lets you analyze your Instagram followers and following lists. It's built using Python and Tkinter for the GUI. This tool allows users to input their followers and following lists, analyzes the data to identify users who don't follow back and users you don't follow back, and displays the results in a graphical user interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Author](#author)
- [Contact](#contact)

## Features

- **Interactive Input**: Input your followers and following lists via text input widgets. This feature allows users to easily copy and paste their lists directly into the application without the need for file uploads or other complex input methods. The user-friendly text widgets support large lists, making it easy to handle extensive data.
- **Comprehensive Analysis**: Analyze followers and following to identify users not following you back and users you don't follow back. The analysis is performed using efficient algorithms that ensure quick and accurate results, even for users with thousands of followers and following. This feature helps users manage their Instagram connections more effectively by providing clear insights into their follower dynamics.
- **Clear Visualization**: Display results in a graphical user interface with labeled output fields for easy interpretation. The results are presented in a clean and organized manner, with separate sections for users not following you back and users you don't follow back. This clear visualization makes it easy for users to take action based on the analysis.
- **Cross-Platform Compatibility**: The application is built using Python and Tkinter, making it compatible with multiple operating systems, including Windows, macOS, and Linux. Users can run the application on their preferred platform without any issues.


## Installation

To use the Instagram Followers Analyzer, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/kevgon8/final_project.git
    ```

2. Navigate into the project directory:
    ```bash
    cd final_project
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

- To run the Instagram Followers Analyzer:
    -  Execute the following command in your terminal:

    ```bash
    python project.py
    ```
    - Instagram allows users to download their data, which includes information about their followers and following lists. You can request a copy of your Instagram data through the app and Instagram will compile the data and send it to you via email. Follow the steps below to download your followers and following information:
        1. Click menu (three horizontallines)  in the bottom left, then click Your Activity.
        2. Click Download your information.
        3. Click Continue.
        4. Click Download or transfer information.
        5. Select the profiles that you'd like to download information from and then Click Next.
        6. Select how much information you want to download (Followers and Follwing in this case) and click Next.
        7. Choose if you want to download your information to a device or directly transfer your information to a destination, and click Next.
        8. If you select Download to device, choose your file options:
            - The date range
            - The notification email
            - The format of your download request.
            - The quality of photos, videos and other media.
        9. Click Create files and Instagram will send your information to you via email

    - Copy your Followers list and paste it in the left text widget of the Instagram Followers Analyzer
    - Copy your Followings list and paste it in the right text widget of the Instagram Followers Analyzer
    - Click on the button that says 'Analyze'. The tool will process the data and display the results in the GUI.

## Testing

- To test Instagram Followers Analyzer, execute the following command in your terminal:

    ```bash
    python test_project.py
    ```

## Technologies Used

- **Python**: The core programming language used for developing the application. Python is chosen for its simplicity and extensive library support.
- **Tkinter**: The standard GUI library for Python, used to create the graphical user interface for the application. Tkinter provides a fast and easy way to create GUI applications.
- **ttkbootstrap**: A themed widget set for Tkinter, used to enhance the visual appearance of the application. ttkbootstrap provides modern themes and styles for Tkinter widgets, making the application look more professional and polished.

## File Structure

```bash
final_project/
├── project.py
├── README.md
├── requirements.txt
└── test_project.py
```

## Future Improvements

Here are some planned improvements and features for future versions of the Instagram Followers Analyzer:
- Enhanced Visualization: Improve the GUI to include charts and graphs for a more visual representation of the analysis results.
- Dark Mode: Add a dark mode option for better usability in low-light environments.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the project
2. Create your feature branch:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/AmazingFeature
    ```
5. Open a pull request

## Author

Kevin Gonsalves

## Contact

For questions or feedback regarding Instagram Followers Analyzer, feel free to reach out:
- Email: kevgonsalves14@gmail.com
