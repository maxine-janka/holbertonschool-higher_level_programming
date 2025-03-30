import os
import logging

def generate_invitations(template, attendees):
    """A templating function - Generates personalized invitation files from a template"""
    if not isinstance(template, str):
        logging.error("error: template must be a string")
        return


