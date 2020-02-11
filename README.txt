CS 337: Natural Language Processing (Winter 2020)
Project 1: The Golden Globes
Group 15: George Malty, Mia Willett, Noah Alvarado
GitHub link: https://github.com/noah-alvarado/cs-337-project-1.git

Before running our project, ensure you have followed these steps to create a virtual environment:
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt

To run: python3 gg_api.py

PROJECT DESCRIPTION: Our project identifies the host(s), award names, along with the presenters, nominees, and winners of each award. We additionally identified the most common sentiments of the host(s), and all of the winners.

OUTPUT:
    Host(s): Host Name
    Host reaction: Reaction to Host

    {Award: Award Name
    Presenters: Presenter Name(s)
    Nominees: Nominee Names
    Winner: Winner Name
    Reaction for Award: Reaction to Award} ... for each award



EXTERNAL LIBRARIES USED: pandas, nltk, numpy, six



