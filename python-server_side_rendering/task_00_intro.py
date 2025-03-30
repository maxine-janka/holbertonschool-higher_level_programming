import os
import logging

def generate_invitations(template, attendees):
    """A templating function - Generates personalized invitation files from a template"""
    
    # Verify template is a string
    if not isinstance(template, str):
        logging.error("error: template must be a string")
        return
    
    #Verify attendees is a list of dictionaries
    if not isinstance(attendees, list):
        logging.error("error: attendees must be a list of dictionaries")
        return
    
    # Check if template is empty
    if not template:
        logging.error("error: Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    # Extract values in attendees for template placeholders, default to "N/A" if key missing
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Replace placeholders in template with attendee values
        invite = template.replace("{name}", name)
        invite = invite.replace("{event_title}", event_title)
        invite = invite.replace("{event_date}", str(event_date))
        invite = invite.replace("{event_location}", event_location)

        # Generate invu=ite with specified file name
        file_name = f"output_{index}.txt"
        
        # Check if file already exists
        if os.path.exists(file_name):
            raise print("File already exists")

        try:
            # Open file in write mode
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(invite) # Write invite into file
                print(f"Invitation {index} generated ")
        except Exception as e:
            print(f"Unable to generate invitation file")



