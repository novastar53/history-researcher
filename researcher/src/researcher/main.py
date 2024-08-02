#!/usr/bin/env python
import sys
from researcher.crew import ResearcherCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Sculptures excavated from the Satvahana capital at Mansar'
    }
    ResearcherCrew().crew().kickoff(inputs=inputs)


if __name__=="__main__":
    run()