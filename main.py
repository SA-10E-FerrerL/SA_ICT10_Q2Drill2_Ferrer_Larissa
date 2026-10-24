from js import document

# SCIENCE CLUB MEMBERS

# 1st - Grade 7 SET
grade7 = {
    "Lara Ferrer",
    "Czyke Lizarda",
    "Marinette Dupain-Cheng"
}

# 2nd - Grade 8 SET
grade8 = {
    "Adrien Agreste",
    "Alya Césaire",
    "Nino Lahiffe"
}

# 3rd - Grade 9 SET
grade9 = {
    "Luka Couffaine",
    "Katniss Everdeen",
    "Peeta Mellark"
}

# 4th - Grade 10 SET
grade10 = {
    "Diana Akari",
    "Lea Johnson"
}


# MASTER SET
# Combines all four grade sets using the union operator
master_set = grade7 | grade8 | grade9 | grade10


# DISPLAY ALL MEMBERS
def display_members():

    # Converts the master set into an HTML list
    members_html = "<br>".join(master_set)

    # Displays all members and the total count
    document.getElementById("output").innerHTML = f"""
        <h3>📋 Science Club Members</h3>

        <p class="member-list">
            {members_html}
        </p>

        <hr>

        <h4 class="total">
            👥 Total Number of Members: {len(master_set)}
        </h4>

        """ # I forgot to put the """ so I was struggling so bad  but what it does is that it allows me to write a multi-line string in Python. It is used to create a string that spans multiple lines, making it easier to format and read. In this case, it is used to create the HTML content that will be displayed on the webpage.

# Add a new member to the master set and update the display

def result_checker(event):

    # Gets the first name entered by the user
    first_name = document.getElementById("first_name").value.strip()

    # Gets the last name entered by the user
    last_name = document.getElementById("last_name").value.strip()

    # Combines the first and last names
    new_member = f"{first_name} {last_name}".strip()

    # Adds the new member to the master set
    master_set.add(new_member)

    # Updates the displayed member list
    display_members()

    # Clears the input boxes
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


# INITIAL DISPLAY
display_members()