import os


def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("Invalid input: template must be a string.")

        if not isinstance(attendees, list):
            raise TypeError("Invalid input: attendees must be \
                            a list of dictionaries")

        if not all(isinstance(attendee, dict) for attendee in attendees):
            raise TypeError("Invalid input: attendees must be \
                             a list of dictionaries")

    except TypeError as e:
        print(f"Error: {e}")
        return e

    try:
        if not template.strip():
            raise ValueError("Template is empty, no output files generated.")

        if not attendees:
            raise ValueError("No data provided, no output files generated.")

    except ValueError as e:
        print(f"Error: {e}")
        return e

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") if attendee.get(
            "event_date") is not None else "N/A"
        event_location = attendee.get("event_location", "N/A")

        personalized_invitation = template.replace("{name}", name) \
            .replace("{event_title}", event_title) \
            .replace("{event_date}", event_date) \
            .replace("{event_location}", event_location)

        output_filename = f'output_{index}.txt'

        if os.path.exists(output_filename):
            print(f"File {output_filename} already exists. Skipping.")
            continue

        try:
            with open(output_filename, 'w') as file:
                file.write(personalized_invitation)
        except Exception as e:
            print(f"Error: {e}")
            return e


if __name__ == "__main__":
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
