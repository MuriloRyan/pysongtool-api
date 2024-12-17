def note_validation(note: str) -> dict:
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note = note.upper()

    response = {}
    strikes = 0

    if note not in notes:
        strikes += 1

        response['is_valid'] = False
        response[f'strike {strikes}'] = {
            'is_valid': False,
            'exception': 'WrongNote',
            'message': f'You entered a wrong note, {note} is not a valid note, remmember to use only standard and sharp notes (C,C#,D,#,...)'
        }

    else:
        response['is_valid'] = True
        response['message'] = 'All data has been validated sucessfully'
    
    return response