[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21364273&assignment_repo_type=AssignmentRepo)
# Welcome to Data Analysis Fundamentals

This GitHub repository is your personal course repository.

It is only accessible by yourself and the class lead.

If you want to make this repository visible to colleagues or potential recruiters, you can make this repository public by clicking on Settings, scrolling down to the bottom of the page then changing the visibility to "Public".

# Setup Instructions

Before starting the course, you need to set up your Python environment with all required packages. Please follow these steps:

## Windows Users
1. Open **VS Code** and open this repository folder
2. Open a new Terminal in VS Code (Top menu: Terminal → New Terminal)
3. Run the setup script by typing: `.\setup_environment_Windows.bat`
4. Wait for the installation to complete (this might take a few minutes)

## Mac/Linux Users
1. Open **VS Code** and open this repository folder
2. Open a new Terminal in VS Code (Top menu: Terminal → New Terminal)
3. Run the setup script by typing: `./setup.sh`
4. IF the script is not executable, make the setup script executable by typing: `chmod +x setup.sh`
5. Wait for the installation to complete (this might take a few minutes)

## Validating Your Setup

After running the setup script, you should verify that everything works correctly:

1. **Command Line Validation**:
   - In the VS Code terminal, type: `python -c "import pandas; print('Setup successful!')"` 
   - If you see "Setup successful!" then the basic packages are installed correctly

2. **Jupyter Notebook Validation**:
   - Navigate to the `demo` folder in VS Code's Explorer panel (left side)
   - Open the file `A_First_demo.ipynb`
   - Click the "Run All" button at the top of the notebook (looks like ▶️)
   - If all cells run without errors and you see outputs with charts and data, your setup is complete!

If you encounter any problems, please contact the class lead for help.

# Python and Jupyter Notebook

This course is a hands-on introduction to data analysis using the programming language Python.

Python was invented by Guido van Rossum and - together with R - is the most widely used language for data analysis.

For this course, we will use Jupyter Notebook. Jupyter Notebook is a web-based computing platform that allows you to combine coding, documentation, and visualization, making it an ideal environment to learn by doing.

# VS Code Basics

If this is your first time using VS Code:
- Open files by clicking on them in the left panel (Explorer)
- Execute code in a Jupyter notebook by clicking the ▶️ button next to a code cell
- Save your work frequently using Ctrl+S (Windows) or Cmd+S (Mac)
- Use Terminal from the top menu when you need to run commands

# How to Pass This Course

In order to pass this course, you will need to complete the homework assignments and submit a personal course project.

Your project needs to be completed by the end of week 4.

## Weekly Homework

Each homework assignment contains scalable difficulty tasks designed to support your individual learning objectives.

To pass the class, you "only" need to complete the TODOs marked with a broccoli: 🥦

The TODOs marked with 1 🌶️, 2 🌶️🌶️ or 3 🌶️🌶️🌶️ hot peppers are optional.

## Personal Course Project

For your personal course project, you need to bring your own data - ideally data from your work or field of study. You should be familiar with the data domain. The source data for your project can be csv, xls, txt, xml, json or any proprietary text format. Your dataset can consist of 1 or several files and should contain enough data (rows, columns, different data types) to showcase the techniques and strategies for data analysis covered in this module.

# Getting Help

If you have questions or run into problems:
- Check the course materials
- Ask questions during class sessions
- Contact the class lead via email

Good luck and enjoy the course!
