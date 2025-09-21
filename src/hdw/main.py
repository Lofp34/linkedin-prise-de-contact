#!/usr/bin/env python
import sys
from hdw.crew import hdwcrew

def run():
    """
    Run the crew.
    """
    inputs = {"prospect": "tu crées un document qui reprend toutes les infomations du profil linkedin de lionel bro, biographe à nîmes. Tu enrichis ce document avec ces 5 derniers posts et ses 5 derniers commentaires."} 
    hdwcrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()