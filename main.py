from pyscript import document

g7 = {"Mendoza, Cheree", "Ramos, Elise"}
g8 = {"Schwab, Princess", "Mendoza, Orange"}
g9 = {"Adlawan, Nico", "Musni, Julienne"}
g10 = {"Ledres, Zoey", "Reyes, Therese"}

members = list(g7 | g8 | g9 | g10) #combination magic

def show_members(): #show CURRENT members
    members_list = document.getElementById("members-list")
    members_list.innerHTML = ""
    for member in sorted(members):
        item = document.createElement("li")
        item.textContent = member
        members_list.appendChild(item)

show_members()

def add_member(e):
    name1 = document.getElementById("fn").value #get fn
    name2 = document.getElementById("ln").value #get ln

    full_name = f"{name2.strip()}, {name1.strip()}" #combination magic pt 2
    members.append(full_name) #add
    members.sort() #sort
    show_members() #show new list