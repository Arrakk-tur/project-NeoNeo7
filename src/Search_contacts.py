elif command == 'find':
    try:
        contact_name = ' '.join(args)
        contact_record = contacts.find(contact_name)
        print(f"Contact found: {contact_record}")
    except ValueError as e:
        print(e)
